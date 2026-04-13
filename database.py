import sqlite3

class Database:
    def __init__(self, db_file):
        """ create a database connection to a SQLite database """
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self):
        """ create a table in the database """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_item(self, item_name, quantity, price):
        """ add an item to the inventory """
        self.cursor.execute('''
            INSERT INTO inventory (item_name, quantity, price)
            VALUES (?, ?, ?)''', (item_name, quantity, price))
        self.conn.commit()

    def update_item(self, item_id, quantity):
        """ update quantity of an item """
        self.cursor.execute('''
            UPDATE inventory
            SET quantity = ?
            WHERE id = ?
        ''', (quantity, item_id))
        self.conn.commit()

    def delete_item(self, item_id):
        """ delete an item from the inventory """
        self.cursor.execute('''
            DELETE FROM inventory
            WHERE id = ?
        ''', (item_id,))
        self.conn.commit()

    def fetch_all_items(self):
        """ fetch all items in the inventory """
        self.cursor.execute('''
            SELECT * FROM inventory
        ''')
        return self.cursor.fetchall()

    def close(self):
        """ close the database connection """
        self.conn.close()