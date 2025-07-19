import sqlite3

def init_database():
    connection = sqlite3.connect('magic8ball.db')
    cursor = connection.cursor()
    print('DB Init')


    query = """
        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
	        answer TEXT NOT NULL
        );
    """
    cursor.execute(query)
    cursor.close()

if __name__ == '__main__':
        init_database()