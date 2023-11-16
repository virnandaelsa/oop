import os
import mysql.connector
from sys import path
path.append('C:\\Users\\ACER\\Documents\\pbl\\Admin')
path.append('C:\\Users\\ACER\\Documents\\pbl\\Kamar')

from Admin import Admin
from Kamar import Kamar
from Penyewa import Penyewa

__db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_py_kelompok"

)
cur = __db.cursor()

DATA_USER = []

def main_menu():
    # os.system("cls" if os.name == "nt" else "clear")
    print(f"Selamat datang, {DATA_USER[0][2]} (Pengguna biasa)!")
    print("Menu Pilihan:")
    print("1. Lihat Data diri")
    print("2. Ubah Data diri")
    print("3. Keluar")

def main():
    admin_con = Admin.Admin()
    kamar_con = Kamar.Kamar()
    penyewa_con = Penyewa.Penyewa()
    penyewa_con.DATA_USER = DATA_USER

    while True:

        main_menu()
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

# if __name__ == "__main__":
#     try:
#         sql = "CREATE DATABASE db_py_kelompok;"
#         cur.execute(sql)
#     except Exception as e:
#         pass
#     main()
