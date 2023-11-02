import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_py_kelompok"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE penyewa(id INT(9) AUTO_INCREMENT PRIMARY KEY, NIK INT(12), alamat VARCHAR(255), jenkel VARCHAR(55), no_hp INT(12), status VARCHAR(55))")