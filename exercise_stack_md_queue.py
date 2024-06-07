from queue import LifoQueue

stack = LifoQueue()
second_stack = LifoQueue()

def add():
    user_input = input('Masukkan kata kunci pencarian : ')
    stack.put(user_input)
    print(f'"{user_input}" ditambahkan ke riwayat pencarian.')

def delete():
    item = stack.get()
    second_stack.put(item)
    print(f'"{item}" dihapus dari riwayat pencarian.')

def undo():
    if not second_stack.empty():
        stack.put(second_stack.queue[-1])
        print(f'"{second_stack.queue[-1]}" dikembalikan ke riwayat pencarian.')
        second_stack.get()
    else:
        print('Tidak ada operasi yang bisa di-undo.')

while True:
    print(f'\nRiwayat pencarian saat ini : {stack.queue}')
    print('Pilihan:')
    print('1. Tambah Pencarian')
    print('2. Hapus Pencarian')
    print('3. Undo')
    print('4. Keluar')

    pilihan = int(input('\nPilih operasi (1/2/3/4): '))
    if pilihan == 1:
        add()
        print("")
        print("======================================")
    elif pilihan == 2:
        delete()
        print("")
        print("======================================")
    elif pilihan == 3:
        undo()
        print("")
        print("======================================")
    elif pilihan == 4:
        exit()