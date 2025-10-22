# Mini REST API Project

This project demonstrates how to build a simple REST API that connects to a PostgreSQL database and provides CRUD operations for an e-commerce system.

**Choose your preferred language:**
- **JavaScript**: Node.js with Express.js (see current directory)
- **Python**: Flask framework (see `python_version/` directory)

Both implementations provide identical functionality and API endpoints.

## Prerequisites

### For JavaScript Version
- Node.js (v14 or later)
- npm (v6 or later)
- PostgreSQL (v12 or later)
- Sample e-commerce database (from Day 2)

### For Python Version
- Python (3.8 or later)
- pip (Python package manager)
- PostgreSQL (v12 or later)
- Sample e-commerce database (from Day 2)

## Project Setup

### JavaScript Version

1. Install dependencies:
   ```bash
   npm install
   ```

2. Configure the database connection:
   - Create a `.env` file based on `.env.example`
   - Update the database connection parameters

3. Start the server:
   ```bash
   npm start
   ```

### Python Version

1. Install dependencies:
   ```bash
   cd python_version
   pip install -r requirements.txt
   ```

2. Configure the database connection:
   - Create a `.env` file based on `.env.example`
   - Update the database connection parameters

3. Start the server:
   ```bash
   python server.py
   ```

For more details, see [Python Version README](./python_version/README.md)

## Project Structure

- `server.js` - Main application entry point
- `db.js` - Database connection module
- `routes/` - API route handlers
  - `customers.js` - Customer-related endpoints
  - `products.js` - Product-related endpoints
  - `orders.js` - Order-related endpoints

## API Endpoints

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
  -d '{"first_name":"John","last_name":"Doe","email":"john.doe@example.com","phone":"555-123-4567","address":"123 Main St","city":"Boston","state":"MA","zip_code":"02108"}'
```

#### Update a product
```bash
curl -X PUT http://localhost:3000/api/products/1 \
  -H "Content-Type: application/json" \
  -d '{"product_name":"Updated Smartphone X","price":799.99,"stock_quantity":45}'
```

## Error Handling

The API includes proper error handling for:
- Invalid requests
- Database errors
- Not found resources
- Validation errors

## Security Considerations

This is a demonstration project. In a production environment, you would need to implement:
- Authentication (JWT, OAuth, etc.)
- Input validation and sanitization
- Rate limiting
- HTTPS
- CORS configuration
- Environment variable protection