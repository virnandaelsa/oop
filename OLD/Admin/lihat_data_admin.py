import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )

   
    con = mydb.cursor()
    sql = "SELECT * FROM admin"
    con.execute(sql)

    val = con.fetchall()

    # print(val)
    # mydb.commit()
    for key in val:
        print(f"NIK :{key[1]} |",end="")
        print(f"Nama :{key[2]} |",end="")
        print(f"Alamat :{key[2]} |",end="")
        print(f"Jenis Kelamin :{key[4]} |",end="")
        print(f"No hp :{key[5]} |",end="")
        print(f"Status :{key[6]} |")
    # print(con.rowcount," Data berhasil di tambahkan")
