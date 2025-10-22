"""Order routes"""
from flask import Blueprint, request, jsonify
from db import get_transaction, query, query_one, execute
import psycopg2

orders_bp = Blueprint('orders', __name__, url_prefix='/api/orders')

# GET all orders
@orders_bp.route('', methods=['GET'])
def get_all_orders():
    try:
        results = query(
            '''SELECT o.*, 
                      c.first_name, 
                      c.last_name, 
                      c.email
               FROM orders o
               JOIN customers c ON o.customer_id = c.customer_id
               ORDER BY o.order_date DESC'''
        )
        return jsonify(results or [])
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# GET a specific order by ID with order items
@orders_bp.route('/<int:id>', methods=['GET'])
def get_order(id):
    try:
        # Get order details
        order_result = query_one(
            '''SELECT o.*, 
                      c.first_name, 
                      c.last_name, 
                      c.email
               FROM orders o
               JOIN customers c ON o.customer_id = c.customer_id
               WHERE o.order_id = %s''',
            (id,)
        )
        
        if not order_result:
            return jsonify({'message': 'Order not found'}), 404
        
        # Get order items
        items_result = query(
            '''SELECT oi.*, 
                      p.product_name, 
                      p.description,
                      c.category_name
               FROM order_items oi
               JOIN products p ON oi.product_id = p.product_id
               JOIN categories c ON p.category_id = c.category_id
               WHERE oi.order_id = %s''',
            (id,)
        )
        
        order_result['items'] = items_result or []
        
        return jsonify(order_result)
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# GET orders by customer
@orders_bp.route('/customer/<int:customer_id>', methods=['GET'])
def get_orders_by_customer(customer_id):
    try:
        # Check if customer exists
        customer_check = query_one(
            'SELECT * FROM customers WHERE customer_id = %s',
            (customer_id,)
        )
        
        if not customer_check:
            return jsonify({'message': 'Customer not found'}), 404
        
        results = query(
            '''SELECT o.*, 
                      c.first_name, 
                      c.last_name, 
                      c.email
               FROM orders o
               JOIN customers c ON o.customer_id = c.customer_id
               WHERE o.customer_id = %s
               ORDER BY o.order_date DESC''',
            (customer_id,)
        )
        
        return jsonify(results or [])
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# POST create a new order
@orders_bp.route('', methods=['POST'])
def create_order():
    conn = get_transaction()
    if conn is None:
        return jsonify({'error': 'Database connection error'}), 500
    
    cursor = None
    try:
        cursor = conn.cursor()
        
        data = request.get_json()
        
        customer_id = data.get('customer_id')
        total_amount = data.get('total_amount')
        status = data.get('status', 'pending')
        shipping_address = data.get('shipping_address')
        shipping_city = data.get('shipping_city')
        shipping_state = data.get('shipping_state')
        shipping_zip_code = data.get('shipping_zip_code')
        items = data.get('items', [])
        
        # Validate required fields
        if not customer_id or total_amount is None or not items or len(items) == 0:
            return jsonify({'message': 'Customer ID, total amount, and at least one item are required'}), 400
        
        # Begin transaction
        cursor.execute('BEGIN')
        
        # Check if customer exists
        cursor.execute('SELECT * FROM customers WHERE customer_id = %s', (customer_id,))
        if not cursor.fetchone():
            cursor.execute('ROLLBACK')
            return jsonify({'message': 'Invalid customer ID'}), 400
        
        # Create the order
        cursor.execute(
            '''INSERT INTO orders 
               (customer_id, total_amount, status, shipping_address, shipping_city, shipping_state, shipping_zip_code) 
               VALUES (%s, %s, %s, %s, %s, %s, %s) 
               RETURNING *''',
            (customer_id, total_amount, status, shipping_address, shipping_city, shipping_state, shipping_zip_code)
        )
        order_result = cursor.fetchone()
        order_id = order_result[0]
        
        # Add order items
        for item in items:
            # Validate item data
            if not item.get('product_id') or not item.get('quantity') or not item.get('unit_price'):
                cursor.execute('ROLLBACK')
                return jsonify({'message': 'Each item must have product_id, quantity, and unit_price'}), 400
            
            # Check if product exists and has enough stock
            cursor.execute('SELECT * FROM products WHERE product_id = %s', (item['product_id'],))
            product = cursor.fetchone()
            
            if not product:
                cursor.execute('ROLLBACK')
                return jsonify({'message': f"Product with ID {item['product_id']} not found"}), 400
            
            product_name = product[1]
            stock_quantity = product[5]
            
            if stock_quantity < item['quantity']:
                cursor.execute('ROLLBACK')
                return jsonify({'message': f'Not enough stock for product {product_name}'}), 400
            
            # Calculate subtotal
            subtotal = item['quantity'] * item['unit_price']
            
            # Add order item
            cursor.execute(
                '''INSERT INTO order_items 
                   (order_id, product_id, quantity, unit_price, subtotal) 
                   VALUES (%s, %s, %s, %s, %s)''',
                (order_id, item['product_id'], item['quantity'], item['unit_price'], subtotal)
            )
            
            # Update product stock
            cursor.execute(
                '''UPDATE products 
                   SET stock_quantity = stock_quantity - %s 
                   WHERE product_id = %s''',
                (item['quantity'], item['product_id'])
            )
        
        conn.commit()
        
        # Get the complete order with items
        complete_order = query_one(
            '''SELECT o.*, 
                      c.first_name, 
                      c.last_name, 
                      c.email
               FROM orders o
               JOIN customers c ON o.customer_id = c.customer_id
               WHERE o.order_id = %s''',
            (order_id,)
        )
        
        items_result = query(
            '''SELECT oi.*, 
                      p.product_name
               FROM order_items oi
               JOIN products p ON oi.product_id = p.product_id
               WHERE oi.order_id = %s''',
            (order_id,)
        )
        
        complete_order['items'] = items_result or []
        
        return jsonify(complete_order), 201
    except Exception as err:
        conn.rollback()
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        conn.close()

