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

    st = input("Masukan Status yang ingin di ganti: ")
    nik = int(input("NIK yang ingin di ganti: "))

    sql = "UPDATE admin SET status = %s WHERE NIK = %s;"
    val = (st,nik)
    
    con.execute(sql,val)

    mydb.commit()

    print(con.rowcount," Data berhasil di ubah")