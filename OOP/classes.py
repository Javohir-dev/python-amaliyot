import datetime

now = datetime.datetime.now().year

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_name(self):
        return self.ism
    
    def get_last_name(self):
        return self.familiya
    
    def get_fullname(self):
        return f"{self.get_name()} {self.get_last_name()}".title()
    
    def get_email(self, email, password):
        return f"{email} {password}"
        
    def get_subject(self, fan):
        self.fan = fan
        return f"Men endi {fan.title()}ni ham o'qiyman"
    
    def get_age(self):
        return now - self.tyil
    
    def get_bosqich(self):
        return self.bosqich
        
    def update_bosqich(self):
        if self.bosqich < 4:
            self.bosqich += 1
            return f"{self.bosqich}-kursga o'tkazildi."
        else:
            return "Talaba bitirdi."
    
    def tanishtir(self):
        if self.bosqich < 4:
            return f"Salom, mening ismim {self.get_name().title()} familiyam {self.get_last_name().title()}, {self.get_age()} yoshdaman va men {self.get_bosqich()}-kurs talabasiman."
        else:
            return f"Salom, mening ismim {self.get_name().title()} familiyam {self.get_last_name().title()}, {self.get_age()} yoshdaman va men Universitetni bitirganman."


class Fan():
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_students(self):
        return [ x.get_fullname() for x in self.talabalar ]

talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)

matematika = Fan("Oliy Matematika")

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

def see_methods(klass):
    return [ method for method in dir(klass) if method.startswith('__') is False ]
