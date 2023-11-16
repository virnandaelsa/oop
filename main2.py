from sys import path
path.append('C:\\Users\\ACER\\Documents\\pbl\\Kamar')
path.append('C:\\Users\\ACER\\Documents\\pbl\\Admin')
path.append('C:\\Users\\ACER\\Documents\\pbl\\Penyewa')

from Kamar import kamar
from Admin import user
from Penyewa import Penyewa

import mysql.connector
# from Admin import Admin
# from Kamar import kamar

admin_con = user.Admin()
kamar_con = kamar.Kamar()
penyewa_con = Penyewa.penyewa()

def login():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cur = db.cursor()

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Periksa kredensial pengguna di database
    sql = "SELECT username, password FROM user WHERE username = %s"
    val = (username,)
    cur.execute(sql, val)
    result = cur.fetchone()

    if result:
        db_username, db_password = result

        if password == db_password:
            return db_username
        else:
            return None
    else:
        return None

def menu_admin():
    print(f"SELAMAT DATANG ADMIN")
    print("Menu Pilihan:")
    print("1. Lihat data Penyewa")
    print("2. Tambah Data Penyewa")
    print("3. Ubah data Penyewa")
    print("4. Hapus data Penyewa")
    print("5. Tambah Data kamar")
    print("6. Lihat Data Kamar")
    print("7. Hapus Data Kamar")
    print("8. Keluar")

def menu_pemilik():
    print(f"SELAMAT DATANG PEMILIK")
    print("Menu Pilihan:")
    print("1. Tambah Data Kamar")
    print("2. Lihat Data Kamar")
    print("3. Edit Data Kamar")
    print("4. Hapus Data Kamar")
    print("5. Lihat Data Penyewa")
    print("6. Keluar")

def menu_penyewa():
    print(f"Selamat datang, (Pengguna biasa)!")
    print("Menu Pilihan:")
    print("1. Lihat Data diri")
    print("2. Ubah Data diri")
    print("3. Keluar")

def login():
    print("\nSilahkan masukan username dan password ")
    usernamelogin=input("Username : ")
    passwordlogin=input("Password : ")
    status_login=admin_con.login(usernamelogin,passwordlogin)
    return status_login

status_login=login()

while True:
    if status_login =="admin":
        menu_admin()
        choice = input("Pilih menu (1/2/3/4/5/6/7/8): ")
        if choice == "1":
            admin_con.show_data()
        elif choice == "2":
            nik = int(input("Masukkan NIK : "))
            name = input("Masukkan nama : ")
            alamat = input("Masukkan alamat : ")
            jk = input("Masukkan jenis kelamin : ")
            hp = int(input("Masukkan no hp : "))
            sts = input("Masukkan status: ")
            username = input("Masukkan username: ")
            pw = input("Masukkan password: ")
            admin_con.insert_data(nik, name, alamat, jk, hp, sts, username, pw)
        elif choice == "3":
            admin_con.show_data()
            nik = int(input("Masukkan NIK yang akan diganti: "))
            name = input("Masukkan nama baru: ")
            alamat = input("Masukkan alamat baru: ")
            jk = input("Masukkan jenis kelamin baru: ")
            hp = int(input("Masukkan no hp baru: "))
            sts = input("Masukkan status baru: ")
            admin_con.update_data(nik, name, alamat, jk, hp, sts)
        elif choice == "4":
            admin_con.show_data()
            nik = int(input("Masukkan NIK yang akan dihapus: "))
            admin_con.delete_data(nik)
        elif choice == "5":
            kamar_con.insert_kamar()
        elif choice == "6":
            kamar_con.show_kamar()
        elif choice == "7":
            kamar_con.delete_kamar()
        elif choice == "8":
            print("Keluar dari program.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    
    elif status_login == "pemilik":
        menu_pemilik()
        choice = input("Pilih menu (1/2/3/4/5/6): ")
        if choice == "1":
            kamar_con.insert_kamar()
        elif choice == "2" :
            kamar_con.show_kamar()
        elif choice == "3":
            kamar_con.update_kamar()
        elif choice == "4":
            kamar_con.delete_kamar()
        elif choice == "5" :
            admin_con.show_data()
        elif choice == "6":
            print("Keluar dari program.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
    elif status_login == "penyewa":
        menu_penyewa()
        choice = input("Pilih menu (1/2/3): ")

        if choice == "1":
            # username = input("Masukkan username yang akan diganti : ")
            # print(penyewa_con.DATA_USER)
            penyewa_con.lihat_data()
        elif choice == "2":
            penyewa_con.update_data()
        elif choice == "3":
            print("Keluar dari program")
            exit()
            break
        elif choice == "4":
            admin_con.show_data()
            nik = int(input("Masukkan NIK yang akan dihapus: "))
            admin_con.delete_data(nik)
        elif choice == "5":
            print("Keluar dari program.")
            exit()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")





