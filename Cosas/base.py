import mysql.connector

conexion = mysql.connector.connect(
    host = "mysql-5707.dinaserver.com",
    port = "3306",
    user = "mouredev_read",
    password = "mouredev_pass",
    db = "moure_test",
    )


cursor= conexion.cursor()

#cursor.execute("SHOW DATABASES")



sql= """SELECT * FROM challenges"""
midic = {}
cursor.execute(sql)
for n, bd in enumerate(cursor):
    renglon = list(bd)
    elemento = renglon[0]
    del(renglon[0])
    midic[str(elemento)] = renglon

for a in midic.values():
    print(a)
