"""Product routes"""
from flask import Blueprint, request, jsonify
from db import query, query_one, execute
import psycopg2

products_bp = Blueprint('products', __name__, url_prefix='/api/products')

# GET all products
@products_bp.route('', methods=['GET'])
def get_all_products():
    try:
        results = query(
            '''SELECT p.*, c.category_name 
               FROM products p
               JOIN categories c ON p.category_id = c.category_id
               ORDER BY p.product_name'''
        )
        return jsonify(results or [])
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# GET a specific product by ID
@products_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    try:
        result = query_one(
            '''SELECT p.*, c.category_name 
               FROM products p
               JOIN categories c ON p.category_id = c.category_id
               WHERE p.product_id = %s''',
            (id,)
        )
        
        if not result:
            return jsonify({'message': 'Product not found'}), 404
        
        return jsonify(result)
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# GET products by category
@products_bp.route('/category/<int:category_id>', methods=['GET'])
def get_products_by_category(category_id):
    try:
        results = query(
            '''SELECT p.*, c.category_name 
               FROM products p
               JOIN categories c ON p.category_id = c.category_id
               WHERE p.category_id = %s
               ORDER BY p.product_name''',
            (category_id,)
        )
        
        return jsonify(results or [])
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# POST create a new product
@products_bp.route('', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        
        product_name = data.get('product_name')
        category_id = data.get('category_id')
        description = data.get('description')
        price = data.get('price')
        stock_quantity = data.get('stock_quantity', 0)
        
        # Validate required fields
        if not product_name or not category_id or price is None:
            return jsonify({'message': 'Product name, category ID, and price are required'}), 400
        
        # Validate price and stock quantity
        try:
            price = float(price)
            if price <= 0:
                return jsonify({'message': 'Price must be a positive number'}), 400
        except (ValueError, TypeError):
            return jsonify({'message': 'Price must be a valid number'}), 400
        
        try:
            stock_quantity = int(stock_quantity or 0)
            if stock_quantity < 0:
                return jsonify({'message': 'Stock quantity must be a non-negative number'}), 400
        except (ValueError, TypeError):
            return jsonify({'message': 'Stock quantity must be a valid number'}), 400
        
        results = execute(
            '''INSERT INTO products 
               (product_name, category_id, description, price, stock_quantity) 
               VALUES (%s, %s, %s, %s, %s) 
               RETURNING *''',
            (product_name, category_id, description, price, stock_quantity)
        )
        
        product = results[0]
        
        # Get the category name for the response
        category = query_one(
            'SELECT category_name FROM categories WHERE category_id = %s',
            (category_id,)
        )
        
        if category:
            product['category_name'] = category['category_name']
        
        return jsonify(product), 201
    except psycopg2.IntegrityError as err:
        if 'foreign key' in str(err):
            return jsonify({'message': 'Invalid category ID'}), 400
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# PUT update a product
@products_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        data = request.get_json()
        
        # Check if product exists
        existing = query_one(
            'SELECT * FROM products WHERE product_id = %s',
            (id,)
        )
        
        if not existing:
            return jsonify({'message': 'Product not found'}), 404
        
        product_name = data.get('product_name', existing['product_name'])
        category_id = data.get('category_id', existing['category_id'])
        description = data.get('description', existing['description']) if 'description' in data else existing['description']
        price = data.get('price', existing['price'])
        stock_quantity = data.get('stock_quantity', existing['stock_quantity']) if 'stock_quantity' in data else existing['stock_quantity']
        
        # Validate price and stock quantity if provided
        if 'price' in data:
            try:
                price = float(price)
                if price <= 0:
                    return jsonify({'message': 'Price must be a positive number'}), 400
            except (ValueError, TypeError):
                return jsonify({'message': 'Price must be a valid number'}), 400
        
        if 'stock_quantity' in data:
            try:
                stock_quantity = int(stock_quantity)
                if stock_quantity < 0:
                    return jsonify({'message': 'Stock quantity must be a non-negative number'}), 400
            except (ValueError, TypeError):
                return jsonify({'message': 'Stock quantity must be a valid number'}), 400
        
        results = execute(
            '''UPDATE products 
               SET product_name = %s, 
                   category_id = %s, 
                   description = %s, 
                   price = %s, 
                   stock_quantity = %s
               WHERE product_id = %s
               RETURNING *''',
            (product_name, category_id, description, price, stock_quantity, id)
        )
        
        product = results[0]
        
        # Get the category name for the response
        category = query_one(
            'SELECT category_name FROM categories WHERE category_id = %s',
            (category_id,)
        )
        
        if category:
            product['category_name'] = category['category_name']
        
        return jsonify(product)
    except psycopg2.IntegrityError as err:
        if 'foreign key' in str(err):
            return jsonify({'message': 'Invalid category ID'}), 400
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# DELETE a product
@products_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        # Check if product exists
        existing = query_one(
            'SELECT * FROM products WHERE product_id = %s',
            (id,)
        )
        
        if not existing:
            return jsonify({'message': 'Product not found'}), 404
        
        # Check if product is in any order
        order_check = query_one(
            'SELECT * FROM order_items WHERE product_id = %s LIMIT 1',
            (id,)
        )
        
        if order_check:
            return jsonify({'message': 'Cannot delete product that exists in orders'}), 400
        
        execute('DELETE FROM products WHERE product_id = %s', (id,))
        
        return jsonify({'message': 'Product deleted successfully'})
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500