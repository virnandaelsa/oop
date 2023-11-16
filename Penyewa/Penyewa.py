import mysql.connector

class penyewa:
    DATA_USER = []
    def __init__(self):
        self.__db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "db_py_kelompok"
        )

    def lihat_data(self):
        con = self.__db.cursor()

        sql = f"SELECT * FROM user WHERE username = '{self.DATA_USER[0][7]}'"
        con.execute(sql)
        val = con.fetchall()
        
        for data in val:
            print(f"NIK : {data[1]}")
            print(f"Nama : {data[2]}")
            print(f"Asal : {data[3]}")
            print(f"Jenis Kelamin : {data[4]}")
            print(f"No Hp : {data[5]}")
            print(f"Status : {data[6]}")
            print(f"Username : {data[7]}")
            print(f"Password : {data[8]}")
        
    def update_data(self):
        con = self.__db.cursor()
        
        print("DATA MU :")
        self.lihat_data()
        no = input("\nSilahkan Ganti NOMOR HP MU: ")

        sql = f"UPDATE user SET no_hp = '{no}' WHERE username='{self.DATA_USER[0][7]}'"
        con.execute(sql)
        self.__db.commit()
        print(con.rowcount," BERHASIL DI GANTI")