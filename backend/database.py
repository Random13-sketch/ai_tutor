import sqlite3

def init_db():
    # Connect to (or create) the database file
    conn = sqlite3.connect('tutor.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')

    # Create ChatHistory table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ChatHistory (
            message_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    ''')

    # Add a demo user so the app has someone to "log in" as
    cursor.execute("INSERT OR IGNORE INTO Users (user_id, username) VALUES (1, 'demo_student')")

    conn.commit()
    conn.close()
    print("✅ Database 'tutor.db' created and initialized!")

if __name__ == '__main__':
    init_db()