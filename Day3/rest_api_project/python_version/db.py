"""Database connection module"""
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432),
    'database': os.getenv('DB_NAME', 'ecommerce'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'postgres'),
}

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = psycopg2.connect(**db_config)
        print('Connected to the database successfully')
        return conn
    except psycopg2.Error as err:
        print(f'Error connecting to the database: {err}')
        return None

def query(sql, params=None):
    """Execute a query and return results as list of dictionaries"""
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(sql, params)
        conn.commit()
        
        # Fetch results if it's a SELECT query
        if cursor.description:
            results = cursor.fetchall()
            return [dict(row) for row in results]
        return None
    except psycopg2.Error as err:
        conn.rollback()
        print(f'Database error: {err}')
        raise err
    finally:
        cursor.close()
        conn.close()

def query_one(sql, params=None):
    """Execute a query and return a single result"""
    results = query(sql, params)
    if results and len(results) > 0:
        return results[0]
    return None

def execute(sql, params=None):
    """Execute a query without returning results (for INSERT, UPDATE, DELETE)"""
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(sql, params)
        conn.commit()
        
        # Fetch results if available (for RETURNING clause)
        if cursor.description:
            results = cursor.fetchall()
            return [dict(row) for row in results]
        return None
    except psycopg2.Error as err:
        conn.rollback()
        print(f'Database error: {err}')
        raise err
    finally:
        cursor.close()
        conn.close()

def get_transaction():
    """Get a connection for transaction handling"""
    return get_db_connection()