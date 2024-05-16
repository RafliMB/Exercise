stok = []
def tambah():
    nama_barang = input("Masukkan nama barang : ")
    stok_barang = input("Masukkan stok barang : ")
    barang = {"nama" : nama_barang, "stok" : stok_barang}
    stok.append(barang)
    return "--- Data berhasil ditambahkan ---"

def hapus():
    delete = int(input("Hapus data index ke : "))
    delete -= 1
    del stok[delete]
    return "--- Data berhasil dihapus ---"

def tampil():
    print("--- Data barang ---")
    number = 1
    for i in stok:
        print(f"{number}. {i["nama"]} , Stok : {i["stok"]}")
        number += 1
    return ""