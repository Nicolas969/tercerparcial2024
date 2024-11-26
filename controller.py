import time
import sqlite3 as sql

def createDB():
    connet = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    connet.commit()
    connet.close()

def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE experience_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,  -- 'growth', 'contribution'
    description TEXT
);
    """)
    print("Tabla creada")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    createTable()

