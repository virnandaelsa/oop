import mysql.connector

class Kamar:
    def __init__(self):
        self.__db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "db_py_kelompok"
        )

        con = self.__db.cursor()

        try:
            sql = "CREATE TABLE kamar (id_kamar INT AUTO_INCREMENT PRIMARY KEY,nama_kamar VARCHAR(100),jenis_kamar VARCHAR(100),status_kamar VARCHAR(100),keterangan TEXT)"
            con.execute(sql)

            print("table kamar berhasil di buat")
        except Exception as e:
            pass
    
    def insert_kamar(self):
        con = self.__db.cursor()

        name = input("Masukan nama kamar: ")
        jns = input("Masukan jenis kamar: ")
        sts = input("Masukan status kamar: ")
        ket = input("Masukan deskripsi kamar: ")
        sql = "INSERT INTO kamar(nama_kamar,jenis_kamar,status_kamar,keterangan) VALUES (%s,%s,%s,%s)"
        val = (name,jns,sts,ket)

        con.execute(sql,val)
        self.__db.commit()

        print(con.rowcount," Data berhasil di tambahkan")

    def show_kamar(self):
        con = self.__db.cursor()

        sql = "SELECT * FROM kamar"
        con.execute(sql)
        ress = con.fetchall()

        for key in ress:
            print(f"Nama kamar      : {key[1]}")
            print(f"Jenis kamar     : {key[2]}")
            print(f"Status kamar    : {key[3]}")
            print(f"Deskripsi kamar : {key[4]}\n")
    
    def update_kamar(self):
        con = self.__db.cursor()
        # s = Kamar()
        self.show_kamar()

        st = input("Masukan Status: ")
        name = input("Masukan Nama kamar: ")
        sql = "UPDATE kamar SET status_kamar = %s WHERE nama_kamar = %s"
        val = (st,name)
        con.execute(sql,val)
        self.__db.commit()

        print(con.rowcount," Data berhasil di ubah")

    def delete_kamar(self):
        con = self.__db.cursor()
        self.show_kamar()

        nm = input("Masukan nama kamar yang ingin di hapus: ")
        sql = "DELETE FROM kamar WHERE nama_kamar = %s"
        val = (nm,)

        con.execute(sql,val)
        self.__db.commit()

