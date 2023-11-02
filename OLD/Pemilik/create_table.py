import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_py_kelompok"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE pemilik (id_pemilik INT AUTO_INCREMENT PRIMARY KEY,NIK INT(16),nama VARCHAR(100), alamat VARCHAR(255), jenis_kelamin VARCHAR(10), no_hp VARCHAR(15), status VARCHAR(20))")
