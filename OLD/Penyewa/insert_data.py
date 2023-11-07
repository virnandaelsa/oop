import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO penyewa (NIK, nama, alamat, jenkel, kampus, no_hp, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = [
        ("23102816772", "Anandya", "Kediri", "Perempuan", "Politeknik Negeri Malang", "0851231552918", "mahasiswa"),
        ("23710029188", "Angelina", "Pasuruan", "Perempuan", "Universitas Islam Kadiri", "0815532718771", "mahasiswa"),
        ("23710281762", "Bunga", "Nganjuk", "Perempuan", "Universitas Kadiri", "0882018155287", "mahasiswa")
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Data penyewa berhasil ditambahkan...")