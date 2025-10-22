# SQL Bootcamp: Day 3 Teacher's Guide
## Advanced Topics and Practical Application

---

## Table of Contents
1. [Overview & Learning Objectives](#overview--learning-objectives)
2. [Pre-Class Setup & Requirements](#pre-class-setup--requirements)
3. [Daily Schedule & Pacing Guide](#daily-schedule--pacing-guide)
4. [Morning Session: Advanced JOINs & Subqueries (9:00 AM - 12:00 PM)](#morning-session-advanced-joins--subqueries)
5. [Afternoon Session: Security & REST API (1:00 PM - 4:30 PM)](#afternoon-session-security--rest-api)
6. [REST API Project Implementation](#rest-api-project-implementation)
7. [Assignments & Exercises](#assignments--exercises)
8. [Teaching Tips & Common Pitfalls](#teaching-tips--common-pitfalls)
9. [Troubleshooting Guide](#troubleshooting-guide)
10. [Assessment & Completion Checklist](#assessment--completion-checklist)
11. [Resources & Further Learning](#resources--further-learning)

---

## Overview & Learning Objectives

### Course Context
Day 3 is the capstone. Students have learned database foundations (Day 1) and query fundamentals (Day 2). Now they tackle advanced techniques and see how everything connects in a real application. By the end of Day 3, they'll have:
- Written complex multi-table queries
- Understood database security principles
- Built and tested a REST API connecting to PostgreSQL
- Completed a comprehensive 3-day bootcamp

This day bridges SQL theory and real-world application development.

### Primary Learning Objectives

By the end of Day 3, students will be able to:

1. **Write complex JOINs** (INNER, LEFT, RIGHT, FULL, CROSS) to combine data from multiple tables
2. **Create self-joins** to compare rows within the same table
3. **Use subqueries** in SELECT, FROM, and WHERE clauses
4. **Create and use Common Table Expressions (CTEs)** for readable complex queries
5. **Understand database security** concepts (roles, permissions, schemas)
6. **Implement basic role management** in PostgreSQL
7. **Build a REST API** that connects to PostgreSQL
8. **Implement CRUD operations** (Create, Read, Update, Delete) via HTTP
9. **Understand API error handling** and validation
10. **Apply all bootcamp knowledge** to build a complete application

### Bloom's Taxonomy Alignment
- **Remember**: JOIN types, CTE syntax, API concepts
- **Understand**: When to use each JOIN type, why CTEs improve readability, security principles
- **Apply**: Writing complex queries, building API endpoints, managing database access
- **Analyze**: Optimizing queries, choosing between JOINS and subqueries, API design
- **Evaluate**: Query performance, security implications of role design, API robustness

---

## Pre-Class Setup & Requirements

### Instructor Preparation (Complete Before Day 3)

**Software & Configuration:**
- PostgreSQL running with populated sample database
- pgAdmin accessible
- All `advanced_joins.sql`, `subqueries_ctes.sql`, `database_security.sql` tested
- **For REST API Project:**
  - If JavaScript: Node.js (v14+), npm installed on demo machine
  - If Python: Python 3.8+, pip installed on demo machine
  - API project files reviewed and tested
  - Port 3000 (or alternative) available and not blocked
  - `.env` configuration templates ready

**Pre-Session Checklist (Morning Of):**
- [ ] PostgreSQL service running
- [ ] Sample database fully populated (all tables with data)
- [ ] pgAdmin accessible
- [ ] Test all complex JOIN queries execute without error
- [ ] Test CTE examples run successfully
- [ ] Verify API project installs dependencies without error
- [ ] Start API server; test with cURL or Postman
- [ ] Display ready for showing complex queries and API testing
- [ ] Have Postman or cURL examples prepared

**Optional but Recommended:**
- Backup copy of database (in case someone deletes data)
- Screenshot/PDF of API endpoints for reference
- Pre-recorded demo of API working (backup if live demo fails)

### Student Prerequisites from Days 1-2

Students should arrive with:
- Working PostgreSQL installation and sample database
- Understanding of SELECT, WHERE, ORDER BY, GROUP BY, aggregate functions
- Experience with INSERT, UPDATE, DELETE
- Comfort with pgAdmin interface
- Understanding of primary keys and foreign keys
- Knowledge of transactions

### Classroom Setup

**Room Configuration:**
- Projector displaying complex queries clearly
- Ability to show API responses (terminal/browser)
- Students able to view and code simultaneously
- Internet access for API testing

**Materials Needed:**
- All Day 3 SQL files accessible
- REST API project files (both JavaScript and Python versions available)
- Postman or cURL documentation
- API endpoint reference sheet
- Backup database in case of data loss

---

## Daily Schedule & Pacing Guide

### Overall Day Structure

```
9:00 AM - 9:15 AM      Welcome & Day 3 Overview (15 min)
9:15 AM - 10:30 AM     Advanced JOINs Deep Dive (75 min)
10:30 AM - 10:45 AM    BREAK (15 min)
10:45 AM - 12:00 PM    Subqueries & CTEs (75 min)

12:00 PM - 1:00 PM     LUNCH

1:00 PM - 1:15 PM      Afternoon Overview & Security Intro (15 min)
1:15 PM - 2:00 PM      Database Security & Roles (45 min)
2:00 PM - 2:15 PM      BREAK (15 min)
2:15 PM - 4:00 PM      REST API Project (105 min)
4:00 PM - 4:15 PM      API Testing & Troubleshooting (15 min)
4:15 PM - 4:30 PM      Course Wrap-Up & Celebration (15 min)
```

**Total Instruction Time**: 6.5 hours  
**Total Active Learning Time**: 5 hours

### Flexibility Notes

- **Complex JOINs take time**: Allow 15% buffer; they're genuinely difficult
- **CTEs are optional if tight on time**: Core is JOINS; CTEs are "nice to have"
- **Security section can be abbreviated**: Core concepts > full implementation
- **API project flexibility**: Choose between JavaScript and Python based on class preference
- **If running behind**: Skip some security details; focus on API project (more tangible)
- **If running ahead**: Add more complex JOIN scenarios, explore API testing in detail

---

## Morning Session: Advanced JOINs & Subqueries

### 9:00 AM - 9:15 AM: Welcome & Day 3 Overview (15 minutes)

**Instructor Delivery**: Presentation + Motivation + Energy

**Content**:
- Warm welcome: "Last day! You're almost SQL bootcamp graduates!"
- Recap Days 1-2: "You learned databases, queries, data manipulation"
- What today brings: "Advanced queries, database security, and building a real REST API"
- Why it matters: "By 4:30 PM, you'll have built something you can show employers"
- Daily flow:
  - Morning: Mastering JOINs and advanced query techniques
  - Afternoon: Security principles + REST API (real code you wrote!)
  - Ending: Course celebration and next steps

**Energy & Confidence Building**:
- "You've come so far. This is where it gets satisfying."
- "Today's REST API? That's a real project you can put on your resume."
- "Let's bring this home strong. Questions? Let's tackle them."

---

### 9:15 AM - 10:30 AM: Advanced JOINs Deep Dive (75 minutes)

**Objective**: Students master all JOIN types and can write multi-table queries to solve complex business problems.

**Delivery Method**: Demonstration + Visualization + Pair Programming + Hands-On Practice

**Content Structure:**

**PART 1: Review & INNER JOIN (15 minutes)**

**Quick Recap** (3 min):
"Day 2 you saw this:"
```sql
SELECT c.category_name, COUNT(p.product_id) AS product_count
FROM products p
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name;
```

"That JOIN combined two tables: products and categories. Only products with matching categories appeared. That's an INNER JOIN (the most common)."

**INNER JOIN Visualization** (5 min):

Draw on board:
```
CUSTOMERS                    ORDERS
ID | Name                    ID | Customer_ID | Amount
1  | John     ────────────→  1  | 1          | 100
2  | Jane     ────────────→  2  | 1          | 200
3  | Bob      ───────────X    3  | 2          | 150
                        ↓
Results: Only customers with orders (1, 2)
```

"INNER JOIN shows only matching records. Customers with no orders don't appear."

**INNER JOIN Examples** (7 min):

```sql
SELECT 
    o.order_id,
    c.first_name,
    c.last_name,
    o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date DESC;
```

"This shows all orders WITH customer names. No orphaned orders."

**Teaching Point**: "INNER JOIN is your default. 90% of queries use INNER JOIN. Master this first."

---

**PART 2: LEFT JOIN (15 minutes)**

**Problem**: "I want to see ALL customers, including those who never ordered."

**Solution**: LEFT JOIN

**Visualization** (5 min):

```
CUSTOMERS                    ORDERS
ID | Name                    ID | Customer_ID | Amount
1  | John     ────────────→  1  | 1          | 100
2  | Jane     ────────────→  2  | 1          | 200
3  | Bob      ───────────X    3  | 2          | 150
                        ↓
Results: ALL customers (1, 2, 3)
Bob's order columns are NULL
```

"LEFT JOIN keeps all rows from the LEFT table, even if no match on right."

**Code Example** (7 min):

```sql
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS order_count,
    COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC;
```

"Results: ALL customers, even those with 0 orders. COALESCE handles NULL (converts to 0)."

**Teaching Point**: "LEFT JOIN is common for 'comprehensive reports' that show all records in one table."

---

**PART 3: RIGHT JOIN and FULL OUTER JOIN (15 minutes)**

**RIGHT JOIN** (5 min):

"RIGHT JOIN is opposite of LEFT JOIN: keeps all rows from RIGHT table."

```sql
SELECT 
    p.product_id,
    p.product_name,
    COUNT(oi.order_id) AS times_ordered
FROM order_items oi
RIGHT JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY times_ordered DESC;
```

"Shows all products, even those never ordered."

**Teaching Note**: "RIGHT JOIN is rare. Most developers prefer LEFT JOIN by rearranging tables. But know it exists."

**FULL OUTER JOIN** (5 min):

"Combines LEFT + RIGHT: all rows from both tables."

```sql
SELECT 
    c.customer_id,
    c.first_name,
    o.order_id,
    o.total_amount
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id;
```

"Results: ALL customers AND all orders, even mismatches. Some rows have NULL customer info, some NULL order info."

**Teaching Point**: "FULL OUTER JOIN is less common but powerful for data reconciliation."

---

**PART 4: CROSS JOIN & Multiple JOINs (15 minutes)**

**CROSS JOIN** (5 min):

"Creates Cartesian product: every row from table A matched with every row from table B."

```sql
SELECT 
    p.product_name,
    c.category_name
FROM products p
CROSS JOIN categories c
LIMIT 20;  -- Result would be huge! Always LIMIT with CROSS JOIN
```

"If 10 products × 5 categories = 50 rows. Use rarely; mostly for testing."

**Multiple JOINs** (10 min):

The real power of JOINs: combining 3+ tables.

```sql
SELECT 
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    p.product_name,
    cat.category_name,
    oi.quantity,
    oi.unit_price
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
INNER JOIN categories cat ON p.category_id = cat.category_id
ORDER BY o.order_date DESC, o.order_id;
```

Walk through:
- Start: orders table (one per order)
- JOIN customers: Add customer names
- JOIN order_items: Add products ordered
- JOIN products: Add product details
- JOIN categories: Add category info
- Result: ONE row per item ordered, with all related info

**Teaching Point**: "This single query answers: 'Show me all orders with customer names, product details, and categories, ordered by date.' Powerful!"

**Show on Projector**: Execute this query. Show rich result set. Students see the power!

---

**PART 5: Self-Join Example (10 minutes)**

"Comparing rows within the same table."

```sql
-- Employee-manager relationships (from Day 1 temporary table concept)
SELECT 
    e.employee_id,
    e.first_name || ' ' || e.last_name AS employee,
    m.first_name || ' ' || m.last_name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id
ORDER BY e.employee_id;
```

"Same table (employees) joined twice: once for employee, once for manager."

---

**PART 6: Guided Complex Query Exercise (15 minutes)**

**Scenario**: "E-commerce manager wants a report: For each order, show:
- Order ID and date
- Customer name
- All products in that order (with quantities)
- Category of each product
- Unit price and subtotal
- Show most recent orders first"

**Expected Query**:
```sql
SELECT 
    o.order_id,
    o.order_date,
    c.first_name || ' ' || c.last_name AS customer_name,
    p.product_name,
    cat.category_name,
    oi.quantity,
    oi.unit_price,
    oi.subtotal
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
INNER JOIN categories cat ON p.category_id = cat.category_id
ORDER BY o.order_date DESC, o.order_id;
```

**Students Work** (10 min): In pairs, write this query. Provide hints as needed.

**Debrief** (5 min): 
- "How many JOINs did you need?" → 4
- "Why?" → To connect orders → customers, order_items, products, and categories
- "What if I want only orders from last month?" → Add WHERE with date condition
- "What if one customer has 5 items? How many rows?" → 5 rows (one per item)

---

### 10:30 AM - 10:45 AM: BREAK (15 minutes)

---

### 10:45 AM - 12:00 PM: Subqueries & CTEs (75 minutes)

**Objective**: Students understand subqueries and CTEs as alternative (sometimes better) ways to write complex queries.

**Delivery Method**: Demonstration + Comparison + Practice

**Content:**

**PART 1: Subqueries - The Concept (15 minutes)**

**What is a Subquery?** (5 min):

"A query INSIDE another query. Like a helper query."

Example:
```sql
-- First, find average price
SELECT AVG(price) FROM products;  -- Returns 247.48

-- Then, find products above average
SELECT * FROM products WHERE price > 247.48;

-- As a subquery (combining both):
SELECT * FROM products 
WHERE price > (SELECT AVG(price) FROM products);
```

"The subquery calculates average price. The outer query uses that value to filter."

**Subqueries in Different Positions** (10 min):

**1. Subquery in WHERE** (5 min) - Most common:
```sql
SELECT customer_id, first_name, last_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id FROM orders WHERE total_amount > 500
);
```

"Find customers who placed large orders (> $500). Inner query finds customer IDs with large orders. Outer query shows those customers."

**2. Subquery in SELECT** (5 min):
```sql
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    (SELECT COUNT(*) FROM orders WHERE customer_id = c.customer_id) AS order_count
FROM customers c;
```

"For each customer, count their orders. Subquery runs for EACH customer (correlated subquery)."

**3. Subquery in FROM**:
```sql
SELECT 
    customer_summary.first_name,
    customer_summary.order_count
FROM (
    SELECT customer_id, first_name, COUNT(*) AS order_count
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY customer_id, first_name
) AS customer_summary
WHERE order_count > 2;
```

"Subquery creates a temporary result set (like a table), outer query filters it."

---

**PART 2: JOINs vs. Subqueries (10 minutes)**

**When to use what?**

**Example 1**: Find customers with orders over $500

**Using JOIN**:
```sql
SELECT DISTINCT c.customer_id, c.first_name, c.last_name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total_amount > 500;
```

**Using Subquery**:
```sql
SELECT customer_id, first_name, last_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id FROM orders WHERE total_amount > 500
);
```

**Discussion**: Both work. Subquery may be clearer (reads: "Find customers whose IDs are in this list"). JOIN is sometimes faster (execution difference minimal for small datasets).

**General Rule**:
- **Subquery**: "I'm filtering one table based on results from another"
- **JOIN**: "I'm combining data from multiple tables"

Most developers prefer **JOINs** for clarity and performance, especially in production.

---

**PART 3: Common Table Expressions (CTEs) (20 minutes)**

**What is a CTE?**

"A named subquery that makes complex queries more readable. Like creating a temporary named result set."

**Syntax**:
```sql
WITH cte_name AS (
    SELECT ... FROM ... WHERE ...
)
SELECT ... FROM cte_name WHERE ...;
```

**Simple Example** (5 min):

```sql
WITH high_value_orders AS (
    SELECT customer_id, order_id, total_amount
    FROM orders
    WHERE total_amount > 300
)
SELECT 
    c.first_name,
    c.last_name,
    COUNT(hvo.order_id) AS high_value_order_count
FROM customers c
JOIN high_value_orders hvo ON c.customer_id = hvo.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;
```

Walk through:
- CTE named "high_value_orders" finds orders over $300
- Main query joins customers with CTE
- Shows how many high-value orders each customer has

**Benefit**: "Much more readable than nested subqueries. You name each step."

**Multiple CTEs** (10 min):

```sql
WITH high_value_orders AS (
    SELECT customer_id, SUM(total_amount) AS total_spent
    FROM orders
    WHERE total_amount > 300
    GROUP BY customer_id
),
loyal_customers AS (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3  -- 3+ orders
)
SELECT 
    c.first_name,
    c.last_name,
    hvo.total_spent,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN high_value_orders hvo ON c.customer_id = hvo.customer_id
JOIN loyal_customers lc ON c.customer_id = lc.customer_id
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, hvo.total_spent;
```

"Build complexity step-by-step with named CTEs. Easier to understand and debug."

**Teaching Point**: "CTEs don't change performance vs. subqueries, but they dramatically improve readability for complex queries."

---

**PART 4: Practical Complex Query Exercise (30 minutes)**

**Scenario**: "For each product category, find:
- Category name
- Total products in category
- Products sold (items ordered, summed)
- Total revenue
- Average price
But only show categories with revenue > $500"

**Approach**:
- Using CTEs makes this much clearer

```sql
WITH category_stats AS (
    SELECT 
        cat.category_id,
        cat.category_name,
        COUNT(DISTINCT p.product_id) AS product_count,
        COALESCE(SUM(oi.quantity), 0) AS total_units_sold,
        COALESCE(SUM(oi.subtotal), 0) AS total_revenue,
        ROUND(AVG(p.price), 2) AS avg_price
    FROM categories cat
    LEFT JOIN products p ON cat.category_id = p.category_id
    LEFT JOIN order_items oi ON p.product_id = oi.product_id
    GROUP BY cat.category_id, cat.category_name
)
SELECT *
FROM category_stats
WHERE total_revenue > 500
ORDER BY total_revenue DESC;
```

**Students Work** (20 min):
1. First, just write the category_stats CTE (without WHERE)
2. Verify results make sense
3. Then add WHERE filter
4. Test and compare with neighbors

**Debrief** (10 min):
- "Does your revenue calculation look right?"
- "Why use LEFT JOIN?" → Include categories with no sales
- "What if revenue filtering was at CTE level vs. main query?" → Both work; WHERE in main query is clearer
- Celebrate: "You just wrote production-level SQL!"

---

## Afternoon Session: Security & REST API

### 1:00 PM - 1:15 PM: Afternoon Overview & Security Intro (15 minutes)

**Content**:
- Welcome back post-lunch
- Afternoon agenda: "Database security (who accesses what) and then building a REST API (real application code)"
- Why it matters: "In any job, you'll encounter security policies and APIs. These are real job skills."
- Plan: "Security concepts this hour, then hands-on API building for the rest of the afternoon"

**Energy Management**: "You're in the home stretch! One last push for a strong finish."

---

### 1:15 PM - 2:00 PM: Database Security & Roles (45 minutes)

**Objective**: Students understand PostgreSQL security model and can create roles with appropriate permissions.

**Delivery Method**: Presentation + Live Demonstration + Guided Practice

**Content:**

**PART 1: Security Concepts (15 minutes)**

**Why Database Security?**

Scenarios:
- "Your app has an admin user and regular users. Should both have same database access?" → No
- "A read-only analyst shouldn't be able to DELETE data" → Restrict permissions
- "A customer service rep should only see customer info, not pricing" → Row-level control
- "Production databases have secrets (passwords); must protect" → Security policies

**Three Levels of Database Security** (10 min):

1. **Authentication**: "Who are you?" (Username/password)
2. **Authorization**: "What can you do?" (Which tables/operations allowed)
3. **Row-Level Security**: "What data can you see?" (Filter rows by rules)

In Day 3, focus on 1 & 2 (3 is advanced).

**Roles and Permissions** (5 min):

- **Role**: A user or group with specific permissions
- **Permissions**: What a role can do (SELECT, INSERT, UPDATE, DELETE on tables/schemas)
- **Principle**: Give minimum permissions needed (least privilege)

---

**PART 2: Creating Roles (15 minutes)**

**Live Demo**:

```sql
-- Create roles
CREATE ROLE ecommerce_admin WITH LOGIN PASSWORD 'admin123';
CREATE ROLE ecommerce_analyst WITH LOGIN PASSWORD 'analyst123';
CREATE ROLE ecommerce_app WITH LOGIN PASSWORD 'app123';
```

Explain:
- `LOGIN`: Can log in to database
- `PASSWORD`: Their password
- Different passwords for different users (security best practice)

**Grant Permissions**:

```sql
-- Admin can do everything
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ecommerce_admin;

-- Analyst can only read
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ecommerce_analyst;

-- App role can read and write (but not delete)
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO ecommerce_app;
```

**Teaching Points**:
- Admin: Full access (creates/modifies tables, deletes data)
- Analyst: Read-only (reports, analysis)
- App: Specific permissions (INSERT/UPDATE for normal operations, no DELETE)

---

**PART 3: Testing Roles (10 minutes)**

**How to verify permissions** (in psql or pgAdmin):

1. Connect as different role:
```bash
psql -U ecommerce_analyst -d bootcamp_db
```

2. Try operations:
```sql
SELECT * FROM customers;  -- Should work (analyst has SELECT)
INSERT INTO customers (...) VALUES (...);  -- Should fail (analyst no INSERT)
```

3. See what fails (expected behavior)

**Have students do this** (pair with instructor on demo machine):
- Connect as analyst
- Show SELECT works
- Show INSERT fails with permission denied error
- Explain: "This is how permissions protect data in production"

---

### 2:00 PM - 2:15 PM: BREAK (15 minutes)

---

### 2:15 PM - 4:00 PM: REST API Project (105 minutes)

**Objective**: Students build and test a functioning REST API that connects to PostgreSQL.

**Delivery Method**: Guided Workshop + Live Coding + Hands-On Practice

**Content:** (Choice of JavaScript or Python; instructors choose based on class)

**PART 1: REST API Concepts (15 minutes)**

**What is a REST API?**

"API = Application Programming Interface. Way one program talks to another."

Example:
- **Old way**: Customer fills form on website → Sends to server → Server modifies database → Returns HTML page
- **Modern way (API)**: App sends JSON request (e.g., "Create customer John") → Server processes → Returns JSON response (e.g., "Success, customer ID 42")

**HTTP Methods** (5 min):

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Read data | "Get all customers" |
| POST | Create data | "Create new customer" |
| PUT | Update data | "Update customer #5" |
| DELETE | Remove data | "Delete order #10" |

**What We're Building** (10 min):

Today's REST API will:
- Allow clients to GET, POST, PUT, DELETE customers, products, orders
- Connect to our PostgreSQL database
- Return JSON responses
- Handle errors gracefully
- Be production-like (real structure, error handling, validation)

---

**PART 2: Project Setup (15 minutes)**

**Choose One Path**: JavaScript (Express.js) or Python (Flask)

**JavaScript Setup** (if chosen):

1. **Navigate to project**:
```bash
cd Day3/rest_api_project
```

2. **Install dependencies**:
```bash
npm install
```
(Installs Express, pg library, dotenv, cors)

3. **Configure database connection**:
```bash
cp .env.example .env
# Edit .env with database credentials
```

4. **Start server**:
```bash
npm start
```
(Should see: "Server running on port 3000")

**Python Setup** (if chosen):

1. **Navigate to project**:
```bash
cd Day3/rest_api_project/python_version
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure database**:
```bash
cp .env.example .env
# Edit .env with database credentials
```

4. **Start server**:
```bash
python server.py
```
(Should see: "Running on http://127.0.0.1:5000")

**Students Do This** (10 min): Get API running on their machine.

**Troubleshooting**:
- Port already in use? Use different port in .env
- npm install fails? Check Node.js version (need v14+)
- pip install fails? Check Python version (need 3.8+)
- Database connection fails? Verify .env has correct credentials

**Success Marker**: Server starts without errors

---

**PART 3: Understanding the API Code (20 minutes)**

**Architecture Overview** (5 min):

```
client (browser/Postman)
    ↓ HTTP request
  API Server (Express/Flask)
    ↓ executes code
  Database Module
    ↓ SQL query
  PostgreSQL
```

**Key Files** (15 min):

**JavaScript:**

`server.js` - Main application:
```javascript
const express = require('express');
const app = express();
// Register routes
app.use('/api/customers', require('./routes/customers'));
app.use('/api/products', require('./routes/products'));
app.use('/api/orders', require('./routes/orders'));
// Start server
app.listen(3000, () => console.log('Server running on port 3000'));
```

`db.js` - Database connection:
```javascript
const { Pool } = require('pg');
const pool = new Pool({ ... });
// Execute queries safely with parameterized statements
async function query(text, params) {
  return pool.query(text, params);
}
```

`routes/customers.js` - Customer endpoints:
```javascript
// GET /api/customers - Get all customers
router.get('/', async (req, res) => { ... });
// POST /api/customers - Create customer
router.post('/', async (req, res) => { ... });
// PUT /api/customers/:id - Update customer
router.put('/:id', async (req, res) => { ... });
// DELETE /api/customers/:id - Delete customer
router.delete('/:id', async (req, res) => { ... });
```

Walk through one endpoint example to show pattern.

**Python equivalent** (similar structure with Flask Blueprints).

---

**PART 4: Testing the API (30 minutes)**

**Tool: Postman or cURL** (choose one)

**cURL Command-Line Examples**:

**1. GET all customers**:
```bash
curl -X GET http://localhost:3000/api/customers
```
Response: JSON array of customers

**2. GET one customer**:
```bash
curl -X GET http://localhost:3000/api/customers/1
```
Response: Single customer object

**3. POST (create) customer**:
```bash
curl -X POST http://localhost:3000/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "first_name":"Alice",
    "last_name":"Wonder",
    "email":"alice@example.com",
    "phone":"555-1234",
    "city":"Boston",
    "state":"MA"
  }'
```
Response: Created customer object (with auto-generated ID)

**4. PUT (update) customer**:
```bash
curl -X PUT http://localhost:3000/api/customers/1 \
  -H "Content-Type: application/json" \
  -d '{"city":"Cambridge"}'
```
Response: Updated customer object

**5. DELETE customer** (carefully!):
```bash
curl -X DELETE http://localhost:3000/api/customers/999
```
Response: Success/error message

**Live Demo** (10 min): Show 3-4 of these requests on projector. Students see API respond.

**Students Test API** (15 min):
1. Run GET all customers
2. Run GET one customer
3. Create new customer (POST)
4. Verify new customer appears in GET all
5. Update customer (PUT)
6. Verify update shows in GET

Have them try in pairs. Help troubleshoot.

**Success Markers**:
- GET requests return JSON
- POST creates new records (verify with GET)
- PUT modifies records
- DELETE removes records (be careful!)
- All responses show proper status codes (200 OK, 201 Created, 400 Bad Request, 404 Not Found)

---

**PART 5: Error Handling & Validation (15 minutes)**

**Show What Happens When Things Go Wrong**:

**1. Invalid data (missing required field)**:
```bash
curl -X POST http://localhost:3000/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "first_name":"Bob"
    # Missing last_name, email, etc.
  }'
```
Response: 400 Bad Request with error message

**2. Duplicate email**:
```bash
curl -X POST http://localhost:3000/api/customers \
  -d '{
    "first_name":"John",
    "last_name":"Doe",
    "email":"john.doe@example.com"  # Already exists
  }'
```
Response: 409 Conflict or 400 Bad Request with error

**3. Resource not found**:
```bash
curl -X GET http://localhost:3000/api/customers/99999
```
Response: 404 Not Found

**4. Business logic violation** (e.g., delete customer with orders):
```bash
curl -X DELETE http://localhost:3000/api/customers/1  # Has orders
```
Response: 400 Bad Request with message explaining why

**Teaching Point**: "Good APIs don't crash. They return meaningful errors. The code handles edge cases."

**Show students the error handling code** (5 min):
- Input validation (required fields)
- Database error catching
- Meaningful error messages
- Proper HTTP status codes

"This is what production-quality code looks like."

---

**PART 6: Putting It All Together (15 minutes)**

**Comprehensive Scenario**:

"You're building an e-commerce website. Here's a user journey via the API:"

**Step 1: Get all products** (browse)
```bash
curl -X GET http://localhost:3000/api/products
```

**Step 2: Get specific product** (view details)
```bash
curl -X GET http://localhost:3000/api/products/1
```

**Step 3: Create new customer** (user signs up)
```bash
curl -X POST http://localhost:3000/api/customers -d {...}
```

**Step 4: Create order** (user places order)
```bash
curl -X POST http://localhost:3000/api/orders \
  -d '{
    "customer_id": 10,
    "items": [
      {"product_id": 1, "quantity": 2, "unit_price": 699.99},
      {"product_id": 3, "quantity": 1, "unit_price": 149.99}
    ]
  }'
```

**Step 5: Get customer's orders** (view order history)
```bash
curl -X GET http://localhost:3000/api/orders/customer/10
```

**Step 6: Update order status** (admin marks as shipped)
```bash
curl -X PUT http://localhost:3000/api/orders/5 \
  -d '{"status": "shipped"}'
```

"This is a real user journey. Every request modifies the database. You're managing a real e-commerce system via API."

**Students Execute This Scenario** (10 min):
- Pair up
- Run these commands in order
- See data flow through API

---

### 4:00 PM - 4:15 PM: API Testing & Troubleshooting (15 minutes)

**Common Issues & Solutions**:

| Issue | Cause | Solution |
|-------|-------|----------|
| "Cannot GET /api/..." | Route not found | Check endpoint URL, check server started |
| "Connection refused" | Server not running | Start API server first |
| "EADDRINUSE: address already in use" | Port 3000 in use | Kill existing process or use different port |
| Database errors | Credentials wrong | Check .env file database connection |
| CORS errors | Browser security | CORS already enabled in project |

**Have students** (5 min):
- Test their API with one GET request
- If fails, troubleshoot together
- Help anyone still having issues

**Verify Everyone Has Working API** (5 min):
- "Who got a successful response from GET /api/customers?"
- Anyone not working? Pair with someone or instructor will help
- Mark in mental notes for follow-up

**Celebrate**: "You've built a REST API connected to a PostgreSQL database. That's a real skill. Wow!"

---

### 4:15 PM - 4:30 PM: Course Wrap-Up & Celebration (15 minutes)

**Instructor Delivery**: Presentation + Reflection + Celebration + Resources

**Content:**

**Recap Entire Bootcamp** (3 minutes)

"Three days ago, you didn't know what a database was. Let's recap:"
- **Day 1**: Learned database structure, created first database
- **Day 2**: Wrote queries, manipulated data, aggregated information
- **Day 3**: Built complex queries, understood security, built a working REST API

"You're not beginners anymore. You're SQL developers."

**Key Concepts Review** (2 minutes)

"Remember these, they matter in every job:"
- Databases organize data with relationships and rules
- SQL queries extract and manipulate that data
- JOINs combine data from multiple tables
- Aggregates summarize data for insights
- APIs let applications talk to databases
- Security means granting minimum necessary permissions

**What You Can Do Now** (2 minutes)

"In a job interview or on the job, you can:"
- Design a basic database
- Write queries from simple to moderately complex
- Build a web application that talks to a database
- Handle errors and validate data
- Understand security implications of database access

"All of that is genuinely valuable. Companies hire for exactly these skills."

**Next Steps & Continued Learning** (2 minutes)

Suggest paths based on interest:
- **If you like SQL**: Learn window functions, optimization, advanced indexing
- **If you like building applications**: Learn API frameworks (Express, Flask), frontend frameworks
- **If you like data analysis**: Learn aggregation, reporting, visualization tools
- **If you like database administration**: Learn backup/recovery, replication, cloud databases

"SQL is foundation. What you build on top is up to you."

**Resources to Keep Learning** (2 minutes)

Provide links:
- PostgreSQL official docs
- Online SQL tutorials (W3Schools, SQLZoo)
- API/Web development resources
- Community (Stack Overflow, Reddit /r/learnprogramming)

**Final Words** (2 minutes)

"This bootcamp is the beginning, not the end. You've built momentum. Keep learning. Keep coding. Ask questions. Make mistakes—that's how you learn.

Thank you for being here. It's been amazing watching you go from 'What's a foreign key?' to 'I built a REST API connected to PostgreSQL.'

Congratulations, SQL Bootcamp graduates!"

**Optional: Q&A / Open Office Hours** (remaining time):
- Answer any lingering questions
- Help students with API issues or queries
- Discuss job prospects, next learning steps
- Take a class photo if desired!

---

## REST API Project Implementation

### Project Structure (Both JavaScript and Python)

**JavaScript (Express.js)**
```
rest_api_project/
├── server.js               # Main app entry point
├── db.js                   # Database connection module
├── package.json           # Dependencies
├── .env.example           # Configuration template
└── routes/
    ├── customers.js       # Customer endpoints
    ├── products.js        # Product endpoints
    └── orders.js          # Order endpoints
```

**Python (Flask)**
```
python_version/
├── server.py              # Main app entry point
├── db.py                  # Database connection module
├── requirements.txt       # Dependencies
├── .env.example          # Configuration template
└── routes/
    ├── customers.py      # Customer endpoints
    ├── products.py       # Product endpoints
    └── orders.py         # Order endpoints
```

### API Endpoints Reference

Both implementations provide identical endpoints:

**Customers**:
- `GET /api/customers` - List all
- `GET /api/customers/:id` - Get one
- `POST /api/customers` - Create
- `PUT /api/customers/:id` - Update
- `DELETE /api/customers/:id` - Delete

**Products**:
- `GET /api/products` - List all
- `GET /api/products/:id` - Get one
- `GET /api/products/category/:categoryId` - Filter by category
- `POST /api/products` - Create
- `PUT /api/products/:id` - Update
- `DELETE /api/products/:id` - Delete

**Orders**:
- `GET /api/orders` - List all
- `GET /api/orders/:id` - Get one with items
- `GET /api/orders/customer/:customerId` - Get customer's orders
- `POST /api/orders` - Create (with validation)
- `PUT /api/orders/:id` - Update status
- `DELETE /api/orders/:id` - Delete

### Security Considerations

"This is a demo project. In production, add:"
- Authentication (JWT, OAuth)
- Input validation & sanitization
- Rate limiting
- HTTPS encryption
- Proper CORS configuration
- SQL injection prevention (using parameterized queries—already done!)

---

## Assignments & Exercises

### In-Class Exercises

**Exercise 1: Complex JOIN Query** (Morning)
- Write query combining 4+ tables
- Answer specific business question
- Grading: 5 points for correct syntax, meaningful results

**Exercise 2: CTE Complex Query** (Morning)
- Write query using 2+ CTEs
- Show readability advantage
- Grading: 5 points for working query, bonus for elegance

**Exercise 3: Role Creation & Permissions** (Afternoon)
- Create 2-3 roles with different permissions
- Verify each role's access works/fails as intended
- Grading: 5 points for correct role setup

**Exercise 4: API Testing** (Afternoon)
- Execute all CRUD operations via API
- Verify data persists in database
- Test error scenarios
- Grading: 5 points for successful testing, 5 for error handling

### Take-Home / Follow-Up

**Assignment 1: Design Your Own Database**
- Choose any domain (library, gym, restaurant reservation, etc.)
- Design schema (3-5 tables with relationships)
- Create tables using SQL
- Insert sample data

**Assignment 2: Advanced Query Challenge**
- Given a business question, write the query
- Examples: "Top 5 customers by spending", "Products never ordered", "Category performance over time"
- Submit queries

**Assignment 3: Extend REST API**
- Add validation rules
- Add new endpoint
- Improve error messages
- Deploy to cloud (Heroku, Replit, etc.)

---

## Teaching Tips & Common Pitfalls

### For Complex JOINs

**Tip 1**: Draw JOIN relationships on board
- Show which tables connect
- Show which keys match
- Students visualize better

**Tip 2**: Build queries incrementally
- Start with SELECT from one table
- Add one JOIN at a time
- Verify results after each JOIN
- Easier to debug

**Tip 3**: Use table aliases consistently
- `products p`, `categories c`, `orders o`
- Shorthand improves readability
- Show why aliases matter

### For Subqueries & CTEs

**Common Misconception**: "CTEs are for advanced developers"

**Correction**: "CTEs are for readability. Any developer can write them. In fact, use them to make your code clearer."

**Tip**: Start with subquery, then convert to CTE for students to see difference.

### For REST API

**Tip 1**: Start with working API, show code gradually
- Don't live-code the entire API
- Show key patterns
- Students understand better

**Tip 2**: Use Postman UI first (easier than cURL)
- Visual; click through endpoints
- Then show cURL equivalents
- Both have value

**Tip 3**: Make mistakes intentionally
- Send invalid JSON
- Omit required field
- Show error handling in action

---

## Troubleshooting Guide

### Complex Query Issues

**Error: "column must appear in GROUP BY"**
- Cause: Selected column not aggregated/grouped
- Fix: Add column to GROUP BY or wrap in aggregate

**Error: "ambiguous column reference"**
- Cause: Same column name in multiple tables
- Fix: Use table alias (e.g., `c.name` not just `name`)

**Too many/few rows in result**
- Cause: Wrong JOIN condition or missing WHERE
- Fix: Verify JOIN ON clause, test with SELECT first

### REST API Issues

**"Cannot connect to database" error**
- Cause: .env credentials wrong or PostgreSQL not running
- Fix: Check .env, verify PostgreSQL service running

**"Cannot POST /api/customers"**
- Cause: Request body malformed or server not started
- Fix: Check JSON format, restart server

**API works but data not persisting**
- Cause: Transaction not committed or wrong database
- Fix: Verify queries are executing against correct database

---

## Assessment & Completion Checklist

### Day 3 Success Criteria

Students successfully complete Day 3 if they:

1. **✓ Advanced JOINs**
   - Write multi-table JOINs correctly
   - Understand difference between JOIN types
   - Answer complex business questions with JOINs

2. **✓ Subqueries & CTEs**
   - Write subqueries in WHERE/SELECT/FROM
   - Use CTEs to improve code readability
   - Demonstrate both approaches

3. **✓ Database Security**
   - Create roles with different permissions
   - Understand least privilege principle
   - Verify permission restrictions work

4. **✓ REST API**
   - Successfully run API server
   - Execute CRUD operations via API
   - Test error scenarios
   - Understand how API connects to database

5. **✓ Bootcamp Completion**
   - Can design basic database
   - Write queries from simple to moderately complex
   - Build application that uses database
   - Understand security principles

### Grading Rubric (if formal grading)

| Criteria | Full (5) | Partial (3) | Incomplete (1) |
|----------|----------|-----------|------------|
| **Complex JOINs** | Multi-table queries correct | Mostly correct, minor issues | Cannot write complex JOINs |
| **Subqueries/CTEs** | Correct syntax, good readability | Works with minor errors | Cannot use subqueries/CTEs |
| **Security** | Roles created correctly, permissions work | Mostly correct | Cannot create roles/permissions |
| **API** | CRUD operations work, error handling present | Mostly works, some errors | Cannot run or test API |
| **Overall Bootcamp** | Demonstrates mastery of all topics | Understands most concepts | Missing key concepts |

---

## Resources & Further Learning

### Official Documentation

- PostgreSQL Docs: https://www.postgresql.org/docs/
- Express.js Docs: https://expressjs.com/
- Flask Docs: https://flask.palletsprojects.com/
- REST API Best Practices: https://restfulapi.net/

### Online Learning Platforms

- Udemy (SQL, Node.js, Python courses)
- Coursera (Database courses)
- Codecademy (Interactive SQL tutorials)
- LeetCode (SQL interview problems)

### Communities & Support

- Stack Overflow (tagged [sql], [postgresql], [api])
- Reddit (/r/learnprogramming, /r/learnSQL)
- PostgreSQL community (forums, IRC)
- GitHub (open source projects to learn from)

### Advanced Topics to Explore

- Window functions (OVER, PARTITION BY)
- Stored procedures and triggers
- Query optimization and indexing
- Replication and backup strategies
- NoSQL databases (MongoDB, Cassandra)
- Cloud databases (AWS RDS, Azure SQL, Google Cloud SQL)

---

## Conclusion

**Day 3 Brings the Bootcamp Home:**

Students have journeyed from "What's a database?" to "I built a REST API connected to PostgreSQL." That's significant progress. They've learned:
- SQL fundamentals through advanced queries
- Database design and structure
- Real-world application development
- Security principles

**This Is Just the Beginning:**

The bootcamp is foundation, not ceiling. Encourage students to:
- Build projects using these skills
- Contribute to open source
- Interview for internships/jobs
- Keep learning (advanced SQL, other frameworks, etc.)

**Final Message to Instructors:**

Teaching databases and SQL is teaching people to think systematically about data. You're equipping them with a skill that scales across industries and decades. The effort matters. The questions matter. The mistakes matter.

Celebrate the completion. You've done great work.

---

**Document Version**: 1.0  
**Last Updated**: Day 3 Planning  
**For Use**: SQL Bootcamp Day 3 (3-Day Course)  
**Total Pages**: Approximately 39