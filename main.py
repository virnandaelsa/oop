import mysql.connector
from sys import path

path.append("C:\\Users\\ACER\\Documents\\pbl\\Admin")
path.append("C:\\Users\\ACER\\Documents\\pbl\\Kamar")

from Admin import Admin
from Kamar import Kamar
import adm
import penyewa
import pemilik

def db():
    db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "db_py_kelompok"
        )
    return db

def make_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        cur = db.cursor()
        sql = "CREATE DATABASE db_py_kelompok;"
        cur.execute(sql)

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "db_py_kelompok"
        )
        cur = db.cursor()
        sql = "CREATE TABLE user(id INT(9) AUTO_INCREMENT PRIMARY KEY, NIK VARCHAR(20), nama VARCHAR(100),alamat VARCHAR(255), jenkel VARCHAR(55), no_hp VARCHAR(12), status VARCHAR(55), username VARCHAR(255) UNIQUE, password VARCHAR(255))"
        cur.execute(sql)

        print("Berhasil membuat database")
    except Exception as e: pass

def login(username, password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "db_py_kelompok"
    )
    cur = db.cursor()

    # Periksa kredensial pengguna di database
    sql = "SELECT * FROM user WHERE username = %s"
    val = (username,)
    cur.execute(sql, val)
    result = cur.fetchone()

    # print(result)
    if result:
        value = result
        # print(value[-1])
        if password == value[-1]:
            print("Login berhasil.")
            return result
        else:
            print("Login gagal. Password salah.")
    else:
        print("Login gagal. Username tidak ditemukan.")

if __name__ == "__main__":
    make_db()
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    logged_in_username = login(username, password)

    # print(logged_in_username[-3])
    if logged_in_username:
        if logged_in_username[-3].lower() == "admin":
            # admin_con = Admin.Admin()
            # kamar_con = Kamar.Kamar()
            adm.DATA_USER.append(logged_in_username)
            adm.main()
            # print(adm.data_user)

        elif logged_in_username[-3].lower() == "pemilik":
            # admin_con = Admin.Admin()
            # kamar_con = Kamar.Kamar()
            pemilik.DATA_USER.append(logged_in_username)
            pemilik.main()

        else:
            # admin_con = Admin.Admin()
            # kamar_con = Kamar.Kamar()
            penyewa.DATA_USER.append(logged_in_username)
            penyewa.main()