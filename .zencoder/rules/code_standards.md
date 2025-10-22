---
description: Code style and standards for SQL, shell scripts, and other code examples
alwaysApply: true
---

# Code Standards

## Overview
All code in course repositories should follow these standards for consistency, readability, and educational value.

---

## SQL Code Standards

### Formatting & Style

#### Capitalization
- **Keywords**: UPPERCASE (SELECT, FROM, WHERE, JOIN, etc.)
- **Built-in functions**: UPPERCASE (COUNT, SUM, AVG, MAX, MIN, etc.)
- **Table names**: lowercase (customers, orders, products)
- **Column names**: lowercase (customer_id, order_date, first_name)
- **Aliases**: lowercase (c for customers, o for orders)

#### Indentation & Line Breaks
```sql
-- Good: Clear indentation and logical breaks
SELECT 
    customer_id,
    first_name,
    last_name,
    email
FROM customers
WHERE country = 'USA'
    AND status = 'active'
ORDER BY last_name;

-- Avoid: Everything on one line (hard to read)
SELECT customer_id, first_name, last_name, email FROM customers WHERE country = 'USA' AND status = 'active' ORDER BY last_name;
```

**Line break rules**:
- Put SELECT keyword on first line, list columns on following lines (one per line for readability)
- Put FROM on its own line
- Put WHERE on its own line, with conditions indented
- Put JOIN clauses on their own lines
- Put ORDER BY on its own line
- Use 4 spaces for indentation (not tabs)

#### JOINs Format
```sql
-- Good: Clear and readable
SELECT 
    c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_date > '2024-01-01';

-- Also acceptable (both ON same line or separate):
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
```

#### WHERE Conditions
```sql
-- Good: Logical grouping with parentheses where helpful
WHERE 
    (country = 'USA' OR country = 'Canada')
    AND status = 'active'
    AND total_spent > 1000;

-- Good: Multiple conditions clearly separated
WHERE country = 'USA'
    AND status = 'active'
    AND total_spent > 1000;
```

### Naming Conventions

#### Table Names
- **Plural**: `customers`, `orders`, `products` (not `customer`, `order`)
- **No abbreviations**: `employees`, not `emp` or `emps`
- **Descriptive**: Use full words that describe the data
- **Snake_case**: `order_items`, not `OrderItems` or `orderitems`

#### Column Names
- **Singular**: `customer_id`, `order_date`, `first_name` (not `customers_id`)
- **Include entity in FK columns**: `customer_id` (not just `id`)
- **Descriptive**: `order_date`, not `date` or `d`
- **Snake_case**: `created_at`, `updated_at`, `total_amount`

#### Aliases
- **Single letter for simple alias**: FROM customers c
- **Descriptive for complex queries**: FROM order_items AS oi, orders AS o
- **Be consistent**: If using 'c' for customers, always use 'c'

```sql
-- Good: Clear, consistent aliases
SELECT 
    c.first_name,
    COUNT(o.order_id) as total_orders
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name;

-- Avoid: Inconsistent, confusing abbreviations
SELECT 
    cu.first_name,
    COUNT(ord.order_id) as cnt
FROM customers cu
LEFT JOIN orders ord ON cu.customer_id = ord.customer_id
GROUP BY cu.customer_id, cu.first_name;
```

### Comments & Documentation

#### File Header
Every SQL file should start with:
```sql
-- ========================================
-- [Topic Name]
-- Course: [Course Name]
-- Day [X]
-- ========================================
-- Description: [What this file contains]
-- Concepts: [List of concepts covered]
-- ========================================
```

#### Section Comments
```sql
-- ========================================
-- SECTION: [Section Name]
-- ========================================
```

#### Example Comments
```sql
-- Example 1.1: [What this query demonstrates]
-- Purpose: [Why we need this]
SELECT ...
```

#### Inline Comments
```sql
SELECT 
    customer_id,
    first_name,
    CASE 
        WHEN total_spent > 5000 THEN 'Premium'      -- High-value customers
        WHEN total_spent > 1000 THEN 'Regular'      -- Regular customers
        ELSE 'New'                                    -- New/inactive customers
    END as customer_tier
FROM customers;
```

**Comment guidelines**:
- ✓ Explain WHY, not WHAT (the code shows what)
- ✓ Explain non-obvious logic
- ✓ Keep comments concise
- ✓ Use `--` for single-line comments
- ✓ Use `/* */` only for multi-line comments (rarely needed)
- ✗ Don't state the obvious: `SELECT * FROM customers  -- selecting all from customers`

