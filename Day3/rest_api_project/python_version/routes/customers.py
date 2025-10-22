"""Customer routes"""
from flask import Blueprint, request, jsonify
from db import query, query_one, execute
import psycopg2

customers_bp = Blueprint('customers', __name__, url_prefix='/api/customers')

# GET all customers
@customers_bp.route('', methods=['GET'])
def get_all_customers():
    try:
        results = query(
            'SELECT * FROM customers ORDER BY last_name, first_name'
        )
        return jsonify(results or [])
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# GET a specific customer by ID
@customers_bp.route('/<int:id>', methods=['GET'])
def get_customer(id):
    try:
        result = query_one(
            'SELECT * FROM customers WHERE customer_id = %s',
            (id,)
        )
        
        if not result:
            return jsonify({'message': 'Customer not found'}), 404
        
        return jsonify(result)
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# POST create a new customer
@customers_bp.route('', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        city = data.get('city')
        state = data.get('state')
        zip_code = data.get('zip_code')
        
        # Validate required fields
        if not first_name or not last_name or not email:
            return jsonify({'message': 'First name, last name, and email are required'}), 400
        
        results = execute(
            '''INSERT INTO customers 
               (first_name, last_name, email, phone, address, city, state, zip_code) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
               RETURNING *''',
            (first_name, last_name, email, phone, address, city, state, zip_code)
        )
        
        return jsonify(results[0]), 201
    except psycopg2.IntegrityError as err:
        if 'unique constraint' in str(err):
            return jsonify({'message': 'Email already exists'}), 400
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# PUT update a customer
@customers_bp.route('/<int:id>', methods=['PUT'])
def update_customer(id):
    try:
        data = request.get_json()
        
        # Check if customer exists
        existing = query_one(
            'SELECT * FROM customers WHERE customer_id = %s',
            (id,)
        )
        
        if not existing:
            return jsonify({'message': 'Customer not found'}), 404
        
        first_name = data.get('first_name', existing['first_name'])
        last_name = data.get('last_name', existing['last_name'])
        email = data.get('email', existing['email'])
        phone = data.get('phone', existing['phone'])
        address = data.get('address', existing['address'])
        city = data.get('city', existing['city'])
        state = data.get('state', existing['state'])
        zip_code = data.get('zip_code', existing['zip_code'])
        
        results = execute(
            '''UPDATE customers 
               SET first_name = %s, last_name = %s, email = %s, 
                   phone = %s, address = %s, city = %s, 
                   state = %s, zip_code = %s
               WHERE customer_id = %s
               RETURNING *''',
            (first_name, last_name, email, phone, address, city, state, zip_code, id)
        )
        
        return jsonify(results[0])
    except psycopg2.IntegrityError as err:
        if 'unique constraint' in str(err):
            return jsonify({'message': 'Email already exists'}), 400
        return jsonify({'error': 'Database error', 'message': str(err)}), 500
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500

# DELETE a customer
@customers_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer(id):
    try:
        # Check if customer exists
        existing = query_one(
            'SELECT * FROM customers WHERE customer_id = %s',
            (id,)
        )
        
        if not existing:
            return jsonify({'message': 'Customer not found'}), 404
        
        # Check if customer has orders
        order_check = query_one(
            'SELECT * FROM orders WHERE customer_id = %s LIMIT 1',
            (id,)
        )
        
        if order_check:
            return jsonify({'message': 'Cannot delete customer with existing orders'}), 400
        
        execute('DELETE FROM customers WHERE customer_id = %s', (id,))
        
        return jsonify({'message': 'Customer deleted successfully'})
    except Exception as err:
        return jsonify({'error': 'Database error', 'message': str(err)}), 500