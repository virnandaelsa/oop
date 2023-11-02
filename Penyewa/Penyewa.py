import mysql.connector

class Penyewa:
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "db_py_kelompok"
        )

        mycursor = self.__mydb.cursor()
        try:
            mycursor.execute("CREATE TABLE penyewa(id INT(9) AUTO_INCREMENT PRIMARY KEY, NIK VARCHAR(12),nama VARCHAR(100), alamat VARCHAR(255), jenkel VARCHAR(55),kampus VARCHAR(100), no_hp VARCHAR(13), status VARCHAR(55))")
        except Exception as e:
            print(e)
            pass

    def insert_data(self):
        mycursor = self.__mydb.cursor()

        sql = "INSERT INTO penyewa (NIK, nama, alamat, jenkel, kampus, no_hp, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = [
            ("23102816772", "Anandya", "Kediri", "Perempuan", "Politeknik Negeri Malang", "0851231552918", "mahasiswa"),
            ("23710029188", "Angelina", "Pasuruan", "Perempuan", "Universitas Islam Kadiri", "0815532718771", "mahasiswa"),
            ("23710281762", "Bunga", "Nganjuk", "Perempuan", "Universitas Kadiri", "0882018155287", "mahasiswa")
        ]

        mycursor.executemany(sql, val)

        self.__mydb.commit()

        print(mycursor.rowcount, "Data penyewa berhasil ditambahkan...")
    
    def delete_data(self):
        mycursor = self.__mydb.cursor()
        
        sql = "DELETE FROM penyewa WHERE nama = %s"
        value = ("Bunga",)
        
        mycursor.execute(sql, value)
        
        self.__mydb.commit()
        
        print(mycursor.rowcount, "Data berhasil dihapus...")

    def show_data(self):

        mycursor = self.__mydb.cursor()

        mycursor.execute("SELECT * FROM penyewa")

        myresult = mycursor.fetchall()

        for key in myresult:
            print(f"NIK :{key[1]} |",end="")
            print(f"Nama :{key[2]} |",end="")
            print(f"Alamat :{key[3]} |",end="")
            print(f"Jenis Kelamin :{key[4]} |",end="")
            print(f"Univ :{key[5]} |",end="")
            print(f"No hp :{key[6]} |",end="")
            print(f"Status :{key[7]} |")

    def update_data(self):
        mycursor = self.__mydb.cursor()
  
        sql = "UPDATE penyewa SET no_hp = %s WHERE nama = %s"
        val = ("0852316620987", "Bunga")
        mycursor.execute(sql, val)
        
        self.__mydb.commit()
        
        print(mycursor.rowcount, "Data berhasil diupdate...")