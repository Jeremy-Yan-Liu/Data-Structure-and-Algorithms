class Flower:

    def __init__(self, name, numPetal, price):

        self._name = name
        self._numPetal = numPetal
        self._price = price

    def get_price(self):

        return self._price

    def get_numPetal(self):

        return self._numPetal

    def get_name(name):
        return self._name

    def update_price(self, new_price):

        self._price = new_price

    def update_name(self,new_name):

        self._name = new_name

    def update_price(self,new_numPetal):

        self._numPetal = new_numPetal
