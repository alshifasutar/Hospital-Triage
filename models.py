import sqlite3

def init_db():
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            severity INTEGER NOT NULL,
            arrival_time REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_patient_to_db(name, severity, arrival_time):
    try:
        conn = sqlite3.connect('patients.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO patients (name, severity, arrival_time) VALUES (?, ?, ?)',
                       (name, severity, arrival_time))
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def fetch_patients():
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, severity, arrival_time FROM patients')
    rows = cursor.fetchall()
    conn.close()
    return rows