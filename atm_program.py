import random
import datetime

from customer import Customer

customer = Customer(random.randint(0,99999))
condition = True

while condition:
    limit = 1
    id = int(input("Masukkan pin Anda: "))

    while customer.checkPin(id):
        pass  