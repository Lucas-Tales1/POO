import math

class EQ2:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    def calc_delt(self):
        return self.__b * self.__b -4 * self.__a * self.__c 
    def bhask1(self):
        delt = self.calc_delt()
        return (-1 * self.__b + math.sqrt(delt))/ (2 * self.__a)
    def bhask2(self):
        delt = self.calc_delt()
        return (-1 * self.__b - math.sqrt(delt))/ (2 * self.__a)
    def y(self,x):
        return self.__a * x * x + self.__b * x + self.__c
    def set_a(self,v):
        if self.__a == 0:
            raise ValueError("Valor inválido")
        else:
            self.__a = v
    def set_b(self,v):
        self.__b = v
    def set_c(self,v):
        self.__c = v
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def __str__(self):
        return f"a = {self.__a} / b = {self.__b} / c = {self.__c}"


    