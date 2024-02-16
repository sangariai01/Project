import mysql.connector
con=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_sangari"
)
print(con)
result=con.cursor()
result.execute("show tables")
result_show=result.fetchall()
for x in result_show:
     print(x)
result.execute("select * from Ai_batch_Stud_list")
result_show=result.fetchall()
for x in result_show:
    print(x)
# result.execute("delete from host_summary where sno = 4")
# result.execute("select * from host_summary")
# result_show=result.fetchall()
# for x in result_show:
#     print(x)