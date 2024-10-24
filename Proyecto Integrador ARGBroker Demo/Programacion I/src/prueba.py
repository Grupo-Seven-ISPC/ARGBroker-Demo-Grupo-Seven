from database.conexion_database import connection

cursor=connection.cursor()
query="""
    SELECT * FROM Estado
"""
cursor.execute(query,())
resultado=cursor.fetchall()
for res in resultado:
    print(res)