# PUT update an order status
@orders_bp.route('/<int:id>', methods=['PUT'])
def update_order(id):
    try:
        data = request.get_json()
        status = data.get('status')
        
        # Validate status
        if not status:
            return jsonify({'message': 'Status is required'}), 400
        
        # Check if order exists
        existing = query_one(
            'SELECT * FROM orders WHERE order_id = %s',
            (id,)
        )
        
        if not existing:
            return jsonify({'message': 'Order not found'}), 404
        
        # Update order status
        results = execute(
            '''UPDATE orders 
               SET status = %s
               WHERE order_id = %s
               RETURNING *''',
            (status, id)
        )
        
        return jsonify(results[0])
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# DELETE an order
@orders_bp.route('/<int:id>', methods=['DELETE'])
def delete_order(id):
    conn = get_transaction()
    if conn is None:
        return jsonify({'error': 'Database connection error'}), 500
    
    cursor = None
    try:
        cursor = conn.cursor()
        
        # Begin transaction
        cursor.execute('BEGIN')
        
        # Check if order exists
        cursor.execute('SELECT * FROM orders WHERE order_id = %s', (id,))
        if not cursor.fetchone():
            cursor.execute('ROLLBACK')
            return jsonify({'message': 'Order not found'}), 404
        
        # Get order items to restore product stock
        cursor.execute('SELECT * FROM order_items WHERE order_id = %s', (id,))
        items = cursor.fetchall()
        
        # Restore product stock
        for item in items:
            cursor.execute(
                '''UPDATE products 
                   SET stock_quantity = stock_quantity + %s 
                   WHERE product_id = %s''',
                (item[2], item[2])
            )
        
        # Delete order items
        cursor.execute('DELETE FROM order_items WHERE order_id = %s', (id,))
        
        # Delete order
        cursor.execute('DELETE FROM orders WHERE order_id = %s', (id,))
        
        conn.commit()
        
        return jsonify({'message': 'Order deleted successfully'})
    except Exception as err:
        conn.rollback()
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        conn.close()