### Query Structure Best Practices

#### CTEs (Common Table Expressions)
```sql
-- Use CTEs to organize complex queries
WITH active_customers AS (
    SELECT customer_id, first_name, email
    FROM customers
    WHERE status = 'active'
),
recent_orders AS (
    SELECT customer_id, order_id, order_date
    FROM orders
    WHERE order_date > CURRENT_DATE - INTERVAL '30 days'
)
SELECT 
    ac.customer_id,
    ac.first_name,
    COUNT(ro.order_id) as recent_order_count
FROM active_customers ac
LEFT JOIN recent_orders ro ON ac.customer_id = ro.customer_id
GROUP BY ac.customer_id, ac.first_name;
```

#### Subqueries
```sql
-- Use subqueries when simpler than CTEs for single use
SELECT 
    customer_id,
    first_name,
    (SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.customer_id) as order_count
FROM customers c
WHERE email LIKE '%@company.com';
```

#### Functions
```sql
-- Use built-in functions effectively
SELECT 
    DATE_TRUNC('month', order_date) as month,
    COUNT(*) as order_count,
    SUM(total_amount) as total_sales,
    ROUND(AVG(total_amount), 2) as avg_order_value
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month DESC;
```

### Common Patterns

#### String Matching
```sql
-- Exact match
WHERE status = 'active'

-- Partial match
WHERE email LIKE '%@gmail.com'

-- Case-insensitive (PostgreSQL)
WHERE LOWER(email) LIKE '%gmail%'

-- Multiple values
WHERE status IN ('active', 'pending', 'review')
```

#### Dates
```sql
-- Current date
WHERE order_date > CURRENT_DATE - INTERVAL '30 days'

-- Specific date
WHERE order_date = '2024-01-15'

-- Date range
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'

-- Last month
WHERE DATE_TRUNC('month', order_date) = DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
```

#### NULL Handling
```sql
-- Check for NULL
WHERE email IS NULL           -- Correct
WHERE email IS NOT NULL       -- Correct

-- Avoid:
-- WHERE email = NULL           -- Wrong, always returns false
-- WHERE email != NULL          -- Wrong, always returns false

-- Use COALESCE to provide defaults
SELECT 
    customer_id,
    COALESCE(phone, 'No phone') as phone_or_default
FROM customers;
```

### Error Prevention

#### Foreign Key Usage
```sql
-- Always use the full reference
WHERE customer_id = 5           -- Good
WHERE id = 5                    -- Bad (ambiguous)

-- In JOINs, be explicit
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
    -- Good: Clear which ID references which table
```

#### Aggregate Functions
```sql
-- When using GROUP BY, include all non-aggregated columns in the SELECT
SELECT 
    customer_id,              -- Include in GROUP BY
    first_name,               -- Include in GROUP BY
    COUNT(*) as order_count   -- Aggregate function
FROM orders
GROUP BY customer_id, first_name;

-- Not like this:
-- SELECT first_name, COUNT(*) FROM orders GROUP BY customer_id;
-- ^ first_name not in GROUP BY - will error or return unexpected results
```

#### DISTINCT Usage
```sql
-- Use DISTINCT when needed, but consider if GROUP BY is better
SELECT DISTINCT country
FROM customers
ORDER BY country;

-- Better for aggregates:
SELECT country, COUNT(*) as count
FROM customers
GROUP BY country
ORDER BY count DESC;
```

---

## Shell Script Standards (.sh files)

### Structure
```bash
#!/bin/bash

# ========================================
# [Script Name]
# Course: [Course Name]
# ========================================
# Description: What this script does
# Usage: How to run it
# Prerequisites: What's needed before running
# ========================================

set -e  # Exit on error

# ========================================
# Configuration
# ========================================
DATABASE_NAME="your_database"
DATABASE_USER="postgres"

# ========================================
# Functions
# ========================================
check_prerequisites() {
    # Check if required tools are installed
    if ! command -v psql &> /dev/null; then
        echo "Error: psql is not installed"
        exit 1
    fi
}

run_script() {
    # Run a SQL script
    psql -U "$DATABASE_USER" -d "$DATABASE_NAME" -f "$1"
}

# ========================================
# Main Execution
# ========================================
echo "Starting [script purpose]..."
check_prerequisites

echo "Creating database..."
# Commands here

echo "Done!"
```

