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
    print("1. Tambah Data Kamar")
    print("2. Lihat Data Kamar")
    print("3. Edit Data Kamar")
    print("4. Hapus Data Kamar")
    print("5. Lihat Data Penyewa")
    print("6. Keluar")

def main():
    admin_con = Admin.Admin()
    kamar_con = Kamar.Kamar()

    while True:
        main_menu()
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
        elif choice == "8":
            print("Keluar dari program.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    try:
        sql = "CREATE DATABASE db_py_kelompok;"
        cur.execute(sql)
    except Exception as e:
        pass
    main()

