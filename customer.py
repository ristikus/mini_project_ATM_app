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

    @cust_pin.getter
    def cust_pin(self):
        return self.__atm.default_pin

    def check_balance(self):
        return self.__atm.default_balance

    def check_pin(self, input_pin):
        if self.__atm.default_pin == input_pin:
            return True
        else:
            return False

    def debt(self, nominal):
        self.__cust_balance -= nominal

    def saving(self, nominal):
        self.__cust_balace += nominal