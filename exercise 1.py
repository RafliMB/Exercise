import modul as mod

print("Selamat datang di program manajemen stock barang!")
print("Pilihan :")
print("1. Tambah data barang")
print("2. Hapus data barang")
print("3. Tampilkan data barang")
print("4. Keluar")
print('\n')

while True:
    pilihan = int(input("Masukkan pilihan : "))
    print("=====================================")
    if pilihan == 1:
        print(mod.tambah())
        print("")
    elif pilihan == 2:
        print(mod.hapus())
        print("")
    elif pilihan == 3:
        print(mod.tampil())
    elif pilihan == 4:
        exit()