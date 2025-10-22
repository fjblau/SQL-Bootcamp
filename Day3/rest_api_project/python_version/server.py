"""Main Flask server"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Import route blueprints
from routes.customers import customers_bp
from routes.products import products_bp
from routes.orders import orders_bp

load_dotenv()

# Create Flask app
app = Flask(__name__)
port = os.getenv('PORT', 3000)

# Enable CORS
CORS(app)

# Middleware to log requests
@app.before_request
def log_request():
    print(f'{request.method} {request.path}')

# Register blueprints
app.register_blueprint(customers_bp)
app.register_blueprint(products_bp)
app.register_blueprint(orders_bp)

# Root route
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({
        'message': 'Welcome to the E-commerce API',
        'endpoints': {
            'customers': '/api/customers',
            'products': '/api/products',
            'orders': '/api/orders'
        }
    })

# Error handling middleware
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
        'message': f'The requested resource was not found'
    }), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'error': 'Something went wrong!',
        'message': str(error)
    }), 500

# Generic error handler
@app.errorhandler(Exception)
def handle_error(error):
    return jsonify({
        'error': 'Something went wrong!',
        'message': str(error)
    }), 500

if __name__ == '__main__':
    app.run(debug=True, port=int(port), host='0.0.0.0')