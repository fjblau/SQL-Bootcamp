# SQL Bootcamp: Day 2 Teacher's Guide
## SQL Queries and Database Management

---

## Table of Contents
1. [Overview & Learning Objectives](#overview--learning-objectives)
2. [Pre-Class Setup & Requirements](#pre-class-setup--requirements)
3. [Daily Schedule & Pacing Guide](#daily-schedule--pacing-guide)
4. [Morning Session: pgAdmin & Basic Queries (9:00 AM - 12:00 PM)](#morning-session-pgadmin--basic-queries)
5. [Afternoon Session: Data Manipulation & Advanced Queries (1:00 PM - 4:30 PM)](#afternoon-session-data-manipulation--advanced-queries)
6. [Assignments & Exercises](#assignments--exercises)
7. [Teaching Tips & Common Pitfalls](#teaching-tips--common-pitfalls)
8. [Troubleshooting Guide](#troubleshooting-guide)
9. [Assessment & Completion Checklist](#assessment--completion-checklist)
10. [Resources & Reference Materials](#resources--reference-materials)

---

## Overview & Learning Objectives

### Course Context
Day 2 builds directly on Day 1's foundation. Students now understand database structure; today they learn to ask questions of that data. This is where SQL becomes powerful—students will write queries that transform raw data into business insights. By the end of the day, they'll have moved from "I can create tables" to "I can extract meaningful information from data."

### Primary Learning Objectives
By the end of Day 2, students will be able to:

1. **Navigate and use pgAdmin** to view databases, tables, and execute queries graphically
2. **Write SELECT queries** with column selection, filtering, and sorting
3. **Filter data effectively** using WHERE clauses with AND, OR, and comparison operators
4. **Sort and limit results** using ORDER BY and LIMIT clauses
5. **Use aggregate functions** (COUNT, SUM, AVG, MIN, MAX) to summarize data
6. **Group data** using GROUP BY and filter groups with HAVING clauses
7. **Combine data from multiple tables** using INNER JOIN (basic introduction)
8. **Manipulate data** using INSERT, UPDATE, and DELETE statements
9. **Understand transactions** and when data modifications succeed or fail
10. **Apply SQL to real-world scenarios** such as business analysis and data updates

### Bloom's Taxonomy Alignment
- **Remember**: SQL syntax, aggregate function names, clause order
- **Understand**: What WHERE does vs. HAVING, why GROUP BY exists, when to use JOINs
- **Apply**: Writing queries to answer business questions, creating data modifications
- **Analyze**: Optimizing queries, choosing between different approaches
- **Evaluate**: Assessing query correctness and efficiency

---

## Pre-Class Setup & Requirements

### Instructor Preparation (Complete Before Day 2)

**Software & Configuration:**
- PostgreSQL running with sample e-commerce database created
- pgAdmin fully installed and accessible
- `sample_database.sql` verified to execute without errors
- All Day 2 SQL scripts tested and working
- Display/projector setup tested (especially pgAdmin GUI viewing)

**Pre-Session Checklist (Morning Of):**
- [ ] PostgreSQL service running and verified
- [ ] Execute `sample_database.sql` on demo machine to populate sample data
- [ ] Open pgAdmin, verify all tables visible and have data
- [ ] Test all queries from `basic_queries.sql` and `advanced_queries.sql`
- [ ] Verify projector can display pgAdmin clearly (test zoom if needed)
- [ ] Have backup screenshots of query results in case of display issues
- [ ] Verify internet connection (for any online resources)

### Student Prerequisites from Day 1

Students should arrive with:
- Working PostgreSQL installation (verified yesterday)
- bootcamp_db database created
- Understanding of tables, rows, columns, primary/foreign keys
- Familiarity with basic DDL (CREATE TABLE)
- pgAdmin installed (or prepared to install during morning session)

### Classroom Setup

**Room Configuration:**
- Projector showing pgAdmin clearly (fonts readable, at least 14pt)
- Students able to see while typing on their machines
- Optional: Have a few extra laptops available in case of system issues

**Materials Needed:**
- Printed: `sample_database.sql` or shared via document
- Printed: SQL query templates for practice
- Digital: All Day 2 SQL files accessible to students
- Digital: Backup copy of data in case anyone needs to reset

---

## Daily Schedule & Pacing Guide

### Overall Day Structure

```
9:00 AM - 9:15 AM      Welcome Back & Day 2 Overview (15 min)
9:15 AM - 9:45 AM      pgAdmin Introduction & Setup (30 min)
9:45 AM - 11:00 AM     Basic SELECT Queries (75 min)
11:00 AM - 11:15 AM    BREAK (15 min)
11:15 AM - 12:00 PM    Filtering with WHERE (45 min)

12:00 PM - 1:00 PM     LUNCH

1:00 PM - 1:15 PM      Afternoon Recap & Introduction (15 min)
1:15 PM - 2:30 PM      Data Manipulation: INSERT, UPDATE, DELETE (75 min)
2:30 PM - 2:45 PM      BREAK (15 min)
2:45 PM - 4:00 PM      Aggregate Functions & GROUP BY (75 min)
4:00 PM - 4:15 PM      Introduction to JOINs Preview (15 min)
4:15 PM - 4:30 PM      Wrap-Up & Day 2 Checkout (15 min)
```

**Total Instruction Time**: 6.5 hours  
**Total Active Learning Time**: 5 hours

### Flexibility Notes

- **pgAdmin installation may delay morning**: If students don't have pgAdmin installed, allocate extra 15 minutes
- **Queries take time**: Allow 15% extra time for students to think and write queries
- **If running behind**: Defer JOINs completely to Day 3; ensure everyone masters SELECT, WHERE, INSERT, UPDATE, DELETE
- **If running ahead**: Expand GROUP BY examples, introduce aggregate functions in WHERE (HAVING preview)

---

## Morning Session: pgAdmin & Basic Queries

### 9:00 AM - 9:15 AM: Welcome Back & Overview (15 minutes)

**Instructor Delivery**: Presentation + Engagement

**Content**:
- Warm welcome: "Day 2! You made it! Today is where the magic happens."
- Recap Day 1: "Yesterday we learned database structure. Today we ask questions of data."
- What you'll do: "By lunch, you'll be writing queries. By 4:30 PM, you'll have an e-commerce database that responds to your questions."
- Daily themes:
  - Morning: Querying data (SELECT, WHERE, ORDER BY)
  - Afternoon: Changing data (INSERT, UPDATE, DELETE) + Aggregate functions
- Logistics: Same breaks, lunch same time, questions always encouraged
- Energy check: "How's everyone feeling? Anyone need a pep talk?" (Build confidence)

**Key Message**: "Every developer who works with data writes SELECT queries multiple times per day. This skill is instantly useful."

---

### 9:15 AM - 9:45 AM: pgAdmin Introduction & Setup (30 minutes)

**Objective**: Students can navigate pgAdmin, view databases/tables, and run queries graphically.

**Delivery Method**: Demonstration + Guided Practice

**Part 1: What is pgAdmin? (5 minutes)**

Show on screen: pgAdmin interface

Explain:
- "pgAdmin is a graphical interface to PostgreSQL"
- "Instead of typing commands in terminal, you can click and see results"
- "It's useful for: browsing databases, writing queries, managing objects"
- "Many production environments use pgAdmin; professional tool"

**Analogy**: "psql is like using command-line file system (Terminal); pgAdmin is like using Finder/Explorer—both do the same thing, different interfaces"

**Part 2: Navigating pgAdmin (10 minutes)**

Live demo on projector:

1. **Open pgAdmin**
   - Show: "pgAdmin usually starts in browser (often localhost:5050)"
   - Show: Login screen (if needed)

2. **Connect to PostgreSQL Server**
   - Servers → Right-click → Create → Server
   - OR: If already connected, expand "Servers"
   - Show existing "PostgreSQL" connection

3. **Navigate Database Structure**
   ```
   Servers
   └── PostgreSQL (your server)
       └── Databases
           └── postgres (default database)
           └── bootcamp_db (from Day 1)
   ```
   
   Expand bootcamp_db → Tables
   Show: contacts, notes tables from Day 1

4. **Run a Query**
   - Tools → Query Tool (or right-click database → Query Tool)
   - Show Query Editor window
   - Type simple query: `SELECT * FROM contacts;`
   - Press F5 or click Execute
   - Show Results pane with three contacts

5. **Load Sample Database**
   - Before students follow along, execute `sample_database.sql`:
     - File → Open File → select `sample_database.sql`
     - Execute entire script (F5)
   - Show: "Creating ecommerce database" with customers, products, orders tables
   - Verify: Browse to new tables, show they have data

**Part 3: Students Set Up pgAdmin (10 minutes)**

Have students:
1. Open pgAdmin
2. Navigate to bootcamp_db
3. Run a simple query: `SELECT COUNT(*) FROM customers;`
4. Should see: "8" (8 customers in sample data)
5. Raise hand when successful

**Support**: Circulate; help anyone stuck on pgAdmin navigation

**Visual Aids**: 
- Screenshot of pgAdmin interface with annotations
- Diagram of database navigation tree
- Sample query result showing columns and data

---

### 9:45 AM - 11:00 AM: Basic SELECT Queries (75 minutes)

**Objective**: Students write SELECT queries with column selection, aliasing, and basic calculations.

**Delivery Method**: Live Coding + Guided Practice + Hands-On Exercises

**Content Structure:**

**SECTION 1: SELECT Fundamentals (20 minutes)**

**1. SELECT all columns (5 min)**

Live demo in pgAdmin Query Tool:

```sql
SELECT * FROM customers;
```

Show results: All customers, all columns (customer_id, first_name, last_name, email, phone, address, city, state, zip_code, created_at)

Explain:
- `SELECT *` means "all columns"
- `FROM customers` means "from the customers table"
- Results show 8 rows (one per customer)
- This is useful for: "Show me everything about customers"

**2. SELECT specific columns (5 min)**

```sql
SELECT first_name, last_name, email FROM customers;
```

Show results: Only three columns (name, last_name, email)

Explain:
- More specific than `*`
- Useful for: "I only care about names and emails"
- Faster than `*` on huge tables (not much difference here, but principle matters)
- Clearer output (less clutter)

**Activity**: Have students write:
```sql
SELECT product_name, price FROM products;
```
They should see product names and prices. ✓

**3. Column aliases (5 min)**

```sql
SELECT 
    first_name AS "First Name",
    last_name AS "Last Name",
    email AS "Email Address"
FROM customers;
```

Show results: Column headers now show "First Name" instead of "first_name"

Explain:
- `AS "column alias"` renames column in output
- Useful for: Professional reports, readable output, names with spaces
- Doesn't change data, just display
- Quotes needed if alias has spaces

**Activity**: Have students write:
```sql
SELECT product_name AS "Product", price AS "Cost" FROM products LIMIT 5;
```

**4. Concatenation (5 min)**

```sql
SELECT 
    first_name || ' ' || last_name AS "Full Name",
    email
FROM customers;
```

Show results: "John Doe", "Jane Smith", etc. (combined first and last names)

Explain:
- `||` is concatenation operator (joins strings)
- Useful for: Creating full names, combining fields
- In PostgreSQL: `||` (in MySQL: `CONCAT()`, in SQL Server: `+`)

**Activity**: Have students write:
```sql
SELECT product_name || ' - $' || price AS "Product Info" FROM products LIMIT 5;
```

**SECTION 2: Calculations & Functions (15 minutes)**

**1. Math calculations (5 min)**

```sql
SELECT 
    product_name,
    price,
    stock_quantity,
    price * stock_quantity AS inventory_value
FROM products;
```

Show results: Last column shows total value of inventory for each product

Explain:
- `price * stock_quantity` calculates inventory value
- Can use +, -, *, / operators
- Useful for: Financial analysis, reporting, derived metrics

**Activity**: Have students calculate:
```sql
SELECT 
    product_name,
    price,
    price * 1.1 AS "Price with 10% markup"
FROM products
LIMIT 5;
```

**2. DISTINCT to remove duplicates (5 min)**

```sql
SELECT DISTINCT city FROM customers;
```

Show results: Unique cities (Boston, Cambridge, Somerville, Brookline, Newton, Watertown, Medford, Arlington)

Explain:
- `DISTINCT` removes duplicates
- Useful for: "What cities do we have customers in?" or "What states are our products available in?"
- Performance impact: Minimal on small tables

**Activity**: Students write:
```sql
SELECT DISTINCT state FROM customers;
```
Should see: "MA" (all sample customers from Massachusetts)

**3. ORDER BY for sorting (5 min)**

```sql
SELECT first_name, last_name, email FROM customers ORDER BY last_name;
```

Show results: Sorted alphabetically by last name

Explain:
- `ORDER BY column` sorts results
- Default: ascending (A to Z, 0 to 9)
- Can do `ORDER BY column DESC` for descending (Z to A)
- Can order by multiple columns: `ORDER BY last_name, first_name`

**Activity**: Students write:
```sql
SELECT product_name, price FROM products ORDER BY price DESC;
```
Should see: Most expensive products first

**SECTION 3: LIMIT and Hands-On Practice (10 minutes)**

**LIMIT clause (3 min)**

```sql
SELECT product_name, price FROM products LIMIT 5;
```

Show results: Only first 5 products

Explain:
- `LIMIT n` shows only first n rows
- Useful for: "Show me the top 10", pagination, testing queries on huge tables
- Can combine with ORDER BY: `ORDER BY price DESC LIMIT 5` (top 5 most expensive)

**Guided Practice Exercise (7 min)**

Project scenario: "E-commerce manager wants a report of products."

Task: Write a query to show:
- Product name and price
- Sorted by price (most expensive first)
- Show only top 10

Expected query:
```sql
SELECT product_name, price 
FROM products 
ORDER BY price DESC 
LIMIT 10;
```

Students write and execute. Verify they see results. Celebrate success!

**Debrief**: Ask:
- "Why ORDER BY DESC?" → Most expensive first
- "Why LIMIT 10?" → We only want top 10
- "What if I want cheapest first?" → ORDER BY price ASC (or just ORDER BY price)

---

### 11:00 AM - 11:15 AM: BREAK (15 minutes)

---

### 11:15 AM - 12:00 PM: Filtering with WHERE (45 minutes)

**Objective**: Students write WHERE clauses to filter data using comparison operators and logical operators.

**Delivery Method**: Live Coding + Pair Programming + Hands-On Exercises

**Content:**

**PART 1: WHERE Clause Fundamentals (15 minutes)**

**1. Simple comparison (5 min)**

```sql
SELECT product_name, price FROM products WHERE price > 100;
```

Show results: Only products over $100 (Smartphone X, Laptop Pro, Winter Jacket, etc.)

Explain:
- `WHERE condition` filters rows
- Only rows meeting condition appear
- Comparison operators: `=`, `<>` (not equal), `>`, `<`, `>=`, `<=`

**2. Text comparison (5 min)**

```sql
SELECT first_name, last_name, city FROM customers WHERE city = 'Boston';
```

Show results: Customers in Boston

Explain:
- `=` works with text too
- Text is case-sensitive (usually; depends on database configuration)
- `WHERE city = 'Boston'` finds exact match
- Note: Single quotes for text values (not double)

**Activity**: Students write:
```sql
SELECT product_name, category_id FROM products WHERE category_id = 1;
```
Should see: Electronics products (category 1)

**3. Combining conditions with AND (5 min)**

```sql
SELECT product_name, price, stock_quantity 
FROM products 
WHERE category_id = 1 AND price < 200;
```

Show results: Electronics products under $200

Explain:
- `AND` means both conditions must be true
- `WHERE condition1 AND condition2`
- Useful for: "I want products in category X AND price under Y"

**Activity**: Students write:
```sql
SELECT product_name, price 
FROM products 
WHERE category_id = 2 AND price > 30;
```
Should see: Clothing items over $30

**PART 2: Complex Filtering (15 minutes)**

**1. OR condition (5 min)**

```sql
SELECT product_name, category_id, price 
FROM products 
WHERE category_id = 1 OR category_id = 2;
```

Show results: Products in category 1 (Electronics) OR category 2 (Clothing)

Explain:
- `OR` means at least one condition must be true
- `WHERE condition1 OR condition2`
- Useful for: "I want products from multiple categories"

**2. Combining AND with OR (5 min)**

Show WITHOUT parentheses first:
```sql
WHERE category_id = 1 OR category_id = 2 AND price < 50
```

Then WITH parentheses:
```sql
WHERE (category_id = 1 OR category_id = 2) AND price < 50
```

Explain:
- Parentheses matter! They change which conditions are grouped
- Without parentheses: category 1 items OR (category 2 items under $50) — includes ALL category 1
- With parentheses: (category 1 OR category 2) items AND under $50 — more restrictive
- Always use parentheses for clarity

**Activity**: Diagram on board:
```
Query: Find products where (category 1 OR category 2) AND price < 100

Answer: Electronics or Clothing products under $100
```

**3. LIKE for pattern matching (5 min)**

```sql
SELECT product_name FROM products WHERE product_name LIKE '%Jacket%';
```

Show results: "Winter Jacket" (any product with "Jacket" in name)

Explain:
- `LIKE` matches text patterns
- `%` is wildcard (matches any characters)
- `%Jacket%` finds "Jacket" anywhere in text
- `Jacket%` finds products starting with "Jacket"
- `%Jacket` finds products ending with "Jacket"
- Useful for: "Find products with 'wireless' in the name"

**Activity**: Students write:
```sql
SELECT product_name FROM products WHERE product_name LIKE '%Laptop%';
```

**PART 3: Guided Exercises (15 minutes)**

**Exercise 1 (5 min)**: "Find all customers in Boston"

```sql
SELECT first_name, last_name, city 
FROM customers 
WHERE city = 'Boston';
```

**Exercise 2 (5 min)**: "Find products in Electronics (category 1) that cost less than $500"

```sql
SELECT product_name, price, category_id 
FROM products 
WHERE category_id = 1 AND price < 500;
```

**Exercise 3 (5 min)**: "Find products that are either very cheap (under $25) or very expensive (over $500)"

```sql
SELECT product_name, price 
FROM products 
WHERE price < 25 OR price > 500;
```

Have students attempt these. Verify. Troubleshoot any issues. Celebrate success!

---

## Afternoon Session: Data Manipulation & Advanced Queries

### 1:00 PM - 1:15 PM: Afternoon Recap & Introduction (15 minutes)

**Content**:
- Welcome back post-lunch; re-energize
- Recap morning: "You've queried data—written SELECT with WHERE, ORDER BY. Professional work."
- Afternoon agenda:
  - "How to change data: INSERT (add), UPDATE (modify), DELETE (remove)"
  - "How to summarize data: COUNT, SUM, AVG, GROUP BY"
  - "How to combine tables: Introduction to JOINs"
- "These are the skills every database job requires"

**Engagement**: Share: "By 4:30 PM, you'll be able to answer complex questions like 'What's our total sales by category?' or 'How many orders did each customer make?'"

---

### 1:15 PM - 2:30 PM: Data Manipulation (75 minutes)

**Objective**: Students can INSERT, UPDATE, and DELETE data; understand transactions and rollback.

**Delivery Method**: Demonstration + Pair Programming + Hands-On Practice

**Content:**

**PART 1: INSERT Statement (20 minutes)**

**1. Basic INSERT (5 min)**

Live demo in pgAdmin:

```sql
INSERT INTO customers (first_name, last_name, email, phone, city, state)
VALUES ('Alice', 'Johnson', 'alice.j@example.com', '555-111-2222', 'Springfield', 'IL');
```

Show message: "INSERT 1" (1 row inserted)

Then verify:
```sql
SELECT * FROM customers WHERE first_name = 'Alice';
```

Show: New customer appears in results

Explain:
- `INSERT INTO table (columns)` specifies what to insert
- `VALUES (values)` provides the data
- Columns you don't list get NULL (or DEFAULT if defined)
- Order matters: VALUES must match column order

**Teaching Point**: "Notice we didn't specify customer_id or created_at. Why? They auto-populate—ID is SERIAL (auto-increment), created_at has DEFAULT CURRENT_TIMESTAMP."

**Activity**: Have students insert themselves:
```sql
INSERT INTO customers (first_name, last_name, email, city, state)
VALUES ('Bob', 'Smith', 'bob.smith@example.com', 'Chicago', 'IL');
```

Verify they see: "INSERT 1" message

**2. INSERT multiple rows (5 min)**

```sql
INSERT INTO customers (first_name, last_name, email, city, state)
VALUES 
    ('Carol', 'White', 'carol.w@example.com', 'Denver', 'CO'),
    ('David', 'Brown', 'david.b@example.com', 'Austin', 'TX'),
    ('Eve', 'Green', 'eve.g@example.com', 'Seattle', 'WA');
```

Show: "INSERT 3" (3 rows inserted)

Explain: "You can insert multiple rows in one statement using multiple VALUES"

**Activity**: Students insert 2-3 products (into products table)

**3. INSERT with calculations (5 min)**

```sql
INSERT INTO orders (customer_id, order_date, total_amount, status)
VALUES (1, CURRENT_TIMESTAMP, 299.99, 'completed');
```

Then add order items:
```sql
INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
VALUES (1, 1, 2, 99.99, 199.98);
```

Show relationships: Orders reference customers (customer_id), order_items reference orders and products

Explain: "When inserting, foreign keys must exist—you can't create an order for a customer_id that doesn't exist"

**4. Common INSERT errors (5 min)**

Show errors and how to fix:

**Error 1: Column doesn't exist**
```sql
INSERT INTO customers (first_name, last_name, invalid_column)
VALUES ('Test', 'User', 'value');
```
Error: "column 'invalid_column' of relation 'customers' does not exist"

**Fix**: Check column names: `\d customers` in psql or look in pgAdmin table structure

**Error 2: UNIQUE constraint violation**
```sql
INSERT INTO customers (first_name, last_name, email)
VALUES ('Test', 'User', 'john.doe@example.com');  -- email already exists
```
Error: "duplicate key value violates unique constraint"

**Fix**: Use unique email address

**Error 3: Foreign key violation**
```sql
INSERT INTO orders (customer_id, total_amount, status)
VALUES (999, 100.00, 'pending');  -- customer_id 999 doesn't exist
```
Error: "insert or update on table 'orders' violates foreign key constraint"

**Fix**: Use existing customer_id

---

**PART 2: UPDATE Statement (20 minutes)**

**1. Basic UPDATE (5 min)**

```sql
UPDATE customers 
SET phone = '555-999-9999' 
WHERE customer_id = 1;
```

Show: "UPDATE 1" message

Verify:
```sql
SELECT * FROM customers WHERE customer_id = 1;
```

Show: Phone updated

Explain:
- `UPDATE table` specifies which table
- `SET column = value` specifies what to change
- `WHERE condition` specifies which rows (CRUCIAL!)
- If you forget WHERE, ALL rows update—disaster!

**Teaching Point**: "Always test your WHERE condition with SELECT first. Do: `SELECT * FROM customers WHERE customer_id = 1;` then change SELECT to UPDATE. Safe pattern."

**Activity**: Students update a customer's phone number

**2. UPDATE multiple columns (5 min)**

```sql
UPDATE customers 
SET city = 'Cambridge', state = 'MA', zip_code = '02139'
WHERE customer_id = 2;
```

Show: "UPDATE 1" (one row, multiple columns changed)

Explain: "You can change multiple columns in one UPDATE statement"

**3. UPDATE multiple rows (5 min)**

```sql
UPDATE products 
SET stock_quantity = stock_quantity - 10 
WHERE category_id = 1;
```

Show: "UPDATE 3" (three electronics products' stock reduced)

Explain:
- `stock_quantity - 10` uses current value and decreases it
- Useful for: Adjusting inventory, applying bulk changes
- BE CAREFUL: Check WHERE condition first!

**4. DELETE statement introduction (5 min)**

```sql
DELETE FROM products WHERE product_id = 999;
```

Show: "DELETE 0" (no rows with that ID, so nothing deleted—safe!)

Explain:
- `DELETE FROM table WHERE condition`
- Deletes matching rows PERMANENTLY
- If you forget WHERE: ALL rows deleted—disaster!
- No undo without backup

**Teaching Point**: "DELETE is dangerous. Best practice: Have a backup. Test DELETE with SELECT first. Never delete production data without approval and backup."

**Safety Tip**: In production databases, use soft deletes (add `is_deleted BOOLEAN` column instead of actually removing rows)

---

**PART 3: Transactions & ROLLBACK (15 minutes)**

**Concept: All-or-Nothing Operations**

Scenario: "Transfer $100 from John's account to Jane's account"
- Step 1: Deduct $100 from John
- Step 2: Add $100 to Jane

What if Step 1 succeeds but Step 2 fails? John loses money, Jane doesn't get it. Bad!

**Solution: Transactions**

```sql
BEGIN;

UPDATE customers SET account_balance = account_balance - 100 WHERE customer_id = 1;
UPDATE customers SET account_balance = account_balance + 100 WHERE customer_id = 2;

COMMIT;  -- Make both changes permanent
```

If Step 2 fails:
```sql
BEGIN;

UPDATE customers SET account_balance = account_balance - 100 WHERE customer_id = 1;
UPDATE customers SET account_balance = account_balance + 100 WHERE customer_id = 2;

ROLLBACK;  -- Undo both changes
```

Explain:
- `BEGIN;` starts a transaction (group of operations)
- If error occurs: `ROLLBACK;` undoes everything
- If all good: `COMMIT;` makes everything permanent
- All-or-nothing guarantee

**Demo**: Show what happens if you rollback:

```sql
BEGIN;
UPDATE customers SET phone = '555-000-0000' WHERE customer_id = 1;
SELECT * FROM customers WHERE customer_id = 1;  -- Shows new phone
ROLLBACK;
SELECT * FROM customers WHERE customer_id = 1;  -- Back to original!
```

**Hands-On Exercise (5 min)**

Scenario: "Create an order for a customer. The order has 3 items. If anything goes wrong, undo everything."

```sql
BEGIN;

-- Create order
INSERT INTO orders (customer_id, order_date, total_amount, status)
VALUES (1, CURRENT_TIMESTAMP, 500.00, 'pending');

-- Get the order_id that was just created (advanced; mention if time)
-- Then add items...
-- If all good:
COMMIT;

-- If problem:
-- ROLLBACK;
```

This is complex; simplify as needed. The key concept: transactions protect data integrity.

---

### 2:30 PM - 2:45 PM: BREAK (15 minutes)

---

### 2:45 PM - 4:00 PM: Aggregate Functions & GROUP BY (75 minutes)

**Objective**: Students use aggregate functions and GROUP BY to summarize data and answer business questions.

**Delivery Method**: Demonstration + Interactive Analysis + Hands-On Practice

**Content:**

**PART 1: Aggregate Functions (25 minutes)**

**1. COUNT (5 min)**

```sql
SELECT COUNT(*) AS total_customers FROM customers;
```

Result: "9" (8 original + Alice + Bob we added)

Explain:
- `COUNT(*)` counts all rows
- `COUNT(column)` counts non-NULL values in that column
- Useful for: "How many products?", "How many orders?"

Alternative:
```sql
SELECT COUNT(phone) AS customers_with_phone FROM customers;
```
(Counts only rows where phone is not NULL)

**Activity**: Students write:
```sql
SELECT COUNT(*) AS total_products FROM products;
```

**2. SUM (5 min)**

```sql
SELECT SUM(total_amount) AS total_revenue FROM orders;
```

Result: Sum of all order amounts

Explain:
- `SUM(column)` adds up all values
- Only works on numeric columns
- Useful for: "Total sales", "Total inventory value"

**Activity**: Students write:
```sql
SELECT SUM(stock_quantity * price) AS total_inventory_value FROM products;
```

**3. AVG, MIN, MAX (5 min)**

```sql
SELECT 
    AVG(price) AS average_price,
    MIN(price) AS cheapest,
    MAX(price) AS most_expensive
FROM products;
```

Show results:
```
average_price | cheapest | most_expensive
   247.48     |  14.99   |   1299.99
```

Explain:
- `AVG(column)` calculates average
- `MIN(column)` finds minimum value
- `MAX(column)` finds maximum value
- Useful for: Price analysis, performance metrics

**Activity**: Students write:
```sql
SELECT 
    COUNT(*) AS order_count,
    AVG(total_amount) AS average_order_value,
    MIN(total_amount) AS smallest_order,
    MAX(total_amount) AS largest_order
FROM orders;
```

**4. Combining aggregates (5 min)**

```sql
SELECT 
    COUNT(*) AS total_products,
    COUNT(DISTINCT category_id) AS unique_categories,
    AVG(price) AS avg_price,
    SUM(stock_quantity) AS total_stock
FROM products;
```

Show results: Multiple statistics in one query

Explain: "You can combine multiple aggregate functions to get a dashboard-like view of data"

**Important Note**: "Once you use an aggregate function, you're summarizing ALL rows. The result is always ONE row. More on this when we learn GROUP BY..."

---

**PART 2: GROUP BY Clause (25 minutes)**

**Problem**: "We want statistics BY category, not for all products combined."

**Solution**: GROUP BY

**1. Basic GROUP BY (5 min)**

```sql
SELECT 
    category_id,
    COUNT(*) AS product_count,
    AVG(price) AS average_price
FROM products
GROUP BY category_id;
```

Show results:
```
category_id | product_count | average_price
     1      |       3       |   683.32
     2      |       3       |   53.32
     3      |       3       |   24.99
     4      |       2       |   69.99
     5      |       1       |   24.99
```

Explain:
- `GROUP BY category_id` groups products by category
- Aggregates (COUNT, AVG) apply to each group
- Result: One row per group
- Useful for: Reporting, analysis by dimension

**2. GROUP BY with multiple columns (5 min)**

Show example (may not have good sample data, but explain):

```sql
SELECT 
    status,
    EXTRACT(MONTH FROM order_date) AS month,
    COUNT(*) AS order_count,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY status, EXTRACT(MONTH FROM order_date)
ORDER BY month, status;
```

Explain: "Group by multiple columns when you want breakdowns by multiple dimensions (e.g., order status AND month)"

**3. GROUP BY with JOIN (10 min)**

More useful example:

```sql
SELECT 
    c.category_name,
    COUNT(p.product_id) AS product_count,
    AVG(p.price) AS average_price,
    SUM(p.stock_quantity) AS total_stock
FROM products p
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name;
```

Show results: Product statistics by category NAME (more readable than ID)

Explain:
- Joins data from two tables
- Groups by category name
- Calculates statistics per category
- Much more useful for reporting than category IDs

**This is powerful!** Emphasize: "This single query answers: What products do we have in each category? How expensive on average? How much inventory?"

---

**PART 3: HAVING Clause (10 minutes)**

**Problem**: "I want to see only categories with more than 2 products."

**Wrong approach**: `WHERE COUNT(*) > 2` ← Doesn't work! COUNT is aggregate, can't filter before grouping

**Solution**: HAVING (filter groups AFTER aggregation)

```sql
SELECT 
    c.category_name,
    COUNT(p.product_id) AS product_count
FROM products p
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name
HAVING COUNT(p.product_id) > 2;
```

Result: Only categories with > 2 products

Explain:
- `WHERE` filters individual rows (before grouping)
- `HAVING` filters groups (after grouping)
- `HAVING` uses aggregate functions; `WHERE` doesn't
- Useful for: "Show me categories with high sales", "Show customers with many orders"

**Visual Comparison**:
```
WHERE  [Filter individual rows] → GROUP BY [Group remaining rows] → HAVING [Filter groups]
```

**Activity**: Students write:
```sql
SELECT 
    status,
    COUNT(*) AS order_count
FROM orders
GROUP BY status
HAVING COUNT(*) > 0;  -- Orders with at least 1 order (will show all)
```

---

**PART 4: Guided Complex Queries (15 minutes)**

**Exercise 1**: "For each category, show name, product count, and average price. Only show categories with average price > $50."

```sql
SELECT 
    c.category_name,
    COUNT(p.product_id) AS product_count,
    AVG(p.price) AS average_price
FROM products p
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name
HAVING AVG(p.price) > 50
ORDER BY average_price DESC;
```

Walk through:
- JOIN: Combine products with category names
- GROUP BY: One row per category
- AVG: Calculate average price per category
- HAVING: Only categories with avg > $50
- ORDER BY: Show most expensive categories first

**Exercise 2**: "Which customers have placed more than 1 order?"

```sql
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS order_count,
    SUM(o.total_amount) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(o.order_id) > 1
ORDER BY total_spent DESC;
```

Walk through: Similar pattern; explains LEFT JOIN briefly (preview of Day 3)

Have students attempt these. Provide hints. Verify results. Celebrate!

---

### 4:00 PM - 4:15 PM: Introduction to JOINs Preview (15 minutes)

**Objective**: Set up expectation for Day 3; show why JOINs are necessary.

**Content**:

**Why JOINs?** (Recap you've already been using them)

"Today you've been using JOINs without calling them that. Example:"

```sql
SELECT 
    c.category_name,
    COUNT(p.product_id) AS product_count
FROM products p
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name;
```

"The `JOIN` part combines products table with categories table. Without it, you'd only have category_id numbers, not names."

**Types of JOINs** (Brief preview):
- **INNER JOIN**: Only matching rows (most common)
- **LEFT JOIN**: All rows from left table + matching from right
- **RIGHT JOIN**: All rows from right table + matching from left
- **FULL OUTER JOIN**: All rows from both tables
- **CROSS JOIN**: All combinations

**Tomorrow**: "Day 3, we deep-dive into all of these. You'll become JOIN experts."

**Exciting Preview**: "Once you master JOINs, you can query across 5+ tables in one query. That's where the real power of SQL appears."

---

### 4:15 PM - 4:30 PM: Wrap-Up & Day 2 Checkout (15 minutes)

**Recap What We Covered (3 minutes)**
- This morning: SELECT, WHERE, ORDER BY, LIMIT (querying)
- This afternoon: INSERT, UPDATE, DELETE (changing data), Aggregates & GROUP BY (summarizing)

**Key Takeaways (2 minutes)**
- SELECT is the most-used SQL command (look up data)
- WHERE filters; ORDER BY sorts; LIMIT restricts results
- INSERT adds; UPDATE modifies; DELETE removes
- Transactions (BEGIN/COMMIT/ROLLBACK) protect data integrity
- Aggregates + GROUP BY answer complex business questions

**Preview Day 3 (2 minutes)**
- Complex JOINs and advanced query techniques
- Subqueries (queries within queries)
- Database security (who can access what)
- Building a REST API (real web application)

**Day 2 Completion Checklist - Verify Everyone (3 minutes)**

- [ ] Can write SELECT queries with WHERE, ORDER BY
- [ ] Can use aggregate functions (COUNT, SUM, AVG, MIN, MAX)
- [ ] Can use GROUP BY and HAVING
- [ ] Can INSERT data into tables
- [ ] Can UPDATE existing rows
- [ ] Can DELETE rows (carefully!)
- [ ] Understand transactions (BEGIN, COMMIT, ROLLBACK)
- [ ] Can execute these queries in pgAdmin

"Raise your hand if you're missing any of these. We'll sort it out now."

**Homework / Prep for Day 3 (2 minutes)**
- **Do**: Review `advanced_queries.sql` file (look at GROUP BY examples)
- **Do**: Try creating 2-3 of your own GROUP BY queries
- **Optional**: Read about JOINS online (Wikipedia or W3Schools)
- **Bring**: Any questions about today's material

**Logistics for Day 3**
- Same time, same place (9:00 AM)
- Bring your laptop (don't forget!)
- You'll be working with the REST API project—exciting stuff!

**Final Words**: "You've gone from 'What's a database?' to writing professional SQL queries. That's huge progress. Tomorrow you'll learn advanced techniques, but you already have the foundation. Great work!"

---

## Assignments & Exercises

### In-Class Exercises (Graded by Completion/Participation)

**Exercise 1: Basic SELECT Queries (Morning)**
- Duration: 15 minutes
- Students write SELECT queries with column selection, ordering, limiting
- Grading: 5 points for 3 queries executed successfully

**Exercise 2: WHERE Clause Filtering (Morning)**
- Duration: 15 minutes
- Write queries with AND, OR, LIKE conditions
- Grading: 5 points for logical correctness

**Exercise 3: Data Manipulation (Afternoon)**
- Duration: 20 minutes
- INSERT 2 new customers, UPDATE one, DELETE testing (carefully!)
- Grading: 5 points for successful execution without errors

**Exercise 4: Aggregate Functions & GROUP BY (Afternoon)**
- Duration: 25 minutes
- Write queries using COUNT, SUM, AVG with GROUP BY
- Answer: "How many products per category?", "What's average price by category?"
- Grading: 10 points for correct syntax and logical results

### Take-Home Assignments (Optional)

**Assignment 1: Design a Query (1 hour)**
- Scenario: E-commerce manager wants to know
  - Total revenue by product category
  - Average order value per customer
  - Which products are in low stock (< 30 units)
- Write 3 queries to answer these questions

**Assignment 2: Data Cleanup (30 min)**
- Review your bootcamp_db data
- If any sample data looks wrong, UPDATE it
- Practice safe updating with WHERE clauses

**Assignment 3: Explore Aggregates (30 min)**
- Experiment with different combinations of aggregate functions
- Combine COUNT, SUM, AVG in single query
- Learn which combinations make sense (and which don't)

---

## Teaching Tips & Common Pitfalls

### High-Impact Teaching Strategies

**1. Test Pattern Before Modifying**
- Teach: "Before UPDATE or DELETE, write SELECT with same WHERE to verify"
- Model: `SELECT * FROM table WHERE condition;` then swap SELECT for UPDATE/DELETE
- Students adopt this as safety habit

**2. Visual Query Breakdown**
- Show query on screen, underline each clause in different color
- "WHERE does this", "ORDER BY does this", "LIMIT does this"
- Helps visual learners understand query flow

**3. Real-World Scenarios**
- Don't say "Write query with GROUP BY"
- Say "Manager wants to know: Which product category makes most revenue?"
- Students see relevance immediately

**4. Build Incrementally**
- Start: `SELECT * FROM products`
- Add: `SELECT product_name, price FROM products`
- Add: `WHERE price > 100`
- Add: `ORDER BY price DESC`
- Add: `LIMIT 10`
- Show how each clause builds on previous

**5. Make Mistakes on Purpose**
- Write query with logical error
- Run it; show unexpected results
- "What went wrong? Let's debug together."
- Students learn critical thinking

**6. Pair Programming for Complex Queries**
- One student types; one watches/suggests
- "What should we add next to filter by category?"
- Switches roles midway
- Builds confidence; reduces frustration

### Common Misconceptions & Corrections

**Misconception 1: "WHERE filters after aggregation"**

**Reality**: WHERE filters rows BEFORE GROUP BY/aggregation

**Correction**: Show visually:
```
Raw data → WHERE filters → GROUP BY groups → HAVING filters groups → Results
```

"WHERE is early; HAVING is late."

**Misconception 2: "I can use aggregate function in WHERE"**

Example (wrong):
```sql
SELECT * FROM products WHERE COUNT(*) > 5;  -- ERROR!
```

**Correction**: "Aggregates only in SELECT and HAVING. Use HAVING for filtering groups."

**Misconception 3: "UPDATE without WHERE only changes one row"**

**Reality**: UPDATE without WHERE changes ALL rows (disaster!)

**Correction**: "Always use WHERE. Make it a rule. No exceptions."

**Misconception 4: "DISTINCT removes all duplicates from result"**

```sql
SELECT DISTINCT customer_id, order_id FROM orders;
```

**Reality**: DISTINCT looks at combination of columns

**Correction**: "DISTINCT looks at complete row. Two rows with same customer_id but different order_id are different."

**Misconception 5: "NULL and empty string are the same"**

**Reality**: NULL means unknown; empty string (' ') means known but blank

**Correction**: Show queries:
```sql
WHERE column IS NULL vs. WHERE column = ''
```
Different results!

### Pacing & Timing Adjustments

**If Running Behind**:
- Skip HAVING clause (mention, defer to Day 3)
- Skip transaction examples (mention concept, show simple COMMIT only)
- Focus on SELECT, WHERE, INSERT, UPDATE, DELETE
- Move GROUP BY introduction to Day 3

**If Running Ahead**:
- Deep-dive into transaction scenarios (more complex examples)
- Add WINDOW FUNCTIONS teaser (OVER, PARTITION BY)
- Have extra exercises ready (complex WHERE with nested conditions)
- Introduce database design patterns

**If Data Manipulation Takes Longer**:
- That's okay; this is critical material
- Reduce GROUP BY practice time
- Emphasize SAFETY over speed for UPDATE/DELETE

**If GROUP BY Confuses Students**:
- Use simpler example: "How many products in each category?"
- Show GROUP BY before aggregates (not after)
- Draw table on board showing how GROUP BY creates groups
- Avoid HAVING initially; introduce later

### Energy & Engagement

**Post-Lunch Slump Mitigation**:
- Start afternoon with interactive challenge ("Write a query to find...")
- Use pair programming (dynamic, engaging)
- Include celebration of small wins
- Take short movement break if energy low

**Build Momentum**:
- Start with easy wins (SELECT is simple)
- Gradually increase complexity
- End afternoon with satisfying complex query
- Students leave feeling accomplished

---

## Troubleshooting Guide

### Common Query Errors

**Error: "Syntax error at or near 'FROM'"**
- **Cause**: Typo in SELECT statement
- **Fix**: Check spelling; read error message line-by-line

**Error: "column 'name' must appear in the GROUP BY clause or be used in an aggregate function"**
- **Cause**: Using column in SELECT that's not in GROUP BY
- **Rule**: Every non-aggregated column must be in GROUP BY
- **Fix**: Add column to GROUP BY or wrap in aggregate function

**Error: "Subquery returns more than one row"**
- **Cause**: Using subquery that returns multiple rows in wrong place
- **Fix**: Subquery must return 1 row in WHERE, or use IN operator

**Error: "UPDATE/DELETE returned 0 rows"**
- **Cause**: WHERE condition matched nothing
- **Fix**: Verify WHERE condition; run SELECT first with same WHERE

### Common Data Issues

**Issue: Duplicate data appears after INSERT**
- **Cause**: Ran INSERT twice by accident
- **Fix**: Use undo/rollback; delete duplicates

**Issue: Data looks wrong after UPDATE**
- **Cause**: WHERE condition was broader than intended
- **Fix**: Check WHERE condition; restore from backup if needed

**Issue: JOINs return unexpected number of rows**
- **Cause**: Joining on wrong column; creating cartesian product
- **Fix**: Check JOIN ON condition; verify it's one-to-one relationship

### pgAdmin Issues

**Issue: pgAdmin won't run query**
- **Fix**: Click query → Press F5 (or Execute button)
- Verify query syntax first in separate test

**Issue: Query results show as truncated**
- **Fix**: Click column header → Widen column manually
- Adjust display settings in pgAdmin preferences

**Issue: Too many rows displayed (slowing interface)**
- **Fix**: Add LIMIT clause to query
- Use pagination in pgAdmin results

---

## Assessment & Completion Checklist

### Day 2 Success Criteria

Students successfully complete Day 2 if they:

1. **✓ Query Writing**
   - Write SELECT queries with column selection
   - Use WHERE to filter data
   - Use ORDER BY and LIMIT correctly
   - Demonstrate understanding through independent query writing

2. **✓ Data Manipulation**
   - Execute INSERT statements successfully
   - Execute UPDATE statements with proper WHERE clauses
   - Execute DELETE statements safely
   - Understand transaction concepts (BEGIN/COMMIT/ROLLBACK)

3. **✓ Aggregation & Grouping**
   - Use COUNT, SUM, AVG, MIN, MAX appropriately
   - Write GROUP BY queries correctly
   - Use HAVING to filter groups
   - Combine aggregates with JOINs

4. **✓ pgAdmin Proficiency**
   - Navigate database structure in pgAdmin
   - Write and execute queries in Query Tool
   - View and interpret results
   - Use pgAdmin for data exploration

### Student Self-Assessment (Provide Handout)

```
Rate your confidence (1=Not confident, 5=Very confident):

1. I can write SELECT queries with specific columns         [ ]
2. I understand WHERE clauses and use them correctly        [ ]
3. I can use ORDER BY and LIMIT to control results          [ ]
4. I can INSERT new data into tables                        [ ]
5. I can UPDATE existing data with WHERE conditions         [ ]
6. I can use aggregate functions (COUNT, SUM, etc.)         [ ]
7. I can use GROUP BY to summarize data                     [ ]
8. I'm comfortable using pgAdmin interface                  [ ]
9. I understand when to use HAVING vs. WHERE                [ ]
10. I'm ready for Day 3 (JOINs and advanced queries)        [ ]

Biggest challenge from today:
_________________________________________________________________

What do you want to practice more?
_________________________________________________________________
```

### Instructor Completion Checklist

Before Day 3, verify:

- [ ] All students can write basic SELECT queries
- [ ] All students understand WHERE filtering
- [ ] All students successfully executed INSERT/UPDATE/DELETE
- [ ] All students attempted GROUP BY queries
- [ ] Students comfortable with pgAdmin interface
- [ ] Any students with gaps identified for extra help
- [ ] Day 3 materials (advanced_joins.sql, etc.) ready
- [ ] REST API project files accessible to students

### Grading Rubric (if formal grading)

| Criteria | Full (5) | Partial (3) | Incomplete (1) |
|----------|----------|-----------|--------------|
| **SELECT Queries** | Writes varied queries correctly | Most queries work, minor syntax issues | Cannot write functional queries |
| **WHERE Clauses** | Correctly filters with AND/OR/LIKE | Mostly correct; occasional logic errors | Cannot filter correctly |
| **Aggregates & GROUP BY** | Correct syntax; meaningful results | Mostly works; some logical errors | Cannot aggregate/group |
| **Data Manipulation** | INSERT/UPDATE/DELETE successful; safe | Works but occasional errors | Cannot modify data safely |
| **pgAdmin Use** | Comfortable navigation; efficient querying | Can navigate; slower execution | Struggles with interface |

---

## Resources & Reference Materials

### Student Handouts to Prepare

**Handout 1: SQL Clause Reference**
```
SELECT Clause Order (Critical!)
SELECT columns
FROM table
WHERE condition
GROUP BY column
HAVING group_condition
ORDER BY column
LIMIT number;

Remember: WHERE filters rows, HAVING filters groups!
```

**Handout 2: WHERE Operators**
```
= Equal
<> Not equal
> Greater than
< Less than
>= Greater or equal
<= Less or equal
AND Both conditions true
OR Either condition true
LIKE Pattern matching (% = wildcard)
IN (value1, value2)
BETWEEN value1 AND value2
IS NULL
```

**Handout 3: Aggregate Functions**
```
COUNT(*) - Count all rows
COUNT(column) - Count non-NULL values
SUM(column) - Total of numeric values
AVG(column) - Average value
MIN(column) - Minimum value
MAX(column) - Maximum value
```

**Handout 4: Common Query Patterns**

```sql
-- Find specific data
SELECT * FROM table WHERE condition

-- Find top N
SELECT * FROM table ORDER BY column DESC LIMIT N

-- Summarize data
SELECT column, COUNT(*) FROM table GROUP BY column

-- Combine tables
SELECT * FROM table1 JOIN table2 ON table1.id = table2.id

-- Safe data update
SELECT * FROM table WHERE condition;  -- Test first
UPDATE table SET column = value WHERE condition;

-- Safe data delete
SELECT * FROM table WHERE condition;  -- Test first
DELETE FROM table WHERE condition;
```

### Online Resources to Share

- **W3Schools SQL Tutorial**: https://www.w3schools.com/sql/ (beginner-friendly)
- **PostgreSQL Official Docs**: https://www.postgresql.org/docs/current/ (comprehensive)
- **SQL Performance Explained**: https://www.sql-performance-explained.com/ (optimization basics)

### Videos & Demos (Recorded or Bookmarked)

- "SELECT Explained" - 5 minute overview
- "GROUP BY Walkthrough" - 10 minute deep dive
- "JOINs Preview" - 5 minute teaser for Day 3

---

## Additional Instructor Notes

### Classroom Management

- **Students typing slowly?** That's fine. SQL syntax is precise; speed comes later.
- **Someone stuck on error?** Have them pair with neighbor; explain error together.
- **Room seems confused?** Pause; go back 5 minutes; re-explain with different example.

### Building Community

- Celebrate small wins: "Great WHERE clause!"
- Acknowledge difficulty: "GROUP BY is one of the hardest SQL concepts"
- Create safety: "There's no 'wrong' query here—just queries that teach us"

### Data-Driven Teaching

- Circulate; listen to misconceptions
- Note which concepts take longest
- Adjust Day 3 based on Day 2 struggles
- Share results: "Everyone got GROUP BY except 2 of you—let's clarify..."

### Energy Management

- Morning: High energy (fresh after break)
- Post-lunch: Slump (plan interactive activity)
- Late afternoon: Either tired OR excited (depends on success)
- Use activities to manage energy

---

## Conclusion

Day 2 is successful when:
- **Every student writes working SELECT queries independently**
- **Every student understands WHERE filtering and can explain it**
- **Every student can safely INSERT/UPDATE/DELETE data**
- **Every student has written at least one GROUP BY query**
- **Every student feels confident and ready for Day 3**

Remember:
- SQL is learnable; show patience
- Celebrate progress (Day 1 to Day 2 is huge leap)
- Connect to real jobs ("Every developer writes these queries daily")
- Build excitement for Day 3 ("Tomorrow: JOINs and APIs!")

Great work! Day 2 is foundational to everything that comes next.

---

**Document Version**: 1.0  
**Last Updated**: Day 2 Planning  
**For Use**: SQL Bootcamp Day 2 (3-Day Course)