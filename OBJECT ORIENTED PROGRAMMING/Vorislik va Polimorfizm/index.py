from distutils.log import info
from turtle import pensize


class shaxs:
    """shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,yil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.yil = yil

    def get_info(self):
        """shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}: \n"
        info += f"passport:{self.passport},\ntug'ulgan yili:{self.yil} "
        return info 


# obyekt
inson = shaxs("hasan","husanov", "FF01122946",2000)
print(inson.get_info())
print(inson.get_age(2022))

# ikkinchi klass
class talaba(shaxs):
    """talaba klasi"""
    def __init__(self, ism, familiya, passport, yil, idraqam):
        """talabani xususiyatlari"""
        super().__init__(ism, familiya, passport, yil)
        self.idraqam = idraqam
        self.bosqich = 1
        
    def get_id(self):
        """talabani id raqami"""
        return self.idraqam

    def get_bosqich(self):
        """talabani o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich}-bosqich. ID raqami{self.get_id}"
        return info 
class manzil:
    """manzil saplash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """manzilni korish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani,"
        manzil += f"{self.kocha} kochasi, {self.uy}-uy" 
        return manzil

talaba1_manzil = manzil(12,"olmazor","bog'bon","samarqand")
talaba1 = talaba("valijon","aliyev","FFA023164",2000,"0000234",talaba1_manzil)        
print(talaba1.get_info())
# obyekt
talaba1 = talaba("alijon","valoyev","FF022259","2001","N0000011")
print(talaba1.get_id())
print(talaba1.get_info())
