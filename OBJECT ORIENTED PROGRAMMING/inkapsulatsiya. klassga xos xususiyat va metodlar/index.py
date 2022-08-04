from uuid import uuid4
class Avto:
    """avtomobil klasi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto



    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self,km):
        """manshinani km ga km qo'shish"""
        if km>=0:
            self.__km += km
        else:
                print("mashina km kamaytirib bo'lmaydi")


avto1 = Avto("GM","Malibu","Qora",2022,30000,1000)  
avto2 = Avto("GM","Lacetti","oq",2018,25000,2000)  
avto3 = Avto("GM","captiva","Qora",2019,40000,1300)  
print(avto1.model)
print(avto1)
print(avto2)
print(avto3)
print(avto1.get_num_avto())

print(avto1.add_km(-2000))

print(avto1.get_km())
print(avto1.get_id())


# klasni imort qilish misol:(from avto import Avto)
# hamma klaslarni chaqrib olishh misol:(from avto import *) lekin bunday qilish tavsiya qilinmaydi sababi klasslar kopayib ketgandan kiyin siz qaysi bir klasni ishlatganigizni bilmaysiz

