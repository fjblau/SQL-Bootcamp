// Product routes
const express = require('express');
const router = express.Router();
const db = require('../db');

// GET all products
router.get('/', async (req, res, next) => {
  try {
    const result = await db.query(
      `SELECT p.*, c.category_name 
       FROM products p
       JOIN categories c ON p.category_id = c.category_id
       ORDER BY p.product_name`
    );
    res.json(result.rows);
  } catch (err) {
    next(err);
  }
});

// GET a specific product by ID
router.get('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    const result = await db.query(
      `SELECT p.*, c.category_name 
       FROM products p
       JOIN categories c ON p.category_id = c.category_id
       WHERE p.product_id = $1`,
      [id]
    );
    
    if (result.rows.length === 0) {
      return res.status(404).json({ message: 'Product not found' });
    }
    
    res.json(result.rows[0]);
  } catch (err) {
    next(err);
  }
});

// GET products by category
router.get('/category/:categoryId', async (req, res, next) => {
  try {
    const { categoryId } = req.params;
    const result = await db.query(
      `SELECT p.*, c.category_name 
       FROM products p
       JOIN categories c ON p.category_id = c.category_id
       WHERE p.category_id = $1
       ORDER BY p.product_name`,
      [categoryId]
    );
    
    res.json(result.rows);
  } catch (err) {
    next(err);
  }
});

// POST create a new product
router.post('/', async (req, res, next) => {
  try {
    const { 
      product_name, 
      category_id, 
      description, 
      price, 
      stock_quantity 
    } = req.body;
    
    // Validate required fields
    if (!product_name || !category_id || !price) {
      return res.status(400).json({ 
        message: 'Product name, category ID, and price are required' 
      });
    }
    
    // Validate price and stock quantity
    if (isNaN(price) || price <= 0) {
      return res.status(400).json({ message: 'Price must be a positive number' });
    }
    
    if (stock_quantity && (isNaN(stock_quantity) || stock_quantity < 0)) {
      return res.status(400).json({ message: 'Stock quantity must be a non-negative number' });
    }
    
    const result = await db.query(
      `INSERT INTO products 
       (product_name, category_id, description, price, stock_quantity) 
       VALUES ($1, $2, $3, $4, $5) 
       RETURNING *`,
      [product_name, category_id, description, price, stock_quantity || 0]
    );
    
    // Get the category name for the response
    const categoryResult = await db.query(
      'SELECT category_name FROM categories WHERE category_id = $1',
      [category_id]
    );
    
    const product = result.rows[0];
    product.category_name = categoryResult.rows[0]?.category_name;
    
    res.status(201).json(product);
  } catch (err) {
    // Check for foreign key violation
    if (err.code === '23503') {
      return res.status(400).json({ message: 'Invalid category ID' });
    }
    next(err);
  }
});

// PUT update a product
router.put('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    const { 
      product_name, 
      category_id, 
      description, 
      price, 
      stock_quantity 
    } = req.body;
    
    // Check if product exists
    const checkResult = await db.query(
      'SELECT * FROM products WHERE product_id = $1',
      [id]
    );
    
    if (checkResult.rows.length === 0) {
      return res.status(404).json({ message: 'Product not found' });
    }
    
    // Validate price and stock quantity if provided
    if (price !== undefined && (isNaN(price) || price <= 0)) {
      return res.status(400).json({ message: 'Price must be a positive number' });
    }
    
    if (stock_quantity !== undefined && (isNaN(stock_quantity) || stock_quantity < 0)) {
      return res.status(400).json({ message: 'Stock quantity must be a non-negative number' });
    }
    
    // Get current product data
    const currentProduct = checkResult.rows[0];
    
    const result = await db.query(
      `UPDATE products 
       SET product_name = $1, 
           category_id = $2, 
           description = $3, 
           price = $4, 
           stock_quantity = $5
       WHERE product_id = $6
       RETURNING *`,
      [
        product_name || currentProduct.product_name,
        category_id || currentProduct.category_id,
        description !== undefined ? description : currentProduct.description,
        price || currentProduct.price,
        stock_quantity !== undefined ? stock_quantity : currentProduct.stock_quantity,
        id
      ]
    );
    
    // Get the category name for the response
    const categoryResult = await db.query(
      'SELECT category_name FROM categories WHERE category_id = $1',
      [result.rows[0].category_id]
    );
    
    const product = result.rows[0];
    product.category_name = categoryResult.rows[0]?.category_name;
    
    res.json(product);
  } catch (err) {
    // Check for foreign key violation
    if (err.code === '23503') {
      return res.status(400).json({ message: 'Invalid category ID' });
    }
    next(err);
  }
});

// DELETE a product
router.delete('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    
    // Check if product exists
    const checkResult = await db.query(
      'SELECT * FROM products WHERE product_id = $1',
      [id]
    );
    
    if (checkResult.rows.length === 0) {
      return res.status(404).json({ message: 'Product not found' });
    }
    
    // Check if product is in any order
    const orderCheck = await db.query(
      'SELECT * FROM order_items WHERE product_id = $1 LIMIT 1',
      [id]
    );
    
    if (orderCheck.rows.length > 0) {
      return res.status(400).json({ 
        message: 'Cannot delete product that exists in orders' 
      });
    }
    
    await db.query('DELETE FROM products WHERE product_id = $1', [id]);
    
    res.json({ message: 'Product deleted successfully' });
  } catch (err) {
    next(err);
  }
});

module.exports = router;