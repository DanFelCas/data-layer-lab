# User Management CLI with PostgreSQL

This is a personal Python project that manages users in a PostgreSQL database through a simple command-line interface. It includes a connection pool, logging, and basic CRUD operations.

## Features

- List, add, update, and delete users
- Uses connection pooling (`psycopg2.pool`)
- Logs actions to console and file
- Thread-safe config updates

## How It Works

The app connects to a PostgreSQL database and interacts with a `usuario` table. It’s structured using:

- `User` class for user data
- `UserDao` for database queries
- Context managers for safe connection handling
- A simple CLI in `main.py`

### PostgreSQL Table

Before running the app, create this table in your database:

```sql
CREATE TABLE usuario (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);
```
