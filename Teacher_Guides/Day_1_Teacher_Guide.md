# SQL Bootcamp: Day 1 Teacher's Guide
## Foundations of Relational Databases

---

## Table of Contents
1. [Overview & Learning Objectives](#overview--learning-objectives)
2. [Pre-Class Requirements & Setup](#pre-class-requirements--setup)
3. [Daily Schedule & Pacing Guide](#daily-schedule--pacing-guide)
4. [Morning Session: Database Fundamentals (9:00 AM - 12:00 PM)](#morning-session-database-fundamentals)
5. [Afternoon Session: Installation & Hands-On (1:00 PM - 4:30 PM)](#afternoon-session-installation--hands-on)
6. [Assignments & Exercises](#assignments--exercises)
7. [Teaching Tips & Common Pitfalls](#teaching-tips--common-pitfalls)
8. [Troubleshooting Guide](#troubleshooting-guide)
9. [Assessment & Completion Checklist](#assessment--completion-checklist)
10. [Resources & Reference Materials](#resources--reference-materials)

---

## Overview & Learning Objectives

### Course Context
Day 1 is the foundation of the 3-day SQL Bootcamp. Students arrive with varying levels of database experience—some may have touched SQL before, others are completely new. Your role is to build confidence alongside competence, establishing a shared vocabulary and conceptual foundation that makes Days 2-3 accessible.

### Primary Learning Objectives
By the end of Day 1, students will be able to:

1. **Understand relational database concepts** and articulate why databases are essential in modern applications
2. **Identify entities, attributes, and relationships** in a business scenario
3. **Recognize the differences** between DDL, DML, DCL, and TCL SQL commands
4. **Explain primary keys and foreign keys** and their role in data integrity
5. **Describe database normalization** concepts (1NF, 2NF, 3NF) at a conceptual level
6. **Successfully install PostgreSQL** on their operating system (macOS, Windows, or Linux)
7. **Connect to PostgreSQL** using both command-line (psql) and GUI tools
8. **Create their first database and tables** using SQL DDL statements
9. **Execute basic insert and select queries** to validate their setup

### Bloom's Taxonomy Alignment
- **Remember**: SQL command categories, data types, PostgreSQL terminology
- **Understand**: Relationships between tables, normalization principles, why databases organize data
- **Apply**: Installing software, creating tables, writing basic SQL
- **Analyze**: Identifying entities and relationships in a business case
- **Evaluate**: Assessing data type choices for different scenarios

---

## Pre-Class Requirements & Setup

### System Requirements - Instructor Setup (Complete Before Day 1)

**Hardware:**
- Instructor machine with adequate display capability (projector/screen sharing)
- Backup laptop with PostgreSQL installed in case of technical issues
- Stable internet connection (for downloading PostgreSQL if needed)

**Software:**
- PostgreSQL 12+ installed and running (verified before class)
- pgAdmin 4 installed (for GUI demonstrations)
- A text editor or IDE (VS Code, Sublime Text, or similar)
- Terminal/Command Prompt access with ability to run commands
- Optional: psql command-line history/examples prepared

**Preparation Timeline:**
- **1 Week Before**: Test installation scripts on multiple OS (at least one Mac, one Windows, one Linux if possible)
- **3 Days Before**: Verify all teaching materials are accessible, SQL files execute without error
- **1 Day Before**: Do a complete dry-run of the installation process on a clean machine
- **Morning Of**: Boot up demo system, verify PostgreSQL is running, test all commands

### Student Prerequisites - Communicate Before Class

Students should arrive with:
- A laptop (Mac, Windows, or Linux)
- Administrator/sudo access to install software
- Internet access (for downloading PostgreSQL)
- No prior database experience required—but SQL exposure is helpful
- Willingness to troubleshoot technical issues collaboratively

### Pre-Class Checklist

**Two Weeks Before:**
- [ ] Send students system requirements email
- [ ] Create installation guide tailored to your environment
- [ ] Test `installation_guide.sh` on representative systems
- [ ] Prepare PostgreSQL download links with correct versions

**One Week Before:**
- [ ] Dry-run all exercises on a clean machine
- [ ] Verify `first_database.sql` executes without errors
- [ ] Create a backup of all materials (USB drive)
- [ ] Prepare slides covering Day 1 topics

**Day Before:**
- [ ] Boot demo machine, verify PostgreSQL service is running
- [ ] Test psql command-line connection
- [ ] Open pgAdmin and verify it's functional
- [ ] Ensure projector/screen sharing works
- [ ] Have backup connection methods (WiFi hotspot, etc.)

**Morning Of:**
- [ ] Arrive 30 minutes early
- [ ] Test database creation with `first_database.sql`
- [ ] Verify network connectivity
- [ ] Have IT support contact info readily available
- [ ] Test backup demo machine

---

## Daily Schedule & Pacing Guide

### Overall Day Structure

```
9:00 AM - 9:15 AM      Welcome & Course Overview (15 min)
9:15 AM - 9:45 AM      Introduction to Databases (30 min)
9:45 AM - 10:45 AM     Relational Concepts & Design (60 min)
10:45 AM - 11:00 AM    BREAK (15 min)
11:00 AM - 12:00 PM    SQL Language Categories & DDL (60 min)

12:00 PM - 1:00 PM     LUNCH

1:00 PM - 1:15 PM      Afternoon Introductions & Recap (15 min)
1:15 PM - 2:30 PM      PostgreSQL Installation Workshop (75 min)
2:30 PM - 2:45 PM      BREAK (15 min)
2:45 PM - 4:15 PM      Hands-On: First Database Creation (90 min)
4:15 PM - 4:30 PM      Wrap-Up & Day 1 Checkout (15 min)
```

**Total Instruction Time**: 6.5 hours (with breaks)  
**Total Active Learning Time**: 5 hours

### Timing Notes & Flexibility

- **Installation is the most time-variable element**: Some students will finish in 5 minutes, others may need 45 minutes. Have support for both advanced and struggling students.
- **Build in 10-15% buffer time** for questions and unexpected delays
- **Afternoon moves faster** because installation is done; hands-on work accelerates understanding
- **If running behind**, defer the normalization deep-dive to tomorrow; ensure everyone has a working database connection

---

## Morning Session: Database Fundamentals

### 9:00 AM - 9:15 AM: Welcome & Course Overview (15 minutes)

**Instructor Delivery Method**: Presentation + Interactive Discussion

**Content to Cover:**
- Warm welcome; learn students' names and background (1 minute)
- Course goals: "By the end of Day 3, you'll have queried databases, built an API, and understood real-world SQL patterns" (2 minutes)
- Why databases matter: 
  - Every application uses databases (social media, banking, e-commerce, healthcare)
  - SQL is the universal language for database access
  - These skills are immediately employable (2 minutes)
- Daily themes overview:
  - Day 1: Foundations & Installation
  - Day 2: Queries & Data Manipulation
  - Day 3: Advanced Queries & Building an API (2 minutes)
- House-keeping: breaks, lunch, restroom, questions encouraged (3 minutes)
- Set expectations: "This is a bootcamp—we move quickly, but nobody gets left behind" (2 minutes)

**Interactive Element**: 
- Ask: "Who's used Excel or Google Sheets?" (most will say yes)
- Say: "Databases are like mega-powered spreadsheets. Today you'll understand why" (engage prior knowledge)

**Slide/Visual Support**: 
- Title slide with course name and dates
- Simple graphic showing how databases connect to apps
- Visual agenda for the day

---

### 9:15 AM - 9:45 AM: Introduction to Databases (30 minutes)

**Learning Objective**: Students understand why databases exist and how they differ from other data storage.

**Instructor Delivery**: Presentation + Examples

**Key Concepts to Present:**

**1. What is a Database? (5 minutes)**
- Definition: "An organized collection of structured data stored and accessed electronically"
- Analogy: "A library is a database. Books are records, card catalog is the index, librarian is the database engine"
- Modern databases are optimized for: speed, reliability, concurrent access, data integrity

**2. Why Not Use Spreadsheets? (5 minutes)**

Show this comparison on screen:

| Aspect | Spreadsheet | Database |
|--------|-------------|----------|
| **Users** | 1-2 simultaneous | Thousands simultaneously |
| **Data Size** | Megabytes | Terabytes+ |
| **Relationships** | Duplicated data | Related via keys |
| **Speed** | Seconds (slow) | Milliseconds (fast) |
| **Integrity** | Manual validation | Automatic enforcement |
| **Queries** | Sort/filter only | Complex questions |

**Real-world examples**:
- Amazon has billions of products—spreadsheet would crash
- Bank needs to process thousands of transactions/second—spreadsheets can't
- Uber needs real-time updates from thousands of drivers—databases handle this

**3. Types of Databases (3 minutes)**
- Relational (SQL): Most common, what we're learning (95% of enterprise)
- NoSQL: Document-based (MongoDB), Key-value (Redis), Graph (Neo4j)
- For this bootcamp: **We focus on relational (PostgreSQL)**

**4. What is PostgreSQL? (2 minutes)**
- Definition: "An open-source relational database management system (RDBMS)"
- Why PostgreSQL? 
  - Free and open-source
  - Industry-standard for learning and enterprise use
  - Powerful, reliable, widely used
  - Skills transfer to MySQL, SQL Server, Oracle

**Activities**:
- Show a simple table on screen (contacts: first_name, last_name, email)
- Ask: "What questions could we ask this table?" (Guide them toward SELECT queries)

**Visual/Slides**:
- Diagram of data hierarchy: Database → Tables → Rows → Columns
- Screenshot of pgAdmin showing a real database
- Timeline: SQL created 1974, PostgreSQL created 1989, still dominant

---

### 9:45 AM - 10:45 AM: Relational Concepts & Design (60 minutes)

**Learning Objectives**: 
- Students understand tables, rows, columns, and relationships
- Students can identify entities in a business scenario
- Students recognize the need for primary and foreign keys

**Instructor Delivery**: Presentation + Interactive Case Study + Whiteboard Activity

**Content Structure:**

**PART 1: Core Relational Concepts (20 minutes)**

**1. Tables, Rows, and Columns (5 minutes)**

Draw on board or show visualization:
```
TABLE: customers

| customer_id | first_name | last_name  | email              |
|-------------|------------|------------|-------------------|
| 1           | John       | Doe        | john@example.com  | ← ROW (Record)
| 2           | Jane       | Smith      | jane@example.com  |
| 3           | Bob        | Johnson    | bob@example.com   |
      ↑           ↑            ↑            ↑
    COLUMN NAMES (Attributes)
```

Key terminology:
- **Table**: Collection of related data (like a spreadsheet sheet)
- **Row/Record**: Single entry (like one line in a spreadsheet)
- **Column/Attribute**: Property of the record (like a column header)
- **Cell**: Single data value

Example: In the customers table above:
- Row 1: customer_id=1, first_name="John", last_name="Doe", email="john@example.com"
- Column 3 (last_name): "Doe", "Smith", "Johnson"

**2. Data Integrity: Constraints (5 minutes)**

Introduce constraints with real-world reasoning:
- **NOT NULL**: "A customer must have a first name"
- **UNIQUE**: "No two customers can have the same email"
- **PRIMARY KEY**: "Each customer needs a unique ID for identification"
- **DEFAULT**: "If we don't record a sign-up time, use 'now'"

Example from their life: A driver's license must have a unique number (PRIMARY KEY), must have a name (NOT NULL), and no two people have the same license number (UNIQUE).

**3. Relationships Between Tables (10 minutes)**

This is crucial. Use the Orders scenario:

**One-to-Many Relationship** (most common):
- One CUSTOMER can place many ORDERS
- One ORDER belongs to exactly one CUSTOMER

Visualize:
```
CUSTOMERS (1)          ORDERS (Many)
┌──────────┐          ┌──────────────┐
│ Cust_ID  │ ─────→   │ Order_ID     │
│ Name     │ 1     M  │ Customer_ID* │ ← Foreign Key
└──────────┘          │ Amount       │
                      └──────────────┘

One customer (ID=5) can have many orders (Order_ID 101, 102, 103...)
```

**One-to-One Relationship**:
- One PERSON has one SOCIAL_SECURITY_NUMBER (uncommon in databases)

**Many-to-Many Relationship**:
- Many STUDENTS attend many COURSES
- Requires a junction table: ENROLLMENTS

Show all three types with simple diagrams.

**PART 2: Primary Keys & Foreign Keys (15 minutes)**

**Primary Key (PK):**
- Uniquely identifies each row in a table
- Cannot be NULL
- Usually an integer that auto-increments (SERIAL)
- Example: `customer_id` in customers table

**Foreign Key (FK):**
- Points to a Primary Key in another table
- Maintains referential integrity
- Example: In orders table, `customer_id` is a Foreign Key pointing to customers.customer_id

Demonstrate referential integrity:
- "If I delete customer #5, what happens to their orders?"
- Options: DELETE CASCADE (delete orders too), RESTRICT (don't delete customer), SET NULL (orphan orders)
- This is why relationships matter: data consistency

Analogy: "A foreign key is like a reference to another document. If the original is destroyed, the reference becomes invalid."

**Activity: Whiteboard Exercise (10 minutes)**

Present scenario: "An e-commerce company sells products to customers."

Ask students (breakout into pairs):
1. What entities (tables) do we need?
2. What attributes does each entity have?
3. What's the relationship between them?

Expected answer:
- Entities: CUSTOMERS, PRODUCTS, ORDERS, ORDER_ITEMS
- Relationships: CUSTOMER → ORDERS (1:M), PRODUCTS → ORDER_ITEMS (1:M), ORDERS → ORDER_ITEMS (1:M)

Go to whiteboard and draw with the class. Celebrate good answers. Fill in any gaps.

**Visual Aids**:
- Entity-Relationship diagram (ER diagram) showing customers, orders, products
- Sample table with PK highlighted in blue, FK in red
- Screenshot of referential integrity error in PostgreSQL

---

### 10:45 AM - 11:00 AM: BREAK (15 minutes)

---

### 11:00 AM - 12:00 PM: SQL Language Categories & DDL (60 minutes)

**Learning Objectives**:
- Students understand the four categories of SQL commands
- Students can write simple CREATE TABLE statements
- Students recognize DDL as the tool for database structure

**Instructor Delivery**: Presentation + Live Coding + Guided Practice

**Content:**

**PART 1: SQL Command Categories (15 minutes)**

Present the four types with clear explanations and examples:

**1. DDL (Data Definition Language) - Structure**
- Purpose: Define/modify database structure
- Commands: CREATE, ALTER, DROP, TRUNCATE
- Example: `CREATE TABLE customers (customer_id SERIAL PRIMARY KEY, name VARCHAR(50))`
- When used: "I'm creating a new table" or "I want to add a column"

**2. DML (Data Manipulation Language) - Data**
- Purpose: Work with data inside structures
- Commands: SELECT, INSERT, UPDATE, DELETE
- Example: `INSERT INTO customers VALUES (1, 'John')`
- When used: "I want to add/change/view data"

**3. DCL (Data Control Language) - Permissions**
- Purpose: Grant/revoke access rights
- Commands: GRANT, REVOKE
- Example: `GRANT SELECT ON customers TO read_user`
- When used: "User XYZ should only be able to read data, not modify it"

**4. TCL (Transaction Control Language) - Safety**
- Purpose: Manage transactions (all-or-nothing operations)
- Commands: COMMIT, ROLLBACK, SAVEPOINT
- Example: "Transfer $100 from John's account to Jane's account—both changes happen or neither do"
- When used: "I need multiple operations to succeed together or fail together"

**Teaching Tip**: Use analogy: "DDL is like creating a filing system, DML is filing papers, DCL is setting access to the files, TCL is undoing mistakes."

Create a visual table on screen:

| Category | Purpose | Commands | Example |
|----------|---------|----------|---------|
| DDL | Structure | CREATE, ALTER, DROP | `CREATE TABLE...` |
| DML | Data | SELECT, INSERT, UPDATE, DELETE | `INSERT INTO...` |
| DCL | Permissions | GRANT, REVOKE | `GRANT SELECT...` |
| TCL | Transactions | COMMIT, ROLLBACK | `ROLLBACK;` |

**PART 2: Data Types Overview (15 minutes)**

Show the data_types_reference.md document on screen. Focus on most common types students will use in Day 2:

**Essential Types for Day 1**:

| Type | Use Case | Example |
|------|----------|---------|
| SERIAL | Auto-incrementing IDs | `product_id SERIAL PRIMARY KEY` |
| INTEGER | Whole numbers | `quantity INTEGER` |
| VARCHAR(n) | Text with max length | `first_name VARCHAR(50)` |
| TEXT | Unlimited text | `description TEXT` |
| DATE | Dates | `created_at DATE` |
| TIMESTAMP | Date & time | `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP` |
| BOOLEAN | True/False | `is_active BOOLEAN DEFAULT true` |
| NUMERIC(p,s) | Money | `price NUMERIC(10,2)` |

**Why choose one over another?**
- INTEGER for IDs (standard, fast)
- VARCHAR with limit for names/emails (predictable size)
- TEXT for comments (unlimited, okay with size)
- NUMERIC for money (precise, not REAL or DOUBLE)
- TIMESTAMP for "when" tracking (auditing, sorting)

**PART 3: CREATE TABLE Syntax (15 minutes) - Live Coding**

Live demo: Write a CREATE TABLE statement on screen as you explain:

```sql
CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Walk through each line:
- `CREATE TABLE contacts (` — Start definition
- `contact_id SERIAL PRIMARY KEY` — Unique ID, auto-increments
- `first_name VARCHAR(50) NOT NULL` — Text up to 50 chars, required
- `email VARCHAR(100) UNIQUE` — Text up to 100 chars, no duplicates
- `phone VARCHAR(20)` — Optional (no NOT NULL)
- `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP` — Automatically records when row was inserted
- `);` — End definition

**Common Mistakes** (address these now to prevent tomorrow's headaches):
- Forgetting NOT NULL on required fields → accepts blank data you didn't intend
- Making UNIQUE field too large → slow queries
- Not having a PRIMARY KEY → can't identify specific rows reliably
- Using VARCHAR without a number → defeats the purpose

**PART 4: Guided Practice (15 minutes)**

Project the following scenario on screen:

"Design a table for storing book information in a library. Books have:
- A unique ID
- Title (required, up to 200 characters)
- Author name (required)
- ISBN (unique, up to 20 characters)
- Publication year (year only)
- Number of pages
- Date added to library

Write the CREATE TABLE statement."

Give students 5 minutes to work individually or in pairs. Then go through a solution together:

```sql
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    publication_year INTEGER,
    pages INTEGER,
    date_added DATE DEFAULT CURRENT_DATE
);
```

Discuss choices:
- Why SERIAL for book_id? (unique, standard for IDs)
- Why VARCHAR(200) for title? (titles can be long but not unlimited)
- Why UNIQUE on ISBN? (each book has one ISBN)
- Why VARCHAR for author not TEXT? (author names fit in 100 chars easily)

**Wrap-Up (5 minutes)**
- DDL creates structure
- Data types must be chosen carefully
- Primary keys and constraints maintain data integrity
- Next: Install PostgreSQL and create your first real database!

---

## Afternoon Session: Installation & Hands-On

### 1:00 PM - 1:15 PM: Afternoon Recap & Transition (15 minutes)

**Objective**: Refresh minds after lunch, re-establish momentum, address morning questions

**Content**:
- Quick recap: "This morning we learned databases organize data with tables, relationships, and rules. Now we install the actual tool."
- "Everyone should have attempted installation before class—show of hands?" (be ready for mixed results)
- Walk through what's about to happen: "We'll install PostgreSQL together, everyone gets a working database, then we create your first tables"
- Logistics: "There will be a few hiccups. That's normal. We troubleshoot together."
- Reminder: "Two key tools: psql (command-line) and pgAdmin (visual interface). Today you'll use both."

**Engagement**: Gauge the room's energy. If slower after lunch, inject enthusiasm: "This is where theory meets practice!"

---

### 1:15 PM - 2:30 PM: PostgreSQL Installation Workshop (75 minutes)

**Objective**: Every student has PostgreSQL running, can connect to it, and understands the basic tools.

**Instructor Approach**: Guided workshop—you lead, students follow at own pace, support as needed.

**Pre-Installation Checklist (5 minutes)**

Before students touch anything, verify:
1. Everyone has admin/sudo access on their machine
2. Everyone has a text editor open for notes
3. Everyone has your installation guide handy (physical handout or screen-shared)
4. Establish support pattern: "Raise your hand when stuck; I'll come over or screen-share"

**Installation by OS (50 minutes total)**

**Windows Installation (Show on Projector)**
1. Visit https://www.postgresql.org/download/windows/
2. Download latest stable version (PostgreSQL 14+)
3. Run installer
4. **Key screen**: Choose password for 'postgres' user—**write this down!**
5. Uncheck pgAdmin if not needed (optional)
6. Click "Finish"
7. Wait for installation (5-10 minutes)

**Verification for Windows**:
- Open Command Prompt
- Type: `psql -U postgres`
- Should prompt for password (enter what you set)
- Should show `postgres=#` prompt (success!)

**macOS Installation (Show on Projector)**

Option A: Homebrew (easiest if Homebrew installed)
```bash
brew install postgresql
brew services start postgresql
psql -U postgres  # May not need password
```

Option B: Download installer from postgresql.org (alternative)
1. Download macOS installer
2. Run .dmg file
3. Follow installer
4. Same password prompt as Windows

**Verification for macOS**:
```bash
psql -U postgres
# Should show postgres=# prompt
```

**Linux (Ubuntu/Debian) - Show Terminal**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql  # Usually starts automatically
sudo -u postgres psql  # Connect as postgres user
```

**Verification for Linux**:
- Should show `postgres=#` prompt

**Key Talking Points During Installation**:
- The password you choose for 'postgres' is critical—write it down immediately
- Installation takes 5-15 minutes depending on system
- PostgreSQL runs as a background service—you don't need to start it each time
- `postgres` is the administrative user; you'll eventually create project users
- psql is the command-line tool; pgAdmin is the visual tool

**After Installation: First Connection (10 minutes)**

Everyone should now see the `postgres=#` prompt in their terminal/command prompt.

**Live Demo**: Show your screen connecting to PostgreSQL:
```bash
$ psql -U postgres
Password for user postgres: [you type password]
psql (14.2 (Debian 14.2-1.pgdg110+1~bpo11+1), server 14.2)
Type "help" for help.

postgres=# 
```

**Teach Basic psql Commands** (show on screen as you type):

```sql
postgres=# \l          -- List all databases
postgres=# \dt         -- List all tables in current database
postgres=# \?          -- Help
postgres=# \q          -- Quit
postgres=# \c dbname   -- Connect to database dbname
postgres=# SELECT version();  -- Show PostgreSQL version
```

**Activity**: Have students type these commands. Wait for everyone to see results. Troubleshoot individually as needed.

**Support Strategy for Installation Issues**:
- **"command not found" error**: Usually PATH not set. On Windows, restart Command Prompt. On Mac/Linux, verify installation completed.
- **"password authentication failed"**: They entered wrong password. Use `psql -U postgres` and try again.
- **Permission denied (sudo)**: They might not have admin access. Escalate to IT if needed.
- **Port 5432 already in use**: Another PostgreSQL instance is running. Unlikely but possible—usually not an issue for bootcamp.

**Backup Plan**: 
- If a student's installation fails completely, they can pair with a neighbor for hands-on exercises
- Provide instructions for installing at home later
- Focus on understanding concepts; installation can be sorted out

---

### 2:30 PM - 2:45 PM: BREAK (15 minutes)

---

### 2:45 PM - 4:15 PM: Hands-On - First Database Creation (90 minutes)

**Objective**: Students execute SQL DDL statements, see databases and tables created, understand the connection between theory and reality.

**Instructor Delivery**: Guided live coding + Student practice + Troubleshooting

**PART 1: Walkthrough of first_database.sql (15 minutes)**

Open the file on projector and walk through it line-by-line. Explain what each section does:

```sql
-- 1. Create a new database
CREATE DATABASE bootcamp_db;
```
- This DDL statement creates a new database named "bootcamp_db"
- You'll connect to this database for all Day 1 work

```sql
-- 2. Connect to the new database
-- \c bootcamp_db
```
- This psql command (\c) connects to the database
- psql commands start with backslash; SQL statements don't

```sql
-- 3. Create a simple table for storing contacts
CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
- This is the DDL you learned this morning
- contact_id is the PRIMARY KEY (unique, auto-incrementing)
- first_name and last_name are required
- email must be unique (no two contacts with same email)
- created_at automatically records when the row is inserted

```sql
-- 4. Add some sample data
INSERT INTO contacts (first_name, last_name, email, phone)
VALUES 
    ('John', 'Doe', 'john.doe@example.com', '555-123-4567'),
    ('Jane', 'Smith', 'jane.smith@example.com', '555-987-6543'),
    ('Bob', 'Johnson', 'bob.johnson@example.com', '555-456-7890');
```
- This is DML: inserting data into the table
- Notice: contact_id and created_at are NOT listed—they auto-populate

```sql
-- 5. View the data
SELECT * FROM contacts;
```
- This is DML: SELECT retrieves data
- `*` means "all columns"
- This shows all contacts and all their attributes

Then shows relationships:
```sql
-- 6. Create a second table to demonstrate relationships
CREATE TABLE notes (
    note_id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(contact_id),
    note_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
- notes table has a FOREIGN KEY: `contact_id REFERENCES contacts(contact_id)`
- This creates a relationship: each note belongs to one contact

```sql
-- 8. View notes with contact information (simple join)
SELECT 
    c.first_name,
    c.last_name,
    n.note_text,
    n.created_at
FROM 
    contacts c
JOIN 
    notes n ON c.contact_id = n.contact_id
ORDER BY 
    n.created_at DESC;
```
- This is the first JOIN they'll see
- Combines data from two related tables
- Preview of Day 2 advanced queries

**Key Teaching Points**:
- Show how DDL (CREATE TABLE) defines structure
- Show how DML (INSERT, SELECT) works with the data
- Highlight the Foreign Key relationship
- Show that a JOIN pulls data from multiple tables

**PART 2: Execute first_database.sql Together (30 minutes)**

**Step 1: Create the Database (5 minutes)**

Everyone connects to PostgreSQL:
```bash
psql -U postgres
```

You show on projector, they follow on their machines:
```sql
postgres=# CREATE DATABASE bootcamp_db;
CREATE DATABASE
postgres=# \c bootcamp_db
You are now connected to database "bootcamp_db" as user "postgres".
bootcamp_db=# 
```

Pause: "Everyone connected to bootcamp_db? Give me a thumbs up."

**Step 2: Copy and Paste first_database.sql (10 minutes)**

There are two ways:

**Option A: Copy-paste into psql** (easiest for first time)
- Share the file content on screen or in a document
- Students copy the SQL commands
- Paste into psql
- Hit Enter

**Option B: Run file directly** (faster but more complex)
```sql
bootcamp_db=# \i /path/to/first_database.sql
```
(Students need correct file path—may vary by OS)

**Recommendation**: For Day 1, use copy-paste so everyone sees what's happening. File execution is faster but hides the learning.

**Step 3: Verify Creation (5 minutes)**

After running the script, verify:
```sql
bootcamp_db=# \dt          -- List tables
                 Table "public.contacts"
 Column  |            Type             | Collation | Nullable | Default 
---------+-----------------------------+-----------+----------+---------
 ...

bootcamp_db=# SELECT * FROM contacts;
 contact_id | first_name | last_name  |            email             |     phone     |         created_at         
-----------+----------|------------|-------------------------------+----------+----------------------------
          1 | John       | Doe        | john.doe@example.com          | 555-123-4567  | 2024-01-15 14:32:05.123456
          2 | Jane       | Smith      | jane.smith@example.com        | 555-987-6543  | 2024-01-15 14:32:05.126543
          3 | Bob        | Johnson    | bob.johnson@example.com       | 555-456-7890  | 2024-01-15 14:32:05.128765
(3 rows)
```

**Celebrate**: "You've created your first database and tables!"

**Step 4: Explore with pgAdmin (10 minutes) - Optional but Recommended**

Switch to pgAdmin on projector:
1. Open pgAdmin
2. Show Server → Databases → bootcamp_db
3. Expand: Tables → contacts
4. Right-click contacts, select "View/Edit Data" → "All Rows"
5. Show the same three contacts in a visual table

**Point out**: "This is the same data you see in psql, but in a nice visual interface. Both tools do the same thing."

Let students explore: "Open pgAdmin and find your bootcamp_db. Click around, see what you can find."

**PART 3: Guided Exercise - Create Your Own Table (25 minutes)**

Present scenario on screen:

**"You're building a contact management system for a team. You need to track:
- Team member ID (unique, auto-increment)
- Full name (required)
- Job title
- Department
- Start date
- Is currently active (yes/no)

Write a CREATE TABLE statement called `team_members`. Think about:
1. What columns do you need?
2. What data types for each?
3. What constraints (NOT NULL, UNIQUE, PRIMARY KEY)?
4. Any DEFAULT values?"**

Students work in pairs or individually for 10 minutes.

**Sample Solution** (reveal after they work):
```sql
CREATE TABLE team_members (
    member_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    job_title VARCHAR(100),
    department VARCHAR(100),
    start_date DATE,
    is_active BOOLEAN DEFAULT true
);
```

**Discuss Design Choices**:
- Why SERIAL for member_id? (standard for IDs)
- Why NOT NULL for full_name? (essential info)
- Why VARCHAR(100) for name? (names rarely exceed 100 chars, good performance)
- Why BOOLEAN for is_active? (only two states)
- Why DEFAULT true? (assume new hires are active)

Have students: **Actually create this table in their bootcamp_db**
```sql
CREATE TABLE team_members (
    ...
);
```

Then verify:
```sql
\dt  -- Should show team_members table
\d team_members  -- Show table structure
```

**PART 4: Insert and View Data (10 minutes)**

Now insert sample data:
```sql
INSERT INTO team_members (full_name, job_title, department, start_date)
VALUES 
    ('Alice Johnson', 'Senior Developer', 'Engineering', '2023-01-15'),
    ('Bob Smith', 'Product Manager', 'Product', '2023-06-01'),
    ('Carol White', 'Designer', 'Design', '2024-01-10');
```

View it:
```sql
SELECT * FROM team_members;
```

Result:
```
 member_id |   full_name   |  job_title  | department |  start_date  | is_active 
-----------+---------------+-------------+------------+--------------+-----------
          1 | Alice Johnson | Senior Dev. | Engineering| 2023-01-15   | true
          2 | Bob Smith     | Product Mgr | Product    | 2023-06-01   | true
          3 | Carol White   | Designer    | Design     | 2024-01-10   | true
```

**Celebrate Again**: "You've created a table from scratch and populated it. That's real database work!"

---

### 4:15 PM - 4:30 PM: Wrap-Up & Day 1 Checkout (15 minutes)

**Objectives**: Reinforce learning, preview Day 2, check for confidence gaps, assign prep work

**Content:**

**1. Recap What We Covered (3 minutes)**
- This morning: Database concepts, tables, relationships, primary/foreign keys, SQL language types
- This afternoon: Installed PostgreSQL, created your first database, understood DDL

**2. Key Takeaways (2 minutes)**
- Databases organize data in tables with relationships
- SQL has four types: DDL (structure), DML (data), DCL (permissions), TCL (transactions)
- Primary keys uniquely identify rows; foreign keys relate tables
- PostgreSQL is the tool; psql and pgAdmin are your interfaces

**3. Preview Day 2 (2 minutes)**
- Tomorrow: Writing queries (SELECT statements)
- We'll ask questions of the data: "Show me all customers from California" or "What's the average order amount?"
- You'll learn JOINs, filtering, sorting, aggregation
- Brings the structure you created today to life with questions

**4. Day 1 Completion Checklist - Verify Everyone** (3 minutes)

Go through this list verbally or on screen:

- [ ] PostgreSQL installed and running
- [ ] Can connect to PostgreSQL (psql -U postgres works)
- [ ] bootcamp_db database created
- [ ] contacts and notes tables exist
- [ ] Can see data with SELECT queries
- [ ] Understand the difference between DDL, DML, DCL, TCL
- [ ] Can explain primary keys and foreign keys
- [ ] pgAdmin installed (optional but recommended)

"Raise your hand if you're missing any of these. We'll sort it out now or I'll email instructions."

**5. Homework / Prep for Day 2 (2 minutes)**
- **Do**: Review the `data_types_reference.md` file (5 minutes)
- **Do**: Review the `first_database.sql` script and understand each line
- **Optional**: Try creating another table on your own (department_info table for departments)
- **Review**: Skim Day 2 README—no pressure, just familiarization

**6. Open Q&A (3 minutes)**
- "What questions do you have before we wrap?"
- Encourage students to ask anything, no question is too basic
- Have IT contact info for anyone with at-home setup issues

**7. Logistics for Day 2**
- Same time tomorrow (9:00 AM)
- Bring your laptop (don't forget!)
- Bring any questions that came up at home
- We'll hit the ground running with queries

**Final Note**: "Great work today. Database fundamentals are the hardest part to learn. Once you get this, everything else clicks. See you tomorrow!"

---

## Assignments & Exercises

### In-Class Exercises (Graded by Participation/Completion)

**Exercise 1: Database Concept Mapping (9:45 AM - 10:30 AM)**
- **Duration**: 20 minutes (individual work) + 15 min (whole-class discussion)
- **Objective**: Apply database concepts to a business scenario
- **Scenario**: "Design a database for a bookstore. Books are written by authors, books are in categories, customers buy books. Map out: tables, attributes, relationships, primary/foreign keys."
- **Expected Output**: Simple diagram or written list
  - Tables: BOOKS, AUTHORS, CATEGORIES, CUSTOMERS, ORDERS, ORDER_ITEMS
  - Attributes: (students fill in)
  - Relationships: (students identify)
- **Grading**: Check for understanding, correct relationships; 5 points
- **Completion Requirement**: Must participate; no "correct" answer, just thoughtful reasoning

**Exercise 2: Design a Table from Requirements (2:45 PM - 3:15 PM)**
- **Duration**: 20 minutes
- **Objective**: Write CREATE TABLE statement based on requirements
- **Scenario Provided**: See "Hands-On" section above (team_members table)
- **Grading**: 
  - Table created without errors: 3 points
  - Appropriate data types: 3 points
  - Proper constraints (PRIMARY KEY, NOT NULL, UNIQUE): 2 points
  - Sensible DEFAULT values: 2 points
- **Completion Requirement**: Must successfully create table in PostgreSQL

**Exercise 3: Query Your Data (3:15 PM - 3:45 PM)**
- **Duration**: 15 minutes
- **Objective**: INSERT data, then SELECT to verify
- **Task**: 
  1. Insert 3-5 sample rows into team_members table
  2. Run SELECT * to view all data
  3. Run SELECT to filter one department
  4. Show instructor or screenshot
- **Grading**: 5 points for correct execution
- **Completion Requirement**: Must see results on their screen

### Take-Home Assignments (Optional Homework)

**Assignment 1: Explore PostgreSQL Documentation (30 minutes)**
- Read: Section on Data Types in PostgreSQL documentation
- Prepare: 2-3 questions about data types you found confusing
- Bring tomorrow: Questions to ask on Day 2

**Assignment 2: Create an Additional Table (Optional, 1 hour)**
- Scenario: You're tracking books in a home library
- Requirements: 
  - Book ID (unique, auto-increment)
  - Title (required)
  - Author (required)
  - Genre
  - Publication year
  - Date added to library
  - Rating (1-5 stars)
- Task: Write CREATE TABLE statement, create table in bootcamp_db
- Bring tomorrow: Screenshot or copy of your CREATE TABLE statement

**Assignment 3: Normalization Study (Optional, 30 minutes)**
- Read: data_types_reference.md (skim)
- Research: Find one example of a poorly normalized database (not in this course)
- Bring tomorrow: One-sentence explanation of why it was poorly designed

### Assessment Methods

**Day 1 Progress Checks**:

1. **Installation verification** (Observable): Everyone connects to PostgreSQL successfully
2. **Table creation** (Hands-on): Students create team_members table without error
3. **Understanding check** (Conceptual): Students can explain primary key vs. foreign key
4. **Query execution** (Technical): Students run SELECT query and see results

**Informal Assessment Throughout Day**:
- Listen for understanding during discussions
- Circulate during exercises; watch for confusion
- Ask probing questions: "Why did you choose SERIAL for this ID?"
- Encourage peer teaching: "Can you explain that to your neighbor?"

**Red Flags to Watch For**:
- Student doesn't understand difference between rows and columns
- Student confused about primary vs. foreign keys
- Installation incomplete (can't connect to PostgreSQL)
- Student silent/withdrawn—may need extra support

**Remediation Strategies**:
- For concept confusion: Use different analogies, draw more diagrams
- For installation issues: Pair with neighbor, continue with lecture, offer post-class support
- For silent students: Direct questions, make it safe to speak up

---

## Teaching Tips & Common Pitfalls

### High-Impact Teaching Strategies

**1. Use Analogies Repeatedly**
Database concepts feel abstract. Anchor to the real world:
- **Table**: Like a spreadsheet sheet
- **Row**: Like one entry in a contact list
- **Primary Key**: Like a driver's license number (unique identifier)
- **Foreign Key**: Like a reference to another document
- **JOIN**: Like stapling two spreadsheets together by matching columns

**2. Show, Don't Tell**
- Live-code everything; don't just talk about it
- Type commands on screen, students follow
- Make mistakes on purpose sometimes, then fix them ("Oops, I forgot the PRIMARY KEY—let me add that")
- Show error messages and how to read them

**3. Build Confidence Early**
- First exercise is easy; let students win
- Celebrate small successes: "Nice, your table created successfully!"
- Normalize struggle: "Installation can be tricky—totally normal to hit a snag"
- Emphasize: "You're learning skills used by millions of developers"

**4. Connect to Student Goals**
- Start class: "By the end of today, you'll have built the foundation for a skill that's on every job posting"
- Link concepts: "This relationship you just designed? Amazon uses this same pattern to track orders"
- Make it real: "Companies hire based on SQL skills. This matters for your career."

**5. Vary Instruction Methods**
- Don't lecture more than 15 minutes without a break or activity
- Mix presentation, discussion, hands-on, pair work
- Use visuals: diagrams, screenshots, live demos
- Engage multiple modalities: see, hear, do

**6. Create Psychological Safety**
- "There are no stupid questions. If you're confused, probably others are too."
- Share your own mistakes: "I once deleted a whole table by accident. Now I always back up first."
- Allow mistakes in exercises: "This is a safe place to fail and learn"
- Normalize different learning speeds: "Some of you already use databases. Some are brand new. Both are fine."

### Common Misconceptions & How to Address Them

**Misconception 1: "Databases are just big spreadsheets"**

**Why it's wrong**: Databases enforce structure, integrity, and relationships in ways spreadsheets can't.

**How to correct**:
- Show the comparison table (Speed, Users, Relationships, etc.)
- Demo: "Let's say I delete a customer. In a spreadsheet, their orders are orphaned data. In a database, I can set it to delete their orders automatically."
- Real consequence: "A spreadsheet can have inconsistent data; a database prevents it."

**Misconception 2: "I should store all data in one table"**

**Why it's wrong**: Data duplication, inability to enforce relationships, hard to update.

**How to correct**:
- Show an example: 100 orders by customer "John Smith" with his address duplicated 100 times
- "If John moves, you'd have to update 100 rows. What if you miss one? With relationships, you update once."
- "Relationships are your friend."

**Misconception 3: "Primary keys and foreign keys are the same thing"**

**Why it's wrong**: Primary key identifies a row in its own table; foreign key is a reference to another table's primary key.

**How to correct**:
- Draw side-by-side:
  ```
  CUSTOMERS table:
  customer_id (PRIMARY KEY) | name
  1                         | John
  
  ORDERS table:
  customer_id (FOREIGN KEY) → points to customers.customer_id
  1                         | Order#101
  ```
- Analogy: "Primary key is your ID; foreign key is your reference to someone else's ID"

**Misconception 4: "VARCHAR should always be unlimited (no length specified)"**

**Why it's wrong**: Unlimited VARCHAR is slow, wastes storage, and defeats input validation.

**How to correct**:
- "Always specify a max length. If it's a name, 100 chars is plenty. Email? 100 chars max."
- "Specifying a length helps catch data entry errors. If an email is longer than 100 chars, something's wrong."

**Misconception 5: "NULL and empty string ('') are the same"**

**Why it's wrong**: NULL means "unknown" or "no value"; empty string is a value (an empty one).

**How to correct**:
- Show a query: `SELECT COUNT(*) FROM customers WHERE email IS NULL` vs. `WHERE email = ''`
- "NULL means we don't know the email. Empty string means we know it, but it's blank. They're different."
- Practical: "If someone hasn't provided an email, use NULL. Don't guess."

### Pacing & Timing Adjustments

**If Running Behind**:
- Skip the detailed normalization forms (1NF, 2NF, 3NF)—mention they exist, save for another course
- Combine break time (reduce break from 15 min to 10 min)
- Defer the "team_members" exercise to homework; focus on concepts
- Drop the pgAdmin demo if short on time (psql is sufficient)

**If Running Ahead**:
- Deepen the normalization discussion (show good vs. bad examples)
- Add another table design exercise
- Introduce ERD software (like dbdiagram.io) for bonus
- Have students explore pgAdmin more thoroughly
- Discuss query optimization basics (preview of Day 2)

**If Installation Takes Longer Than Expected**:
- This is normal. Don't stress.
- While troubleshooting individual machines, have others review the first_database.sql file
- Prioritize getting everyone connected before lunch
- If 2-3 people still have issues, pair them post-day, don't hold up the class
- Have a pre-configured backup VM or Cloud database they can use if installation fails completely

### Motivation & Engagement

**Start with Why**:
- "Real applications: Netflix has databases. Your bank has databases. When you order from Amazon, a database tracks it."
- "In 3 days, you'll be querying real data and building an API. Cool, right?"

**Celebrate Wins**:
- "You've created a database! That's something many people never do."
- "Look at that data in the table—you put that there with a single command."
- "Your bootcamp_db will get more sophisticated each day. Cool progression."

**Make It Relevant**:
- "This skill is on every 'developer jobs' posting"
- "Startups will ask you to build databases; consultants bill thousands for this"
- "Understanding data is power; databases are how real businesses store data"

---

## Troubleshooting Guide

### Pre-Installation Issues

**Issue**: Student forgot to download installer before class
- **Quick Fix**: Have a USB with the installer, or GitHub repo they can clone
- **Prevention**: Email download link 1 week before

**Issue**: Student's laptop is old/underpowered
- **Workaround**: Use Replit.com or similar to run PostgreSQL in browser
- **Alternative**: Pair with another student

**Issue**: Student doesn't have admin access
- **Workaround**: IT provision admin rights (reach out before class)
- **Alternative**: Use cloud database (AWS RDS, or managed service)

### Installation Errors

**Error: "command not found: psql"** (after installation)
- **Cause**: PostgreSQL installed but not in PATH
- **Windows Fix**: Restart terminal/Command Prompt, or add PostgreSQL bin folder to PATH
- **Mac/Linux Fix**: Reinstall with Homebrew or verify install path

**Error: "port 5432 already in use"**
- **Cause**: Another PostgreSQL instance running
- **Fix**: Check if PostgreSQL is already running. If yes, that's fine. If not, check for conflicting service.
- **Usually not a problem** for bootcamp purposes

**Error: "password authentication failed" (at psql -U postgres)**
- **Cause**: Wrong password entered
- **Fix**: Restart psql and re-enter password carefully. If still wrong and you didn't set it, use cloud option.

**Error: "Peer authentication failed" (Linux)**
- **Cause**: PostgreSQL configured to use peer authentication instead of password
- **Fix**: Use `sudo -u postgres psql` instead, or reconfigure pg_hba.conf

### Connection Issues During Workshop

**Issue**: Student connects to PostgreSQL but can't create database
- **Cause**: Not using correct username (should be 'postgres') or don't have permissions
- **Fix**: `psql -U postgres` (explicitly use postgres user)

**Issue**: CREATE DATABASE command doesn't work
- **Cause**: Syntax error (missing semicolon, typo)
- **Fix**: Show error message, check for typos. `CREATE DATABASE bootcamp_db;` (note semicolon)

**Issue**: Can see database in pgAdmin but not in psql**
- **Cause**: Connected to wrong database in psql
- **Fix**: Use `\l` to list databases, `\c bootcamp_db` to connect

### Data & Queries Issues

**Issue**: INSERT statement returns error "duplicate key value"**
- **Cause**: Violating UNIQUE constraint (email already exists)
- **Fix**: Use different email value, or INSERT with ON CONFLICT clause (Day 2 topic)

**Issue**: SELECT returns "permission denied"**
- **Cause**: User doesn't have SELECT permission (unlikely on postgres user, but possible)
- **Fix**: Run query as postgres user: `sudo -u postgres psql -d bootcamp_db`

**Issue**: Table structure looks wrong after creation**
- **Cause**: Typo in CREATE TABLE statement
- **Fix**: `DROP TABLE tablename;` then re-create with correct syntax

### Group Support Strategies

**1. Pair Programming**
- If one student finishes early, have them help a struggling student
- Both learn: peer teaching reinforces concepts

**2. Demonstrate on Their Machine**
- Use screen sharing (Zoom, Teams) to show on their screen while they follow
- More effective than giving verbal directions

**3. Have a "Working Example" Machine**
- Set up one machine perfectly, keep it connected
- Students can compare: "Does your output match the projector screen?"

**4. Create a Troubleshooting Checklist Handout**
- "Can you see postgres=# prompt?" (Y/N) → if N, check installation
- "Can you see bootcamp_db in \l output?" (Y/N) → if N, \c bootcamp_db
- "Does SELECT * FROM contacts; show three rows?" (Y/N)
- Each step is a checkpoint; troubleshoot in order

---

## Assessment & Completion Checklist

### Day 1 Success Criteria

Students successfully complete Day 1 if they:

1. **✓ Software Installation**
   - PostgreSQL installed and running
   - psql command-line tool accessible
   - Can authenticate with `psql -U postgres`

2. **✓ Conceptual Understanding** (checked via discussion)
   - Explain difference between tables and rows
   - Define primary key and foreign key
   - Describe why relationships matter
   - Identify DDL vs. DML commands
   - Recognize appropriate data types for given scenarios

3. **✓ Hands-On Skills**
   - Create a database using SQL
   - Create a table with appropriate columns and constraints
   - Insert data into a table
   - Query data using SELECT
   - Use psql commands (\l, \dt, \d, \c)

4. **✓ Database Creation**
   - bootcamp_db database exists and is accessible
   - contacts table exists with correct structure
   - notes table exists with correct structure and foreign key
   - At least one additional table created (team_members)

### Student Self-Assessment (Provide Handout)

Students fill this out as they leave:

```
Rate your confidence (1=Not confident, 5=Very confident):

1. I understand what a database is and why it's useful      [ ]
2. I can explain primary keys and foreign keys              [ ]
3. I know the difference between DDL and DML                [ ]
4. I successfully installed PostgreSQL                      [ ]
5. I can create a table in PostgreSQL                       [ ]
6. I can insert data and retrieve it with SELECT            [ ]
7. I understand relationships between tables                [ ]
8. I'm ready for Day 2 (querying data)                      [ ]

What was the most useful thing you learned today?
_________________________________________________________________

What topic needs more explanation?
_________________________________________________________________
```

(Use this to gauge comprehension and plan Day 2 if needed.)

### Completion Checklist for You (Instructor)

Before Day 2, verify:

- [ ] All students have working PostgreSQL installation
- [ ] Each student created bootcamp_db successfully
- [ ] Each student created at least one table
- [ ] Each student executed a SELECT query and saw results
- [ ] Any installation issues documented (for follow-up)
- [ ] Students with gaps identified (for targeted review tomorrow)
- [ ] All Day 1 materials uploaded/shared with students
- [ ] Day 2 materials prepared and reviewed
- [ ] Any student who needs one-on-one help scheduled for evening/tomorrow morning

### Grading Rubric (if formal grading required)

| Criteria | Full (5) | Partial (3) | Incomplete (1) |
|----------|----------|-----------|--------------|
| **Installation** | PostgreSQL installed, running, verified | Installed but minor issues | Not installed or not working |
| **Conceptual** | Explains all concepts clearly, examples are accurate | Explains most concepts, one or two gaps | Cannot explain concepts |
| **Hands-On** | Creates tables, inserts data, runs queries successfully | Completes most tasks with minor errors | Cannot complete tasks |
| **Participation** | Active engagement, asks questions, helps peers | Follows along, completes exercises | Passive or disengaged |
| **Homework** | Completes optional assignments thoroughly | Attempts assignments | No attempt |

---

## Resources & Reference Materials

### Student Handouts to Prepare

**Handout 1: PostgreSQL Installation Quick Ref**
```
Windows:
1. Download from postgresql.org
2. Run installer, set postgres password
3. Open Command Prompt, type: psql -U postgres
4. You should see: postgres=#

macOS:
1. brew install postgresql
2. brew services start postgresql
3. Open Terminal, type: psql -U postgres
4. You should see: postgres=#

Linux (Ubuntu):
1. sudo apt install postgresql postgresql-contrib
2. Type: sudo -u postgres psql
3. You should see: postgres=#
```

**Handout 2: psql Command Reference**
```
\l                  List all databases
\c dbname           Connect to database
\dt                 List tables in current database
\d tablename        Describe table structure
\?                  Get help
\q                  Quit psql
SELECT version();   Show PostgreSQL version
```

**Handout 3: CREATE TABLE Template**
```sql
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    column_name DATA_TYPE CONSTRAINTS,
    column_name DATA_TYPE CONSTRAINTS,
    ...
);

Common constraints:
- PRIMARY KEY: Unique identifier for each row
- NOT NULL: This column must have a value
- UNIQUE: No duplicates allowed
- REFERENCES table(column): Foreign key to another table
- DEFAULT value: Use this value if not specified
```

**Handout 4: Day 1 Concept Map**
(Visual showing: Database → Tables → Rows & Columns, with relationships, keys, data types)

### Online Resources to Share

**Official PostgreSQL Documentation**
- https://www.postgresql.org/docs/ (most comprehensive)
- Data types: https://www.postgresql.org/docs/current/datatype.html

**Free Interactive Tutorials**
- SQLiteOnline: https://sqliteonline.com (browser-based SQL practice)
- W3Schools SQL Tutorial: https://www.w3schools.com/sql/ (beginner-friendly)

**Video Resources** (for students who learn better visually)
- PostgreSQL Installation Tutorial (YouTube) - search "PostgreSQL install Mac/Windows"
- Database Concepts Explained: https://www.youtube.com/watch?v=jtxmcS9x3eg

**pgAdmin Documentation**
- https://www.pgadmin.org/docs/pgadmin4/latest/ (how to use the GUI tool)

### Files to Keep Organized

Before class, have these files ready:

```
Day1/
├── README.md                      (overview)
├── installation_guide.sh           (installation commands)
├── first_database.sql             (the main script)
├── data_types_reference.md        (quick reference)
└── Teacher_Guides/
    └── Day_1_Teacher_Guide.md     (this document)
```

Make sure students have access to:
- `installation_guide.sh` (emailed, printed, or shared link)
- `first_database.sql` (to copy-paste or run)
- `data_types_reference.md` (for homework review)

### Troubleshooting Resources to Have Ready

**Bookmark in your browser**:
- PostgreSQL Installation Troubleshooting: https://www.postgresql.org/download/
- Stack Overflow [postgresql] tag: https://stackoverflow.com/questions/tagged/postgresql
- PostgreSQL Slack Community

**Keep downloaded**:
- PostgreSQL installers for all three OS (Mac, Windows, Linux)
- pgAdmin installer
- Backup of all course materials on USB

---

## Additional Instructor Notes

### Building a Community of Learning

- **First names**: Use them from day one
- **Normalize struggle**: "I've been using databases for 15 years and still Google things"
- **Celebrate wins**: "First database! Nice work."
- **Create peer support**: "Help your neighbor if they're stuck"

### Monitoring Individual Students

- **Quiet students**: Check in: "How's it going? Any questions?" They might be stuck but won't ask
- **Fast finishers**: "Can you help troubleshoot your neighbor's install?" → peer teaching
- **Visibly frustrated**: Take a breath with them, break problem into smaller steps
- **Asking great questions**: Celebrate it! "That's exactly the right question."

### Time Management Reality

- **Installation always takes longer than you think**: Okay. Plan for it. Flexibility is good.
- **Some students process faster**: That's fine. Have extension exercises ready (design more tables, explore pgAdmin).
- **Some students need repeats**: That's fine. One-on-one explanations after class.
- **You won't get through everything planned**: That's okay. Core material (install + create + concepts) matters most. Normalization forms can be taught day 2 or omitted.

### Equipment Failures & Backups

**If your demo machine fails**:
- Have slides with screenshots of expected outputs
- Use a backup laptop (pre-prepared)
- Use screen recording of commands if live demo isn't possible
- Cloud-based PostgreSQL (AWS, Heroku) as backup

**If student's machine fails**:
- Pair them with neighbor
- Promise post-class one-on-one
- Have a USB with installers
- Reference to cloud option (managed database)

### Energy Management

- **Start strong**: You set the tone. Excited about databases? They'll be excited.
- **Maintain momentum**: Transition quickly between sections; avoid dead air
- **Post-lunch slump is real**: Have something interactive after lunch
- **End on a high**: Final 15 minutes should feel celebratory ("You did real database work!")

### Feedback for Continuous Improvement

Collect at end of Day 1:
- "What one thing would have helped you more?"
- "What was confusing?"
- "What was clear?"

Use this to adjust Day 2. Learning from students makes you better teacher.

---

## Conclusion

**Day 1 is Successful When:**
- Every student has PostgreSQL running
- Every student understands tables, rows, columns, relationships, keys
- Every student has created and queried a database
- Every student feels confident and ready for tomorrow

**Remember**: 
- You're not just teaching SQL; you're teaching a way of thinking about data
- This foundation is critical; invest in getting it right
- Your enthusiasm is contagious; model excitement about databases
- Mistakes and struggles are part of learning; normalize them

**Looking Ahead to Day 2**: Tomorrow students will write queries. They'll discover questions they can ask of data. The groundwork today makes that exciting. You've done your job if they leave Day 1 thinking, "I can't wait to query data tomorrow."

Good luck! Teaching databases is incredibly rewarding. Your students will carry these skills into their careers.

---

**Document Version**: 1.0  
**Last Updated**: Day 1 Planning  
**For Use**: SQL Bootcamp Day 1 (3-Day Course)  
**Author**: SQL Bootcamp Teaching Team  
**Contact**: [Your Contact Info]