import mysql.connector as mysql


class konek:
    
    def __init__(self):
        self.mydb = mysql.Connect(host="localhost", user="root", password="",database="python_api")
        
        self.mycursor = self.mydb.cursor()

