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
            sql = "CREATE TABLE admin(id INT(9) AUTO_INCREMENT PRIMARY KEY, NIK VARCHAR(12), nama VARCHAR(100),alamat VARCHAR(255), jenkel VARCHAR(55), no_hp VARCHAR(12), status VARCHAR(55))"
            mycursor.execute(sql)
            print("Berhasil menambhakan Table admin")
        except Exception as e:
            # print(e)
            pass

    def insert_data(self,nik, name, alamat, jk, hp, sts):

        con = self.__db.cursor()
        sql = "INSERT INTO `admin` (`NIK`, `nama`, `alamat`, `jenkel`, `no_hp`, `status`) VALUES (%s,%s,%s,%s,%s,%s);"
        val = (nik,name,alamat,jk,hp,sts)
        con.execute(sql,val)

        self.__db.commit()

        print(con.rowcount," Data berhasil di tambahkan")

    def delete_data(self,nik):

        sql = f"DELETE FROM admin WHERE NIK = '{nik}';"
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
        sql = "SELECT * FROM admin"
        con.execute(sql)

        val = con.fetchall()

        for key in val:
            print(f"NIK :{key[1]} |",end="")
            print(f"Nama :{key[2]} |",end="")
            print(f"Alamat :{key[2]} |",end="")
            print(f"Jenis Kelamin :{key[4]} |",end="")
            print(f"No hp :{key[5]} |",end="")
            print(f"Status :{key[6]} |")
        print()
