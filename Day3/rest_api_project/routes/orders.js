// Order routes
const express = require('express');
const router = express.Router();
const db = require('../db');

// GET all orders
router.get('/', async (req, res, next) => {
  try {
    const result = await db.query(
      `SELECT o.*, 
              c.first_name, 
              c.last_name, 
              c.email
       FROM orders o
       JOIN customers c ON o.customer_id = c.customer_id
       ORDER BY o.order_date DESC`
    );
    res.json(result.rows);
  } catch (err) {
    next(err);
  }
});

// GET a specific order by ID with order items
router.get('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    
    // Get order details
    const orderResult = await db.query(
      `SELECT o.*, 
              c.first_name, 
              c.last_name, 
              c.email
       FROM orders o
       JOIN customers c ON o.customer_id = c.customer_id
       WHERE o.order_id = $1`,
      [id]
    );
    
    if (orderResult.rows.length === 0) {
      return res.status(404).json({ message: 'Order not found' });
    }
    
    // Get order items
    const itemsResult = await db.query(
      `SELECT oi.*, 
              p.product_name, 
              p.description,
              c.category_name
       FROM order_items oi
       JOIN products p ON oi.product_id = p.product_id
       JOIN categories c ON p.category_id = c.category_id
       WHERE oi.order_id = $1`,
      [id]
    );
    
    // Combine order with its items
    const order = orderResult.rows[0];
    order.items = itemsResult.rows;
    
    res.json(order);
  } catch (err) {
    next(err);
  }
});

// GET orders by customer
router.get('/customer/:customerId', async (req, res, next) => {
  try {
    const { customerId } = req.params;
    
    // Check if customer exists
    const customerCheck = await db.query(
      'SELECT * FROM customers WHERE customer_id = $1',
      [customerId]
    );
    
    if (customerCheck.rows.length === 0) {
      return res.status(404).json({ message: 'Customer not found' });
    }
    
    const result = await db.query(
      `SELECT o.*, 
              c.first_name, 
              c.last_name, 
              c.email
       FROM orders o
       JOIN customers c ON o.customer_id = c.customer_id
       WHERE o.customer_id = $1
       ORDER BY o.order_date DESC`,
      [customerId]
    );
    
    res.json(result.rows);
  } catch (err) {
    next(err);
  }
});

