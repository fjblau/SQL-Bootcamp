// Customer routes
const express = require('express');
const router = express.Router();
const db = require('../db');

// GET all customers
router.get('/', async (req, res, next) => {
  try {
    const result = await db.query(
      'SELECT * FROM customers ORDER BY last_name, first_name'
    );
    res.json(result.rows);
  } catch (err) {
    next(err);
  }
});

// GET a specific customer by ID
router.get('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    const result = await db.query(
      'SELECT * FROM customers WHERE customer_id = $1',
      [id]
    );
    
    if (result.rows.length === 0) {
      return res.status(404).json({ message: 'Customer not found' });
    }
    
    res.json(result.rows[0]);
  } catch (err) {
    next(err);
  }
});

// POST create a new customer
router.post('/', async (req, res, next) => {
  try {
    const { 
      first_name, 
      last_name, 
      email, 
      phone, 
      address, 
      city, 
      state, 
      zip_code 
    } = req.body;
    
    // Validate required fields
    if (!first_name || !last_name || !email) {
      return res.status(400).json({ 
        message: 'First name, last name, and email are required' 
      });
    }
    
    const result = await db.query(
      `INSERT INTO customers 
       (first_name, last_name, email, phone, address, city, state, zip_code) 
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8) 
       RETURNING *`,
      [first_name, last_name, email, phone, address, city, state, zip_code]
    );
    
    res.status(201).json(result.rows[0]);
  } catch (err) {
    // Check for duplicate email error
    if (err.code === '23505') {
      return res.status(400).json({ message: 'Email already exists' });
    }
    next(err);
  }
});

// PUT update a customer
router.put('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    const { 
      first_name, 
      last_name, 
      email, 
      phone, 
      address, 
      city, 
      state, 
      zip_code 
    } = req.body;
    
    // Check if customer exists
    const checkResult = await db.query(
      'SELECT * FROM customers WHERE customer_id = $1',
      [id]
    );
    
    if (checkResult.rows.length === 0) {
      return res.status(404).json({ message: 'Customer not found' });
    }
    
    const result = await db.query(
      `UPDATE customers 
       SET first_name = $1, last_name = $2, email = $3, 
           phone = $4, address = $5, city = $6, 
           state = $7, zip_code = $8
       WHERE customer_id = $9
       RETURNING *`,
      [first_name, last_name, email, phone, address, city, state, zip_code, id]
    );
    
    res.json(result.rows[0]);
  } catch (err) {
    // Check for duplicate email error
    if (err.code === '23505') {
      return res.status(400).json({ message: 'Email already exists' });
    }
    next(err);
  }
});

// DELETE a customer
router.delete('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    
    // Check if customer exists
    const checkResult = await db.query(
      'SELECT * FROM customers WHERE customer_id = $1',
      [id]
    );
    
    if (checkResult.rows.length === 0) {
      return res.status(404).json({ message: 'Customer not found' });
    }
    
    // Check if customer has orders
    const orderCheck = await db.query(
      'SELECT * FROM orders WHERE customer_id = $1 LIMIT 1',
      [id]
    );
    
    if (orderCheck.rows.length > 0) {
      return res.status(400).json({ 
        message: 'Cannot delete customer with existing orders' 
      });
    }
    
    await db.query('DELETE FROM customers WHERE customer_id = $1', [id]);
    
    res.json({ message: 'Customer deleted successfully' });
  } catch (err) {
    next(err);
  }
});

module.exports = router;