from atm_card import ATMCard

class Customer:
    def __init__(self, id, cust_pin = 1234, cust_balance = 10000):
        self.__id = id
        self.__atm = ATMCard(cust_pin, cust_balance)

    @property
    def id(self):
        pass

    @id.getter
    def id(self):
        return self.__id

    @property
    def cust_pin(self):
        pass

    @cust_pin.setter
    def cust_pin(self, new_pin):
        self.__atm.default_pin = new_pin

    def check_balance(self):
        return self.__atm.default_balance

    def check_pin(self, input_pin):
        if self.__atm.default_pin == input_pin:
            return True
        else:
            return False

    def withdraw_balance(self, nominal):
        self.__atm.default_balance -= nominal

    def deposit_balance(self, nominal):
        self.__atm.default_balance += nominal