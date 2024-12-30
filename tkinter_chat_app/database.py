import sqlite3

def create_database():
    conn = sqlite3.connect('chat_app.db')
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mobile_number TEXT UNIQUE NOT NULL,
        otp TEXT,
        is_verified INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

def insert_user(mobile_number, otp):
    conn = sqlite3.connect('chat_app.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (mobile_number, otp) VALUES (?, ?)', (mobile_number, otp))
    conn.commit()
    conn.close()

def verify_user(mobile_number, otp):
    conn = sqlite3.connect('chat_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE mobile_number = ? AND otp = ?', (mobile_number, otp))
    user = cursor.fetchone()
    if user:
        cursor.execute('UPDATE users SET is_verified = 1 WHERE mobile_number = ?', (mobile_number,))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False
