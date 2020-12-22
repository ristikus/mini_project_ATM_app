import random
import datetime

from customer import Customer

customer = Customer(random.randint(0,99999))

while True:
    limit = 0
    id = int(input("Masukkan pin Anda: "))

    while customer.checkPin(id) and limit < 3:
        id = int(input("Pin anda salah. Silakan masukkan lagi: "))
        limit += 1

        

