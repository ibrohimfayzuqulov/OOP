
     # class Mashina:
#     def __init__(self, model, yil, rang):
#         self.model = model
#         self.yil = yil
#         self.rang = rang

# matiz = Mashina("matiz", 2000, "qora")
# print(matiz.yil)

class moshina:
    def __init__(self,model,yil,rang):
        self.model = model
        self.yil = yil
        self.rang = rang
    
    def boshlash(self):
        print("mashina boshlandi")

    def signal(self):
        print("segnal chaldi")

    def tohtadi(self):
        print("tohtadi")

mustang = moshina("malebu",2021,"malla")
# print(mustang.model)

mustang.boshlash()
mustang.signal()
mustang.tohtadi()
        

