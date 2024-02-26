class DBManipulate():
    
    def __init__(self):
        con = mysql.connector.connect(
        host="host",
        user="root",
        password="Sangari@2024",
        database="ai_sangari"
        )
        return con  
        print(con)
        result=con.cursor()
        result.execute("show tables")
        for x in result_show:
        print(x)