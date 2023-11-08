import mysql.connector
from sys import path

path.append("C:\\Users\\ACER\\Documents\\pbl\\Admin")
path.append("C:\\Users\\ACER\\Documents\\pbl\\Kamar")

from Admin import Admin
from Kamar import Kamar
import adm
import penyewa
import pemilik

def login(username, password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cur = db.cursor()

    # Periksa kredensial pengguna di database
    sql = "SELECT username, password FROM user WHERE username = %s"
    val = (username,)
    cur.execute(sql, val)
    result = cur.fetchone()

    if result:
        db_username, db_password = result

        if password == db_password:
            print("Login berhasil.")
            return db_username
        else:
            print("Login gagal. Password salah.")
    else:
        print("Login gagal. Username tidak ditemukan.")

if __name__ == "__main__":
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    logged_in_username = login(username, password)

    if logged_in_username:
        if logged_in_username == "admin":

            admin_con = Admin.Admin()
            kamar_con = Kamar.Kamar()
            adm.main_menu(admin_con, kamar_con)
        elif logged_in_username == "pemilik":

            admin_con = Admin.Admin()
            kamar_con = Kamar.Kamar()
            pemilik.main_menu(admin_con, kamar_con)
        else:
            print(f"Selamat datang, {logged_in_username} (Pengguna biasa)!")
            admin_con = Admin.Admin()
            kamar_con = Kamar.Kamar()
            penyewa.main_menu()
            


