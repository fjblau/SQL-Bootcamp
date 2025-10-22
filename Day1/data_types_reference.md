# PostgreSQL Data Types Reference

This document provides a quick reference for the most commonly used PostgreSQL data types.

## Numeric Types

| Data Type | Description | Size | Range |
|-----------|-------------|------|-------|
| SMALLINT | Small-range integer | 2 bytes | -32,768 to +32,767 |
| INTEGER | Typical choice for integer | 4 bytes | -2,147,483,648 to +2,147,483,647 |
| BIGINT | Large-range integer | 8 bytes | -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807 |
| DECIMAL(p,s) | Exact numeric with precision p, scale s | variable | Up to 131,072 digits before decimal point; up to 16,383 digits after |
| NUMERIC(p,s) | Exact numeric with precision p, scale s | variable | Up to 131,072 digits before decimal point; up to 16,383 digits after |
| REAL | Single precision floating-point | 4 bytes | 6 decimal digits precision |
| DOUBLE PRECISION | Double precision floating-point | 8 bytes | 15 decimal digits precision |
| SERIAL | Auto-incrementing integer | 4 bytes | 1 to 2,147,483,647 |
| BIGSERIAL | Auto-incrementing bigint | 8 bytes | 1 to 9,223,372,036,854,775,807 |

## Character Types

| Data Type | Description | Size |
|-----------|-------------|------|
| CHAR(n) | Fixed-length character string | n characters |
| VARCHAR(n) | Variable-length character string | Up to n characters |
| TEXT | Variable unlimited length | Unlimited |

## Binary Data Types

| Data Type | Description |
|-----------|-------------|
| BYTEA | Binary data ("byte array") |

## Date/Time Types

| Data Type | Description | Size | Range |
|-----------|-------------|------|-------|
| DATE | Calendar date (year, month, day) | 4 bytes | 4713 BC to 5874897 AD |
| TIME | Time of day (no time zone) | 8 bytes | 00:00:00 to 24:00:00 |
| TIMESTAMP | Date and time (no time zone) | 8 bytes | 4713 BC to 294276 AD |
| TIMESTAMPTZ | Date and time with time zone | 8 bytes | 4713 BC to 294276 AD |
| INTERVAL | Time interval | 16 bytes | -178,000,000 years to 178,000,000 years |

## Boolean Type

| Data Type | Description | Size | Values |
|-----------|-------------|------|--------|
| BOOLEAN | Logical Boolean (true/false) | 1 byte | true, false, null |

## Special Types

| Data Type | Description |
|-----------|-------------|
| UUID | Universally Unique Identifier |
| JSON | JavaScript Object Notation |
| JSONB | Binary JSON format, decomposed |
| ARRAY | Array of values |

## When to Use Each Type

- **INTEGER**: For most whole numbers (IDs, counts, etc.)
- **SERIAL**: For auto-incrementing primary keys
- **NUMERIC/DECIMAL**: For exact calculations (financial data)
- **VARCHAR**: For variable-length strings with a reasonable limit
- **TEXT**: For unlimited length strings (comments, descriptions)
- **TIMESTAMP**: For recording when events occurred
- **BOOLEAN**: For true/false flags
- **UUID**: For globally unique identifiers

## Example Usage in Table Creation

```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL,
    weight REAL,
    is_available BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tags TEXT[]
);
```

## Best Practices

1. Use the smallest data type that can reliably store your data
2. Use TEXT for unlimited length strings instead of VARCHAR without a limit
3. Use TIMESTAMPTZ instead of TIMESTAMP when working with time zones
4. Consider using UUID for distributed systems where IDs need to be globally unique
5. Use JSONB instead of JSON when you need to query or index the JSON data