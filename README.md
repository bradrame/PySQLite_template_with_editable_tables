# SQLite Template

A bare-bones SQLite database template with Python for quick database operations.

## Files

- `database.py` - Database connection manager
- `query.py` - SQL query executor that reads from `query.sql`
- `query.sql` - SQL statements to execute

## Quick Start

1. Edit your SQL statements in `query.sql`
2. Run the query executor:
   ```bash
   python query.py
   ```

The script will automatically:
- Clear the terminal
- Execute all SQL statements from `query.sql` 
- Display SELECT results in table format
- Create `database.db` if it doesn't exist

## Usage Examples

### Using QueryExecutor
```python
from query import QueryExecutor

executor = QueryExecutor()
results = executor.execute_sql_file()  # Runs query.sql
```

### Using DatabaseManager directly
```python
from database import DatabaseManager

db = DatabaseManager()
users = db.execute_query("SELECT * FROM users")
db.execute_non_query("INSERT INTO users (name, username, password) VALUES (?, ?, ?)", 
                      ("John Doe", "johndoe", "password123"))
```

### Custom SQL file
```python
executor = QueryExecutor()
results = executor.execute_sql_file("custom.sql")
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Database

Creates `database.db` SQLite file in the current directory.# PySQLite_template_with_editable_tables
