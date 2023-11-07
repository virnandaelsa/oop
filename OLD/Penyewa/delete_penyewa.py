import mysql.connector
def main():
 mydb = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "",
     database = "db_py_kelompok"
 )
 
 mycursor = mydb.cursor()
 
 sql = "DELETE FROM penyewa WHERE nama = %s"
 value = ("Bunga",)
 
 mycursor.execute(sql, value)
 
 mydb.commit()
 
 print(mycursor.rowcount, "Data berhasil dihapus...")