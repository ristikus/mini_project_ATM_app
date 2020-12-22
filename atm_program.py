import random
import datetime

from customer import Customer

customer = Customer(random.randint(0,99999))

while True:
    id = int(input("Masukkan pin Anda: "))
    trial = 1

    while not customer.check_pin(id) and trial < 3:
        id = int(input("Pin anda salah. Silakan masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi...")
            exit()

    while True:
        print("---------------------")
        print("Selamat datang di ATM")
        print("1. Cek Saldo")
        print("2. Debit")
        print("3. Simpan")
        print("4. Ganti pin")
        print("0. Keluar")
        
        selected_menu = int(input("Pilihan menu: "))

        if selected_menu == 1:
            print("Saldo anda Rp. " + str(customer.check_balance()) + "\n")
        elif selected_menu == 2:
            pass
        elif selected_menu == 3:
            pass
        elif selected_menu == 4:
            pass
        elif selected_menu == 0:
            print("")
            break
        else:
            pass