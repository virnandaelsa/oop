import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_py_kelompok"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pemilik")
myresult = mycursor.fetchall()

# print(myresult)

for key in myresult:
    print(f"NIK :{key[1]} |",end="")
    print(f"Nama :{key[2]} |",end="")
    print(f"Alamat :{key[2]} |",end="")
    print(f"Jenis Kelamin :{key[4]} |",end="")
    print(f"No hp :{key[5]} |",end="")
    print(f"Status :{key[6]} |")