import mysql.connector,lihat_data_admin

def mian():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )
    con = mydb.cursor()

    lihat_data_admin.main()

    nik = int(input("Masukan nik: "))
    sql = "DELETE FROM admin WHERE NIK = %s;"
    val = (nik,)
    con.execute(sql,val)

    mydb.commit()

    print(con.rowcount," Data berhasil di hapus")