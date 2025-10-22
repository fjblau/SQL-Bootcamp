# Python REST API - E-commerce API

This project demonstrates how to build a simple REST API using Flask that connects to a PostgreSQL database and provides CRUD operations for an e-commerce system. This is the Python alternative to the Node.js/Express version.

## Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- PostgreSQL (v12 or later)
- Sample e-commerce database (from Day 2)

## Project Setup

### 1. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Configure the database connection:
- Create a `.env` file based on `.env.example`
- Update the database connection parameters with your PostgreSQL credentials

Example `.env` file:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce
DB_USER=postgres
DB_PASSWORD=your_password
PORT=3000
FLASK_ENV=development
```

### 3. Start the server:
```bash
python server.py
```

The server will start on `http://localhost:3000`

## Project Structure

- `server.py` - Main Flask application entry point
- `db.py` - Database connection and query execution module
- `routes/` - API route handlers
  - `customers.py` - Customer-related endpoints
  - `products.py` - Product-related endpoints
  - `orders.py` - Order-related endpoints

## API Endpoints

All endpoints are identical to the JavaScript version.

### Customers

- `GET /api/customers` - Get all customers
- `GET /api/customers/:id` - Get a specific customer
- `POST /api/customers` - Create a new customer
- `PUT /api/customers/:id` - Update a customer
- `DELETE /api/customers/:id` - Delete a customer

### Products

- `GET /api/products` - Get all products
- `GET /api/products/:id` - Get a specific product
- `GET /api/products/category/:categoryId` - Get products by category
- `POST /api/products` - Create a new product
- `PUT /api/products/:id` - Update a product
- `DELETE /api/products/:id` - Delete a product

### Orders

- `GET /api/orders` - Get all orders
- `GET /api/orders/:id` - Get a specific order with items
- `GET /api/orders/customer/:customerId` - Get orders by customer
- `POST /api/orders` - Create a new order
- `PUT /api/orders/:id` - Update an order status
- `DELETE /api/orders/:id` - Delete an order

## Testing the API

You can test the API using tools like:

- cURL from the command line
- Postman desktop application
- VS Code REST Client extension
- Browser for GET requests

### Example cURL Commands

#### Get all customers
```bash
curl -X GET http://localhost:3000/api/customers
```

#### Create a new customer
```bash
curl -X POST http://localhost:3000/api/customers \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Jane","last_name":"Smith","email":"jane.smith@example.com","phone":"555-987-6543","address":"456 Oak Ave","city":"Cambridge","state":"MA","zip_code":"02139"}'
```

#### Get a specific customer
```bash
curl -X GET http://localhost:3000/api/customers/1
```

#### Update a customer
```bash
curl -X PUT http://localhost:3000/api/customers/1 \
  -H "Content-Type: application/json" \
  -d '{"phone":"555-999-9999","city":"Boston"}'
```

#### Get all products
```bash
curl -X GET http://localhost:3000/api/products
```

#### Get products by category
```bash
curl -X GET http://localhost:3000/api/products/category/1
```

#### Create a new product
```bash
curl -X POST http://localhost:3000/api/products \
  -H "Content-Type: application/json" \
  -d '{"product_name":"USB-C Cable","category_id":1,"description":"High-speed USB-C cable","price":19.99,"stock_quantity":100}'
```

#### Get all orders
```bash
curl -X GET http://localhost:3000/api/orders
```

#### Get orders for a specific customer
```bash
curl -X GET http://localhost:3000/api/orders/customer/1
```

#### Create a new order
```bash
curl -X POST http://localhost:3000/api/orders \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "total_amount": 199.98,
    "status": "pending",
    "shipping_address": "123 Main St",
    "shipping_city": "Boston",
    "shipping_state": "MA",
    "shipping_zip_code": "02108",
    "items": [
      {"product_id": 1, "quantity": 1, "unit_price": 149.99},
      {"product_id": 3, "quantity": 1, "unit_price": 49.99}
    ]
  }'
```

#### Update order status
```bash
curl -X PUT http://localhost:3000/api/orders/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"shipped"}'
```

#### Delete a customer
```bash
curl -X DELETE http://localhost:3000/api/customers/9
```

## Development

### Running in Development Mode

The application uses Flask's debug mode when `FLASK_ENV=development` is set in the `.env` file. This enables:
- Auto-reloading when code changes
- Detailed error messages
- Debug toolbar

### Common Issues

**Connection refused:**
- Ensure PostgreSQL is running
- Check your `.env` file for correct database credentials
- Verify the database name is `ecommerce`

**Module not found errors:**
- Ensure you've installed all dependencies: `pip install -r requirements.txt`
- Make sure you're in the correct directory

## Key Differences from JavaScript Version

- Flask instead of Express.js
- psycopg2 instead of pg (Node.js)
- Python context managers for database connections
- Blueprint routing instead of Router middleware
- Dictionary responses instead of JSON objects (Flask handles conversion)

## Error Handling

The API includes proper error handling for:
- Invalid requests (400)
- Not found resources (404)
- Database errors (500)
- Validation errors with descriptive messages

## Security Considerations

This is a demonstration project. In a production environment, you would need to implement:
- Authentication (JWT, OAuth, etc.)
- Input validation and sanitization
- Rate limiting
- HTTPS
- CORS configuration (already implemented)
- Environment variable protection
- SQL injection prevention (parameterized queries are used)