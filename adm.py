# from Admin import delete_data_admin,insert_data_admin,update_data_admin,lihat_data_admin
# from Admin import *
# import Admin.lihat_data_admin as a
import Admin.lihat_data_admin as a
import Admin.insert_data_admin as i
import Admin.delete_data_admin as d
import Admin.update_data_admin as u

# while True:
#     try:
while True :
    print (""" 
    Menu Pilihan 
        1. Lihat data Admin
        2. Tambah Pengeluaran
        3. Ubah data Admin 
        4. Hapus data admin 
        5. keluar""")
    usr = int(input("Silahkan pilih menu : "))
    
    if usr > 5 or usr < 1:      
        print("Masukan tidak valid pilih 1-5 ")
        continue
    if usr == 1:
        a.main()
    elif usr == 2:
        i.main()
    elif usr == 3:
        u.main()
        break
    elif usr == 4:
        d.main()
    elif usr == 5:
        exit()     
    # except Exception :
    #     # print(Exception)
    #     print("\nMasukan Harus berupa angka")