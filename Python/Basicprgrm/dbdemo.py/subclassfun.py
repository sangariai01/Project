import mysql.connector

class DBManipulate():
    
    def Mydbconnection(self):
        con = mysql.connector.connect(
        host="192.168.1.240",
        user="AIBATCH01",
        password="AI@123",
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

        stmts="INSERT INTO student_details (Name, Tamil, English, Maths, Science, Social) VALUES ( "+ '"' + Name + '"' + "," + str(Tamil) + "," + str(English)+","+ str(Maths)  +","+ str(Science) +","+ str(Social) + ");"
        
        result.execute(stmts)
        print(stmts)

       
        data.commit()

        return (str(result.rowcount) + " row inserted")