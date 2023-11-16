import mysql.connector

class Admin:
    def __init__(self):
        self.__db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "db_py_kelompok"
        )

        mycursor = self.__db.cursor()
        try:
            sql = "CREATE TABLE user(id INT(9) AUTO_INCREMENT PRIMARY KEY, NIK VARCHAR(20), nama VARCHAR(100),alamat VARCHAR(255), jenkel VARCHAR(55), no_hp VARCHAR(12), status VARCHAR(55), username VARCHAR(255) PRIMARY KEY, password VARCHAR(255))"
            mycursor.execute(sql)
            print("Berhasil menambahkan Table penyewa")
        except Exception as e:
            # print(e)
            pass
    
    def login(self,val1, val2): 
        con = self.__db.cursor()
        sql = "SELECT status FROM user WHERE username  = %s AND password = %s"
        val = (val1, val2) 
        con.execute(sql,val)
        status = con.fetchone()
        return str(status[0]) 

    def insert_data(self,nik, name, alamat, jk, hp, sts, username, pw):

        con = self.__db.cursor()
        sql = "INSERT INTO `user` (`NIK`, `nama`, `alamat`, `jenkel`, `no_hp`, `status`,`username`,`password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (nik,name,alamat,jk,hp,sts,username, pw)
        con.execute(sql,val)

        self.__db.commit()

        print(con.rowcount," Data berhasil di tambahkan")

    def delete_data(self,nik):

        sql = f"DELETE FROM user WHERE NIK = '{nik}';"
        con = self.__db.cursor()

        con.execute(sql)

        self.__db.commit()
        if con.rowcount < 0 : 
            print("Data gagal di Hapus")
        else :
            print(con.rowcount," Data berhasil di Hapus")


    def update_data(self,nik, name, alamat, jk, hp, sts):
        con = self.__db.cursor()

        sql = f"UPDATE admin SET nama='{name}',alamat='{alamat}',jenkel='{jk}',no_hp='{hp}',status='{sts}' WHERE NIK='{nik}';"
        
        con.execute(sql)

        self.__db.commit()

        if con.rowcount < 0 : 
            print("Data gagal di Ubah")
        else :
            print(con.rowcount," Data berhasil di ubah")

    def show_data(self):
        con = self.__db.cursor()
        sql = "SELECT * FROM user WHERE status = 'penyewa'"
        con.execute(sql)

        val = con.fetchall()

        for key in val:
            print(f"NIK             :{key[1]}")
            print(f"Nama            :{key[2]}")
            print(f"Alamat          :{key[2]}")
            print(f"Jenis Kelamin   :{key[4]}")
            print(f"No hp           :{key[5]}")
            print(f"Status          :{key[6]}\n")
        print()