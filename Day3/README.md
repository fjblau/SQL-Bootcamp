# Day 3: Advanced Topics and Practical Application

## Learning Objectives
By the end of Day 3, participants will be able to:
- Write complex queries involving multiple tables using various join types
- Create and use subqueries and Common Table Expressions (CTEs)
- Implement database security best practices with roles and permissions
- Build a simple REST API that interacts with a PostgreSQL database
- Apply all SQL knowledge in a practical, real-world context

## Session Content

### Morning Session (9:00 AM - 12:00 PM)

#### Querying Multiple Tables (9:00 - 10:30)
- Deep dive into join operations:
  - INNER JOIN
  - LEFT JOIN
  - RIGHT JOIN
  - FULL OUTER JOIN
  - CROSS JOIN
- Practical examples using our e-commerce database
- Performance considerations when joining tables
- Hands-on exercises with complex join scenarios

#### Embedded Queries (10:45 - 12:00)
- Subqueries in SELECT, FROM, and WHERE clauses
- Correlated vs. non-correlated subqueries
- Common Table Expressions (CTEs)
- Recursive CTEs for hierarchical data
- Performance comparison: joins vs. subqueries
- Practical examples and best practices

### Afternoon Session (1:00 PM - 4:30 PM)

#### Database Security (1:00 - 2:00)
- PostgreSQL security model overview
- Creating and managing roles
- Granting and revoking privileges
- Schema organization for security
- Row-level security introduction
- Password policies and connection security
- Security best practices checklist

#### Mini REST Server Project (2:15 - 4:00)
- REST API concepts and principles
- Setting up a Node.js environment
- Connecting to PostgreSQL with node-postgres
- Implementing CRUD operations:
  - GET (SELECT)
  - POST (INSERT)
  - PUT (UPDATE)
  - DELETE
- Error handling and validation
- Testing the API with Postman/cURL

#### Course Wrap-up (4:00 - 4:30)
- Review of key concepts from all three days
- Additional resources for continued learning
- Q&A session
- Course evaluation and feedback

## Files in this Directory

- `README.md` - This overview document
- `advanced_joins.sql` - Examples and exercises for various join types
- `subqueries_ctes.sql` - Examples and exercises for subqueries and CTEs
- `database_security.sql` - Role and permission management examples
- `rest_api_project/` - Directory containing the REST API project files
  - `README.md` - Project setup and instructions
  - `package.json` - Node.js project configuration
  - `server.js` - Main server file
  - `db.js` - Database connection module
  - `routes/` - API route handlers

## Preparation for Further Learning

After completing this bootcamp, consider exploring:
- Advanced PostgreSQL features (triggers, stored procedures, etc.)
- Database performance optimization and indexing strategies
- NoSQL databases and when to use them
- Data warehousing concepts
- Business intelligence and data visualization tools
- Database administration and maintenance
- Cloud-based database services (AWS RDS, Azure SQL, etc.)