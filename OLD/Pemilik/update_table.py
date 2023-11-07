import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_py_kelompok"
)

mycursor = mydb.cursor()

update_query = "UPDATE admin SET status = %s WHERE id_pemilik = %s"
new_alamat = "Kediri"  
pemilik_id = 1  

mycursor.execute(update_query, (new_alamat, pemilik_id))
mydb.commit()
