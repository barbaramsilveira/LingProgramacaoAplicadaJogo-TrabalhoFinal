import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(f"{db_name}.db")
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS DBScore (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ship TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save(self, record: dict):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO DBScore (name, ship, score, date)
            VALUES (?, ?, ?, ?)
        ''', (record['name'], record['ship'], record['score'], record['date']))
        self.conn.commit()

    def retrieve_top5(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT id, name, ship, score, date
            FROM DBScore
            ORDER BY score DESC
            LIMIT 5
        ''')
        return cursor.fetchall()

    def close(self):
        self.conn.close()