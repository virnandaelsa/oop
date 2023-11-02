import mysql.connector
import Admin.lihat_data_admin as a

def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )
    con = mydb.cursor()

    a.main()

    nik = int(input("Masukan nik: "))
    sql = "DELETE FROM admin WHERE NIK = %s;"
    val = (nik,)
    con.execute(sql,val)

    mydb.commit()

    print(con.rowcount," Data berhasil di hapus")