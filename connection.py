from dotenv import load_dotenv
import os
import mysql.connector 

load_dotenv()

class Connection:
    def __init__(self):
        self.user = os.getenv("DB_USER")
        self.host =os.getenv("DB_HOST")
        self.__password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        
    def create_conn(self):
        try: 
            conn = mysql.connector.connect(user=self.user,host=self.host,password = self.__password,database = self.database)
            cursor_obj = conn.cursor()
            print("connection established successfully!")
            return conn,cursor_obj
        except Exception as e:
            print(e)
            return None,None
            

    