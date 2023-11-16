import mysql.connector
import os
from sys import path
path.append('C:\\Users\\ACER\\Documents\\pbl\\Admin')
path.append('C:\\Users\\ACER\\Documents\\pbl\\Kamar')

import Admin
import kamar

__db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_py_kelompok"
)
cur = __db.cursor()

DATA_USER = []

def main_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"SELAMAT DATANG ADMIN {DATA_USER[0][2]}")
    print("Menu Pilihan:")
    print("1. Lihat data Penyewa")
    print("2. Tambah Data Penyewa")
    print("3. Ubah data Penyewa")
    print("4. Hapus data Penyewa")
    print("5. Tambah Data kamar")
    print("6. Lihat Data Kamar")
    print("7. Hapus Data Kamar")
    print("8. Keluar")

def main():
    admin_con = Admin()
    kamar_con = kamar()

    while True:
        main_menu()
        choice = input("Pilih menu (1/2/3/4/5/6/7/8): ")

        if choice == "1":
          try :
            admin_con.show_data()
          except Exception :
              print ("data belum ada")
        elif choice == "2":
            nik = input("Masukkan NIK : ")
            name = input("Masukkan nama : ")
            alamat = input("Masukkan alamat : ")
            jk = input("Masukkan jenis kelamin : ")
            hp = input("Masukkan no hp : ")
            sts = input("Masukkan status: ")
            username = input("Masukkan username: ")
            pw = input("Masukkan password: ")
            admin_con.insert_data(nik, name, alamat, jk, hp, sts, username, pw)
        elif choice == "3":
            admin_con.show_data()
            nik = input("Masukkan NIK yang akan diganti: ")
            name = input("Masukkan nama baru: ")
            alamat = input("Masukkan alamat baru: ")
            jk = input("Masukkan jenis kelamin baru: ")
            hp = input("Masukkan no hp baru: ")
            sts = input("Masukkan status baru: ")
            admin_con.update_data(nik, name, alamat, jk, hp, sts)
        elif choice == "4":
            admin_con.show_data()
            nik = input("Masukkan NIK yang akan dihapus: ")
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
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# if __name__ == "__main__":
#     try:
#         sql = "CREATE DATABASE db_py_kelompok;"
#         cur.execute(sql)
#     except Exception as e:
#         pass
#     main()
