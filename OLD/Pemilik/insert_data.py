import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_py_kelompok"
)

mycursor = mydb.cursor()

sql = "INSERT INTO pemilik (nik, nama, alamat, jenis_kelamin, no_hp, status) VALUES (%s, %s, %s, %s, %s, %s)"
val = (1234, "Hasan","Kediri", "Pria", "0895394189", "Mahasiswa")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data berhasil ditambahkan....")