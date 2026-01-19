import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "laralysis.db"

def init_db():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS functions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        expr_str TEXT,
        var_name TEXT
    )
    """)

    connection.commit()
    connection.close()

def save_function(function_model):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO functions (name, expr_str, var_name)
        VALUES (?, ?, ?)
        """,
        (
            function_model.name,
            function_model.expr_str,
            function_model.var_name,
        )
    )

    connection.commit()
    connection.close()

from core.function_model import FunctionModel

def load_functions():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT name, expr_str, var_name FROM functions")
    rows = cursor.fetchall()

    connection.close()

    functions = []
    for name, expr_str, var_name in rows:
        f = FunctionModel(expr_str=expr_str, var_name=var_name)
        functions.append(f)

    return functions