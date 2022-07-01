from Calc import Calc

class Binary(Calc):
    def toBinary(self, dec):
        return bin(dec)[2:]

    def toDec(self, bin):
        return int(bin, 2)