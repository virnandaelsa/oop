import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_py_kelompok"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE penyewa(id INT(9) AUTO_INCREMENT PRIMARY KEY, NIK VARCHAR(12),nama VARCHAR(100), alamat VARCHAR(255), jenkel VARCHAR(55),kampus VARCHAR(100), no_hp VARCHAR(13), status VARCHAR(55))")