import mysql.connector

class DBManipulate():
    
    def Mydbconnection(self):
        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sangari@2024",
        database="ai_sangari"
        )
        return con  
   
    def insertvalues(self,st_name,tamil,eng,math,sci,ss):  
        Name=st_name
        Tamil=tamil
        English=eng
        Maths=math
        Science=sci
        Social=ss
      
        data=self.Mydbconnection()
        result=data.cursor()

        statement="insert into Student_details (Name,Tamil,English,Maths,Science,Social) values(%s,%s,%s,%s,%s,%s);"
        valuepass=(Name,Tamil,English,Maths,Science,Social)
        result.execute(statement,valuepass)
        print(statement)
      



        # data.commit()

        # return (str(result.rowcount) + " row inserted")