fasilitaskos = {}

def tambah_kamar(nomor_kamar, fasilitas):
    fasilitaskos[nomor_kamar] = fasilitas

def info_kamar(nomor_kamar):
    if nomor_kamar in fasilitaskos:
        print(f"Informasi Kamar {nomor_kamar}:")
        for fasilitas in fasilitaskos[nomor_kamar]:
            print(f"- {fasilitas}")
    else:
        print(f"Kamar {nomor_kamar} tidak ditemukan.")