import random
import datetime

from customer import Customer

customer = Customer(random.randint(0,99999))

while True:
    trial = 0
    id = int(input("Masukkan pin Anda: "))

    while customer.checkPin(id) and trial < 3:
        id = int(input("Pin anda salah. Silakan masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("Error. Silakan ambil kartu dan coba lagi...")
            exit()
