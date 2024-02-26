import mysql.connector

class DBManipulate():
    
    def Mydbconnection(self):
        con = mysql.connector.connect(
        host="host",
        user="root",
        password="Sangari@2024",
        database="ai_sangari"
        )
        return con  
      
        