### Bash Best Practices
```bash
# ✓ Use quotes around variables
echo "Database: $DATABASE_NAME"  # Good
echo Database: $DATABASE_NAME   # Risky

# ✓ Use ${} for clarity
echo "User: ${DB_USER}"

# ✓ Use meaningful variable names
BACKUP_PATH="/backups/"  # Good
BP="/backups/"           # Avoid

# ✓ Check for errors
if ! command -v psql &> /dev/null; then
    echo "Error: psql not found"
    exit 1
fi

# ✓ Provide helpful output
echo "Starting database backup..."
# ... commands ...
echo "Backup completed successfully!"

# ✓ Exit with proper codes
exit 0  # Success
exit 1  # Error
```

---

## JavaScript/Node.js Standards (if applicable)

### Formatting
```javascript
// File header
/**
 * [File purpose]
 * Course: [Course Name]
 * Day: [X]
 */

// Indentation: 2 spaces
// Naming: camelCase for variables, UPPER_CASE for constants

const DATABASE_URL = process.env.DATABASE_URL;
const MAX_CONNECTIONS = 10;

// Function naming: descriptive verbs
function connectToDatabase() {
    // Implementation
}

// Variable naming: descriptive nouns
const userData = {};
const customerEmail = "customer@example.com";
```

### Code Organization
```javascript
// 1. Imports at the top
const express = require('express');
const { Pool } = require('pg');

// 2. Configuration
const pool = new Pool({
    connectionString: process.env.DATABASE_URL
});

// 3. Helper functions
function formatResponse(data) {
    return { success: true, data };
}

// 4. Route handlers
app.get('/customers', async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM customers');
        res.json(formatResponse(result.rows));
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// 5. Server startup
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

---

## Python Standards (if applicable)

### Formatting
```python
# File header
"""
[File purpose]
Course: [Course Name]
Day: [X]
"""

# Naming conventions
DATABASE_URL = os.getenv('DATABASE_URL')  # Constants: UPPER_CASE
MAX_CONNECTIONS = 10

def connect_to_database():  # Functions: snake_case
    """Connect to PostgreSQL database"""
    pass

customer_data = {}  # Variables: snake_case
customer_email = "customer@example.com"
```

### Code Organization
```python
# 1. Imports
import os
from flask import Flask, jsonify
import psycopg2

# 2. Configuration
DATABASE_URL = os.getenv('DATABASE_URL')
DEBUG = os.getenv('DEBUG', False)

# 3. Initialize app
app = Flask(__name__)

# 4. Helper functions
def format_response(data):
    return {'success': True, 'data': data}

# 5. Route handlers
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers')
        results = cursor.fetchall()
        return jsonify(format_response(results))
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# 6. Server startup
if __name__ == '__main__':
    app.run(debug=DEBUG)
```

---

## Code Quality Checklist

When creating any code file, verify:

### SQL Files
- ✓ Keywords in UPPERCASE
- ✓ Table and column names in lowercase
- ✓ Proper indentation (4 spaces)
- ✓ Comments explain the purpose
- ✓ File header included
- ✓ Examples are practical and realistic
- ✓ Code has been tested and runs without errors
- ✓ Follows naming conventions
- ✓ NULL handling is correct
- ✓ GROUP BY includes all non-aggregated columns

### Shell Scripts
- ✓ Shebang line: `#!/bin/bash`
- ✓ File header with description
- ✓ Comments explain purpose
- ✓ Error checking (`set -e` or `if` statements)
- ✓ Meaningful variable names
- ✓ Clear output messages
- ✓ Proper exit codes
- ✓ Has been tested

### JavaScript/Node.js
- ✓ File header comment
- ✓ Consistent indentation (2 spaces)
- ✓ Meaningful variable names (camelCase)
- ✓ Function names are descriptive verbs
- ✓ Comments explain complex logic
- ✓ Error handling included
- ✓ Code follows your framework's conventions
- ✓ Has been tested

### Python
- ✓ File docstring with purpose
- ✓ PEP 8 compliant (or your chosen style)
- ✓ Meaningful variable names (snake_case)
- ✓ Function docstrings
- ✓ Comments explain complex logic
- ✓ Error handling included
- ✓ Imports organized (stdlib, third-party, local)
- ✓ Has been tested

---

## Consistency Rules

1. **Within a file**: All similar code follows same pattern
2. **Across files**: All SQL files follow same standard
3. **Across repos**: All 3 course repos follow same standards
4. **With examples**: Code files match code shown in documentation

When in doubt, follow the style of existing code in that repository.