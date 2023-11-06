from sys import path
path.append('C:\\Users\\ACER\\Documents\\pbl\\Admin')

from Admin import Admin

def main_menu():
    print("Menu Pilihan:")
    print("1. Lihat data Admin")
    print("2. Tambah Data Admin")
    print("3. Ubah data Admin")
    print("4. Hapus data admin")
    print("5. Keluar")

def main():
    admin_con = Admin()
    admin_con.connect()

    while True:
        main_menu()
        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == "1":
          admin_con.lihat()
        elif choice == "2":
            nik = int(input("Masukkan NIK : "))
            name = input("Masukkan nama : ")
            alamat = input("Masukkan alamat : ")
            jk = input("Masukkan jenis kelamin : ")
            hp = int(input("Masukkan no hp : "))
            sts = int(input("Masukkan statusm: "))
            admin_con.insert(nik, name, alamat, jk, hp, sts)
        elif choice == "3":
            nik = int(input("Masukkan NIK yang akan diperbarui: "))
            name = input("Masukkan nama baru: ")
            alamat = input("Masukkan alamat baru: ")
            jk = input("Masukkan jenis kelamin baru: ")
            hp = int(input("Masukkan no hp baru: "))
            sts = int(input("Masukkan status baru: "))
            admin_con.update(nik, name, alamat, jk, hp, sts)
        elif choice == "4":
            nik = int(input("Masukkan NIK yang akan dihapus: "))
            admin_con.delete(nik)
        elif choice == "5":
            print("Keluar dari program.")
            admin_con.close()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
