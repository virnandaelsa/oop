from sys import path
path.append('C:\\Users\\ACER\\Documents\\')

import pbl.kamar as k
data_master = {} 

def main_menu(): 
    global data_master 
 
    print("################################################") 
    print("####### SISTEM INFORMASI MANAJEMEN KOS #########") 
    print("################################################") 
    print() 
 
    while True: 
        print("\nSelamat Datang admin ") 
        print("silahkan pilih menu di bawah ini:") 
        print("1) lihat data") 
        print("2) tambah data") 
        print("3) ubah data") 
        print("4) hapus data") 
        print("5) lihat data kamar") 
        print("6) keluar") 
 
        choice = input("Pilih menu: ") 
 
        if choice == "1": 
            if not data_master: 
                print("Master data kosong.") 
            else: 
                tampil() 
 
        elif choice == "2": 
            print("Informasi Kamar")
            k.info_kamar("01")
            k.info_kamar("02")
            k.info_kamar("03")
            print("Masukkan data diri anda dengan benar")
            nik = int(input("Masukkan nomor NIK anda : "))  
            nama = (input("Masukkan Nama Anda : "))  
            kamar = (input("Masukkan pilihan kamar Anda : "))  
            alamat = (input("Masukkan alamat anda : "))  
            email = (input("Masukkan email anda : "))  
            data_master[nama] = {"NIK" : nik,"Email": email, "Alamat": alamat, "kamar":kamar}
            print(f"Data '{nama}' berhasil ditambahkan!")
             
        elif choice == "3": 
            tampilNama()

            nama = input("Masukan nama yang ingin di ganti: ") 
            if nama in data_master: 
                print(f"Data saat ini:") 
                print(f"NIK: {data_master[nama]['NIK']}") 
                print(f"Nama: {nama}") 
                print(f"Kamar NO: {data_master[nama]['kamar']}") 
                print(f"Email: {data_master[nama]['Email']}") 
                print(f"Alamat: {data_master[nama]['Alamat']}") 
                data_master[nama]["Email"] = input("Masukan email baru: ") 
                data_master[nama]["Alamat"] = input("Masukan Alamat baru: ") 
                data_master[nama]["kamar"] = input("Masukan No Kamar baru: ") 
                print(f"Date '{nama}' Berhasil di ganti!") 
            else: 
                print(f"Date '{nama}' Tidak ada.") 
 
        elif choice == "4": 
            tampilNama() 
            nama = input("masukan nama yang ingin di hapus: ") 
            if nama in data_master: 
                del data_master[nama] 
                print(f"Date '{nama}' Berhasil menghapus!") 
            else: 
                print(f"Date '{nama}' Tidak ada.") 
 
        elif choice == "5": 
            k.info_kamar("01")
            k.info_kamar("02")
            k.info_kamar("03")

        elif choice == "6": 
            print("Keluar.") 
            exit()
 
        else: 
            print("Pilihan tidak ada.") 
 
def tampil(): 
    global data_master 
    print("Master data:") 
    for key, value in data_master.items(): 
        print(f"NIK: {value['NIK']}") 
        print(f"Name: {key}") 
        print(f"Kamar NO: {value['kamar']}") 
        print(f"Email: {value['Email']}") 
        print(f"Alamat: {value['Alamat']}") 
        print() 
 
def tampilNama():
    print("Master data:") 
    for key, value in data_master.items(): 
        print(f"Name: {key}") 
 
def login(): 
 a = "admin"  
 password = "123"  
   
 while True: 
  user = input("Username: ")  
  Password = input("Password : ")  
   
  if user == a and Password== password:
    k.tambah_kamar("01", ["AC", "Kamar Mandi Dalam", "TV","Lemari","Meja Kerja"])
    k.tambah_kamar("02", ["Kipas Angin", "Lemari", "Meja Kerja"])
    k.tambah_kamar("03", ["Kipas Angin", "Kamar Mandi Dalam","Meja Kerja"])
    main_menu() 
  else: 
   print("Masukkan Username dan Password dengan benar")  

if __name__ == "__main__": 

    login()

 