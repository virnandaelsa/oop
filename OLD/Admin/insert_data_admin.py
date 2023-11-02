import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )

    nik = int(input("Masukan NIK: "))
    name = input("Masukan nama: ")
    alamat = input("Masukan alamat: ")
    jk = input("Masukan jenis kelamin: ")
    hp = int(input("Masukan no hp: "))
    sts = int(input("Masukan status: "))

    con = mydb.cursor()
    sql = "INSERT INTO `admin` (`NIK`, `nama`, `alamat`, `jenkel`, `no_hp`, `status`) VALUES (%s,%s,%s,%s,%s,%s);"
    val = (nik,name,alamat,jk,hp,sts)
    con.execute(sql,val)

    mydb.commit()

    print(con.rowcount," Data berhasil di tambahkan")
