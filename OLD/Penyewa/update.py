import mysql.connector

def main():
  mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "",
      database = "db_py_kelompok"
  )
  
  mycursor = mydb.cursor()
  
  sql = "UPDATE penyewa SET no_hp = %s WHERE nama = %s"
  val = ("0852316620987", "Bunga")
  mycursor.execute(sql, val)
  
  mydb.commit()
  
  print(mycursor.rowcount, "Data berhasil diupdate...")