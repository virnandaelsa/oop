import mysql.connector

class Pemilik:
    def __init__ (self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_py_kelompok"
        )

        db = self.__mydb.cursor()

        try:
            db.execute("CREATE TABLE pemilik (id_pemilik INT AUTO_INCREMENT PRIMARY KEY,NIK INT(16),nama VARCHAR(100), alamat VARCHAR(255), jenis_kelamin VARCHAR(10), no_hp VARCHAR(15), status VARCHAR(20))")
            print("Table Pemilik berhasil di tambahkan")
        except Exception as e:
            pass

    def insert_data(self):
        mycursor = self.__mydb.cursor()

        sql = "INSERT INTO pemilik (nik, nama, alamat, jenis_kelamin, no_hp, status) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (1234, "Hasan","Kediri", "Pria", "0895394189", "Mahasiswa")
        mycursor.execute(sql, val)

        self.__mydb.commit()

        print(mycursor.rowcount, "Data berhasil ditambahkan....")

    def delete_data(self):
        mycursor = self.__mydb.cursor()

        sql = "DELETE FROM pemilik WHERE id_pemilik = %s"
        val = (2,)
        mycursor.execute(sql, val)
        self.__mydb.commit()
        print(mycursor.rowcount, "Data berhasil dihapus..")

    def show_data(self):
        mycursor = self.__mydb.cursor()

        mycursor.execute("SELECT * FROM pemilik")
        myresult = mycursor.fetchall()

        for key in myresult:
            print(f"NIK :{key[1]} |",end="")
            print(f"Nama :{key[2]} |",end="")
            print(f"Alamat :{key[3]} |",end="")
            print(f"Jenis Kelamin :{key[4]} |",end="")
            print(f"No hp :{key[5]} |",end="")
            print(f"Status :{key[6]} |")
    
    def update_data(self):
        
        mycursor = self.__mydb.cursor()

        new_alamat = "Kediri"  
        pemilik_id = 1  
        update_query = "UPDATE pemilik SET status = %s WHERE id_pemilik = %s"
        val = (new_alamat,pemilik_id)

        mycursor.execute(update_query,val)
        self.__mydb.commit()

        print(mycursor.rowcount, "Data berhasil diubah..")

