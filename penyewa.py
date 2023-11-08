import mysql.connector
from sys import path
from Admin import Admin
from Kamar import Kamar

path.append('C:\\Users\\ACER\\Documents\\pbl\\Admin')
path.append('C:\\Users\\ACER\\Documents\\pbl\\Kamar')

__db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)
cur = __db.cursor()

def main_menu():
    print("Menu Pilihan:")
    print("1. Ubah username User")
    print("2. Lihat Data kamar")
    print("3. Lihat Data Diri")
    print("4. Keluar")

def main():
    admin_con = Admin.Admin()
    kamar_con = Kamar.Kamar()

    while True:
        main_menu()
        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == "1":
            username = input("Masukkan username yang akan diganti : ")
            admin_con.update_data_penyewa(username)
        elif choice == "2":
            kamar_con.show_kamar()
        elif choice == "3":
            pass
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

if __name__ == "__main__":
    try:
        sql = "CREATE DATABASE db_py_kelompok;"
        cur.execute(sql)
    except Exception as e:
        pass
    main()