// POST create a new order
router.post('/', async (req, res, next) => {
  // Start a transaction
  const client = await db.pool.connect();
  
  try {
    await client.query('BEGIN');
    
    const { 
      customer_id, 
      total_amount, 
      status, 
      shipping_address, 
      shipping_city, 
      shipping_state, 
      shipping_zip_code,
      items 
    } = req.body;
    
    // Validate required fields
    if (!customer_id || !total_amount || !items || !Array.isArray(items) || items.length === 0) {
      return res.status(400).json({ 
        message: 'Customer ID, total amount, and at least one item are required' 
      });
    }
    
    // Check if customer exists
    const customerCheck = await client.query(
      'SELECT * FROM customers WHERE customer_id = $1',
      [customer_id]
    );
    
    if (customerCheck.rows.length === 0) {
      return res.status(400).json({ message: 'Invalid customer ID' });
    }
    
    // Create the order
    const orderResult = await client.query(
      `INSERT INTO orders 
       (customer_id, total_amount, status, shipping_address, shipping_city, shipping_state, shipping_zip_code) 
       VALUES ($1, $2, $3, $4, $5, $6, $7) 
       RETURNING *`,
      [
        customer_id, 
        total_amount, 
        status || 'pending', 
        shipping_address, 
        shipping_city, 
        shipping_state, 
        shipping_zip_code
      ]
    );
    
    const order_id = orderResult.rows[0].order_id;
    
    // Add order items
    for (const item of items) {
      // Validate item data
      if (!item.product_id || !item.quantity || !item.unit_price) {
        await client.query('ROLLBACK');
        return res.status(400).json({ 
          message: 'Each item must have product_id, quantity, and unit_price' 
        });
      }
      
      // Check if product exists and has enough stock
      const productCheck = await client.query(
        'SELECT * FROM products WHERE product_id = $1',
        [item.product_id]
      );
      
      if (productCheck.rows.length === 0) {
        await client.query('ROLLBACK');
        return res.status(400).json({ 
          message: `Product with ID ${item.product_id} not found` 
        });
      }
      
      const product = productCheck.rows[0];
      
      if (product.stock_quantity < item.quantity) {
        await client.query('ROLLBACK');
        return res.status(400).json({ 
          message: `Not enough stock for product ${product.product_name}` 
        });
      }
      
      // Calculate subtotal
      const subtotal = item.quantity * item.unit_price;
      
      // Add order item
      await client.query(
        `INSERT INTO order_items 
         (order_id, product_id, quantity, unit_price, subtotal) 
         VALUES ($1, $2, $3, $4, $5)`,
        [order_id, item.product_id, item.quantity, item.unit_price, subtotal]
      );
      
      // Update product stock
      await client.query(
        `UPDATE products 
         SET stock_quantity = stock_quantity - $1 
         WHERE product_id = $2`,
        [item.quantity, item.product_id]
      );
    }
    
    await client.query('COMMIT');
    
    // Get the complete order with items
    const completeOrderResult = await client.query(
      `SELECT o.*, 
              c.first_name, 
              c.last_name, 
              c.email
       FROM orders o
       JOIN customers c ON o.customer_id = c.customer_id
       WHERE o.order_id = $1`,
      [order_id]
    );
    
    const itemsResult = await client.query(
      `SELECT oi.*, 
              p.product_name
       FROM order_items oi
       JOIN products p ON oi.product_id = p.product_id
       WHERE oi.order_id = $1`,
      [order_id]
    );
    
    const completeOrder = completeOrderResult.rows[0];
    completeOrder.items = itemsResult.rows;
    
    res.status(201).json(completeOrder);
  } catch (err) {
    await client.query('ROLLBACK');
    next(err);
  } finally {
    client.release();
  }
});

// PUT update an order status
router.put('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    const { status } = req.body;
    
    // Validate status
    if (!status) {
      return res.status(400).json({ message: 'Status is required' });
    }
    
    // Check if order exists
    const checkResult = await db.query(
      'SELECT * FROM orders WHERE order_id = $1',
      [id]
    );
    
    if (checkResult.rows.length === 0) {
      return res.status(404).json({ message: 'Order not found' });
    }
    
    // Update order status
    const result = await db.query(
      `UPDATE orders 
       SET status = $1
       WHERE order_id = $2
       RETURNING *`,
      [status, id]
    );
    
    res.json(result.rows[0]);
  } catch (err) {
    next(err);
  }
});

// DELETE an order
router.delete('/:id', async (req, res, next) => {
  // Start a transaction
  const client = await db.pool.connect();
  
  try {
    await client.query('BEGIN');
    
    const { id } = req.params;
    
    // Check if order exists
    const checkResult = await client.query(
      'SELECT * FROM orders WHERE order_id = $1',
      [id]
    );
    
    if (checkResult.rows.length === 0) {
      return res.status(404).json({ message: 'Order not found' });
    }
    
    // Get order items to restore product stock
    const itemsResult = await client.query(
      'SELECT * FROM order_items WHERE order_id = $1',
      [id]
    );
    
    // Restore product stock
    for (const item of itemsResult.rows) {
      await client.query(
        `UPDATE products 
         SET stock_quantity = stock_quantity + $1 
         WHERE product_id = $2`,
        [item.quantity, item.product_id]
      );
    }
    
    // Delete order items
    await client.query('DELETE FROM order_items WHERE order_id = $1', [id]);
    
    // Delete order
    await client.query('DELETE FROM orders WHERE order_id = $1', [id]);
    
    await client.query('COMMIT');
    
    res.json({ message: 'Order deleted successfully' });
  } catch (err) {
    await client.query('ROLLBACK');
    next(err);
  } finally {
    client.release();
  }
});

module.exports = router;