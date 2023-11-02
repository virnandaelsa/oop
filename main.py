from Admin import delete_data_admin,insert_data_admin,update_data_admin,lihat_data_admin


while True:
    try:
        while True :
            print (""" 
            Menu Pilihan 
                1. Lihat data Admin
                2. Tambah Pengeluaran
                3. Ubah data Admin 
                4. Hapus data admin 
                5. keluar""")
            usr = int(input("Silahkan pilih menu : "))
            
            if usr > 4 or usr < 1:
                print("Masukan tidak valid pilih 1-4 ")
                continue

            if usr == 1:
                lihat_data_admin.main()
            elif usr == 2:
                insert_data_admin.main()
            elif usr == 3:
                update_data_admin.main()
                break
            elif usr == 4:
                delete_data_admin.mian()
            elif usr == 5:
                exit        
    except:
        print("\nMasukan Harus berupa angka")