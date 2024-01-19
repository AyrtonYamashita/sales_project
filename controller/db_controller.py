import psycopg2

class ManageDB:
    def __init__(self):
        self.con = psycopg2.connect(
            dbname='seara',
            user='postgres',
            password='admin',
            host='localhost'
        )

        cur = self.con.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS seara")
        cur.execute("CREATE SCHEMA IF NOT EXISTS users")
        cur.execute("""CREATE TABLE IF NOT EXISTS users.clients (
                    client_id
        ) """)