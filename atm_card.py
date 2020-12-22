class ATMCard:
    def __init__(self, default_pin, default_balance):
        self.__default_pin = default_pin
        self.__default_balance = default_balance

    @property
    def default_pin(self):
        pass

    @default_pin.getter
    def default_pin(self):
        return self.__default_pin

    @property
    def default_balance(self):
        pass

    @default_balance.getter
    def default_balance(self):
        return self.__default_balance