import mysql.connector
from sys import path
from Admin import Admin

path.append('C:\\Users\\ACER\\Documents\\pbl\\Admin')
__db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)
cur = __db.cursor()

def main_menu():
    print("Menu Pilihan:")
    print("1. Lihat data Admin")
    print("2. Tambah Data Admin")
    print("3. Ubah data Admin")
    print("4. Hapus data admin")
    print("5. Keluar")

def main():
    admin_con = Admin.Admin()

    while True:
        main_menu()
        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == "1":
          admin_con.show_data()
        elif choice == "2":
            nik = int(input("Masukkan NIK : "))
            name = input("Masukkan nama : ")
            alamat = input("Masukkan alamat : ")
            jk = input("Masukkan jenis kelamin : ")
            hp = int(input("Masukkan no hp : "))
            sts = input("Masukkan status: ")
            admin_con.insert_data(nik, name, alamat, jk, hp, sts)
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
