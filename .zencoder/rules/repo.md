---
description: Repository Information Overview
alwaysApply: true
---

# SQL Bootcamp Course Materials Information

## Summary
This repository contains comprehensive course materials for a 3-day SQL Bootcamp using PostgreSQL. The materials are organized by day, with each day focusing on different aspects of SQL and database management. The course progresses from basic database concepts to advanced SQL queries and practical application with a REST API.

## Structure
- **Day1/**: Foundations of Relational Databases
- **Day2/**: SQL Queries and Database Management
- **Day3/**: Advanced Topics and Practical Application
- **syllabus.md**: Complete course outline with schedule and topics
- **description.txt**: Brief course description

## Language & Runtime
**Languages**: SQL (PostgreSQL), Bash, JavaScript (Node.js), Python
**SQL Version**: PostgreSQL (compatible with version 12+)
**JavaScript Runtime**: Node.js (v14+ recommended for Day 3)
**Python Runtime**: Python 3.8+ (alternative for Day 3 REST API)
**Package Managers**: npm (Node.js), pip (Python)

## Dependencies
**Main Dependencies**:
- PostgreSQL database server (v12+)
- pgAdmin (GUI tool for PostgreSQL)

**JavaScript Dependencies (Day 3)**:
- Node.js (v14+)
- Express.js, pg, cors, dotenv

**Python Dependencies (Day 3)**:
- Python (3.8+)
- Flask, psycopg2, python-dotenv, Flask-CORS

## Course Content

### Day 1: Foundations of Relational Databases
**Main Files**:
- `README.md`: Day overview and learning objectives
- `installation_guide.sh`: PostgreSQL installation instructions
- `first_database.sql`: Basic database creation and operations
- `data_types_reference.md`: PostgreSQL data types reference

### Day 2: SQL Queries and Database Management
**Main Files**:
- `README.md`: Day overview and learning objectives
- `pgadmin_guide.md`: pgAdmin installation and usage guide
- `sample_database.sql`: E-commerce database creation script
- `basic_queries.sql`: SELECT statements and filtering
- `data_manipulation.sql`: INSERT, UPDATE, DELETE operations
- `advanced_queries.sql`: Aggregate functions, JOINs, GROUP BY

### Day 3: Advanced Topics and Practical Application
**Main Files**:
- `README.md`: Day overview and learning objectives
- `advanced_joins.sql`: Complex join operations
- `subqueries_ctes.sql`: Subqueries and Common Table Expressions
- `database_security.sql`: Role and permission management
- `rest_api_project/`: REST API connecting to PostgreSQL
  - **JavaScript Version**: Node.js with Express.js (default)
  - **Python Version**: Flask framework (in `python_version/` directory)
  - Both versions provide identical functionality and endpoints

## REST API Project
Students can choose between two implementations:

### JavaScript Version
**Configuration File**: `package.json`
**Framework**: Express.js
**Build & Installation**:
```bash
cd Day3/rest_api_project
npm install
npm start
```

### Python Version
**Configuration File**: `requirements.txt`
**Framework**: Flask
**Build & Installation**:
```bash
cd Day3/rest_api_project/python_version
pip install -r requirements.txt
python server.py
```

Both versions provide identical API endpoints and functionality.

## Usage & Operations
**PostgreSQL Setup**:
```bash
# Run installation script
chmod +x Day1/installation_guide.sh
./Day1/installation_guide.sh
```

**Database Creation**:
```bash
# Create sample e-commerce database
psql -U postgres -f Day2/sample_database.sql
```

**Running Queries**:
```bash
# Run through pgAdmin or psql
psql -U postgres -d ecommerce -f Day2/basic_queries.sql
```