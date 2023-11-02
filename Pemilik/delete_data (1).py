import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_py_kelompok"
)

mycursor = mydb.cursor()

sql = "DELETE FROM pemilik WHERE id = %s"
val = (2,)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "Data berhasil dihapus..")