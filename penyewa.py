# from Admin import delete_data_admin,insert_data_admin,update_data_admin,lihat_data_admin
# from penyewa import *
# import penyewa.insert_data as i
# import penyewa.delete_penyewa as d
# import penyewa.lihat_data as l
# import penyewa.update as u

# while True:
try:
    while True :
        print (""" 
        Menu Pilihan 
            1. Lihat data penyewa
            2. Tambah Penyewa
            3. Ubah data penyewa 
            4. Hapus data penyewa
            5. keluar""")
        usr = int(input("Silahkan pilih menu : "))
        
        if usr > 5 or usr < 1:
            print("Masukan tidak valid pilih 1-5 ")
            continue
        if usr == 1:
            l.main()
        elif usr == 2:
            i.main()
        elif usr == 3:
            u.main()
            break
        elif usr == 4:
            d.mian()
        elif usr == 5:
            exit()     
except Exception :
    pass
    # print(Exception)
    # print("\nMasukan Harus berupa angka")