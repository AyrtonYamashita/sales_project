import psycopg2

class ManageDB:
    def __init__(self):
        self.con = psycopg2.connect(
            dbname='seara',
            user='postgres',
            password='admin',
            host='localhost'
        )
        self.create_user_data_info()
        self.create_products_data()
        return self.con
      
    def create_user_data_info(self):
        try:
            cur = self.con.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS seara")
            cur.execute("CREATE SCHEMA IF NOT EXISTS users")
            cur.execute("""CREATE TABLE IF NOT EXISTS users.data_pf (
                client_id VARCHAR(200) PRIMARY KEY NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL,
                complete_name VARCHAR(100) NOT NULL,
                cpf INTEGER(11) NOT NULL UNIQUE,
                auth_insta BOOLEAN NOT NULL,          
                instagram VARCHAR(100)    
            ) """)
            cur.execute("""CREATE TABLE IF NOT EXISTS users.data_pj (
                client_id VARCHAR(200) PRIMARY KEY NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL,
                company_name VARCHAR(100) NOT NULL,
                cnpj INTEGER(14) NOT NULL UNIQUE,
                auth_insta BOOLEAN NOT NULL,          
                instagram VARCHAR(100)               
            ) """)
            cur.execute("""CREATE TABLE IF NOT EXISTS users.data_delivery (
                client_id VARCHAR(200) PRIMARY KEY NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL,
                complete_name VARCHAR(100) NOT NULL,
                cpf INTEGER(11) NOT NULL UNIQUE,              
            ) """)
            cur.execute("""CREATE TABLE IF NOT EXISTS users.data_address_sender (
                client_id VARCHAR(200) PRIMARY KEY NOT NULL UNIQUE,
                cep_sender INTEGER(8) NOT NULL,
                street VARCHAR(100) NOT NULL,
                neighbourhood VARCHAR(100) NOT NULL,
                city VARCHAR(100) NOT NULL,
                state CHAR(2) NOT NULLM
                complement VARCHAR(100)
                )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS users.data_address_recipient (
                client_id VARCHAR(200) PRIMARY KEY NOT NULL UNIQUE,
                cep_recipient INTEGER(8) NOT NULL,
                street VARCHAR(100) NOT NULL,
                neighbourhood VARCHAR(100) NOT NULL,
                city VARCHAR(100) NOT NULL,
                state CHAR(2) NOT NULLM
                complement VARCHAR(100)
                )""")
            self.con.commit()
            cur.close()
            return {
                'Status': True
            }
        except Exception as e:
            return {
                'Status': False
            }
        
    def create_products_data(self):
        try:
            cur = self.con.cursor()
            cur.execute("CREATE SCHEMA IF NOT EXISTS orders")
            cur.execute("""CREATE TABLE IF NOT EXISTS orders.products (
                client_id VARCHAR(200) PRIMARY KEY NOT NULL UNIQUE,
                chocotone INTEGER(99999),
                panetone INTEGER(99999),
                person_box BOOLEAN NOT NULL,
                date_delivery DATE NOT NULL,
                total_value FLOAT(99999)
                )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS orders.payment (
                client_id VARCHAR(200), PRIMARY KEY NOT NULL UNIQUE
                type_payment VARCHAR(50) NOT NULL,
                exp_date VARCHAR(50) NOT NULL,
                fiscal_doc VARCHAR(200) NOT NULL
                )""")
            self.con.commit()
            cur.close()
            return {
                'Status': True
            }
        except Exception as e:
            return {
                'Status': False
            }
        
    def add_user_data(self, uid, email, name, cpf_cnpj, auth_insta, instagram):
        try:
            if len(cpf_cnpj) == 11:
                cur = self.con.cursor()
                cur.execute
                ("""INSERT INTO users.data_pf 
                    (client_id, email, complete_name, cpf, auth_insta, instagram)
                    VALUES (%s, %s, %s, %s, %s, %s)""", (uid, email, name, int(cpf_cnpj), bool(auth_insta), instagram))
                self.con.commit()
                cur.close()
            elif len(cpf_cnpj) == 14:
                cur = self.con.cursor()
                cur.execute
                ("""INSERT INTO users.data_pf 
                    (client_id, email, company_name, cnpj, auth_insta, instagram)
                    VALUES (%s, %s, %s, %s, %s, %s)""", (uid, email, name, int(cpf_cnpj), bool(auth_insta), instagram))
                self.con.commit()
                cur.close()
            
            return {
                'Status': True
            }
        except Exception as e:
            return {
                'Status': False
            }
            
    def add_address_sender(self, uid, cep, street, neigh, city, state, complement):
        try:
            cur = self.con.cursor()
            cur.execute("""INSERT INTO users.data_address_sender 
                        (client_id, cep_recipient, street, neighbourhood, city, state, complement)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                        (uid, cep, street, neigh, city, state, complement))
            self.con.commit()
            cur.close()
            return {
                'Status': True
            }
        except Exception as e:
            return {
                'Status': False
            }
    
    def add_address_recipient(self, uid, cep, street, neigh, city, state, complement):
        try:
            cur = self.con.cursor()
            cur.execute("""INSERT INTO users.data_address_recipient
                        (client_id, cep_recipient, street, neighbourhood, city, state, complement)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                        (uid, cep, street, neigh, city, state, complement))
            self.con.commit()
            cur.close()
            return {
                'Status': True
            }
        except Exception as e:
            return {
                'Status': False
            }
            
    def add_products_data(self, uid, qnt_choco, qnt_pane, person_box, date, value):
        try:
            cur = self.con.cursor()
            cur.execute("""INSERT INTO orders.products 
                        (client_id, chocotone, panetone, person_box, date_delivery, total_value)
                        VALUES (%s, %s, %s, %s, %s, %s)""", (uid, int(qnt_choco), int(qnt_pane), bool(person_box), date, float(value)))
            self.con.commit()
            cur.close()
            return {
                'Status': True
            }
        except Exception as e:
            return {
                'Status': False
            }
            
    def add_fiscal_data(self, uid, type, exp, fiscal_info):
        try:
            cur = self.con.cursor()
            cur.execute("""INSERT INTO orders.payment (client_id, type_payment, exp_date, fiscal_doc)
                        VALUES (%s, %s, %s, %s)""", uid, type, exp, fiscal_info)
            self.con.commit()
            cur.close()
            return {
                'Status': True
            }
        except Exception as e:
            return {
                'Status': False
            }