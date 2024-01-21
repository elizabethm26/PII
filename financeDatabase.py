import mysql.connector

class FinanceDatabase:
    def __init__(self, host='localhost', user='root', password='your_password', database='finance_recommendations'):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products
                              (id INT AUTO_INCREMENT PRIMARY KEY,
                               product_name VARCHAR(255),
                               description TEXT)''')
        self.conn.commit()

    def insert_product(self, product_name, description):
        query = "INSERT INTO products (product_name, description) VALUES (%s, %s)"
        values = (product_name, description)
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
