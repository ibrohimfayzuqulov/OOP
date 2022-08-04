class Avto:
    def __init__(self,make,model,rang,yil,narx):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        # Avto.__num_avto += 1

    def __repr__(self):
        return f"Avto: {self.make} {self.model}"        


avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Qora",2020,40000)
dir(Avto)
['_Avto__num_avto',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'make',
 'model',
 'narh',
 'rang',
 'yil']

# """obyektlarni taqqoslash"""
x,y=10,20
print(x>y)
print(x<y)

#kattami
def __eq__(self,y):
    return self.narh==y.narh
print(avto1==avto2)
#kichkinami
def __lt__(self):
    return self.narh<y.narh
# print(avto1<avto2)
#obyektni uzunligini qaytaruvchi method
tanish = ("assalomu alekum")
len(tanish)
#misol uchun avto salonda nechta mashina borligini aniqlamoqchimiz

