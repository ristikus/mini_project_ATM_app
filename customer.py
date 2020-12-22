from atm_card import ATMCard

class Customer:
    def __init__(self, id, cust_pin = 1234, cust_balance = 10000):
        self.__id = id
        self.__cust_pin = 1234
        self.__cust_balance = 10000

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
        return self.__cust_pin

    @property
    def cust_balance(self):
        pass

    @cust_balance.getter
    def cust_balance(self):
        return self.__cust_balance

    def debt(self, nominal):
        self.__cust_balance -= nominal

    def saving(self, nominal):
        self.__cust_balace += nominal