import mysql.connector,lihat_data_admin

def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )
    con = mydb.cursor()
    lihat_data_admin.main()

    st = input("Masukan Status yang ingin di ganti: ")
    nik = int(input("NIK yang ingin di ganti: "))

    sql = "UPDATE admin SET status = %s WHERE NIK = %s;"
    val = (st,nik)
    
    con.execute(sql,val)

    mydb.commit()

    print(con.rowcount," Data berhasil di ubah")