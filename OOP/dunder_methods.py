
class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
    
    def __eq__(self, y):
        return self.narh == y.narh
    
    def __lt__(self, y):
        return self.narh < y.narh
    
    def __le__(self, y):
        return self.narh <= y.narh

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Malibu", "Qora", 2020, 40000)
# print(avto1 < avto2)

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self, index, value):
        if isinstance(value, Avto):
            self.avtolar[index] = value
    
    def add_avto(self, avto):
        if isinstance(avto, Avto): # agar avto Avto klassidan bo'lsa
            self.avtolar.append(avto)
        else:
            print("Avto obyketini kiriting")


salon1 = AvtoSalon("MaxAvto")

# Avto obyektlarini yaratamiz
avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", 'Supra', "Silver", 2018, 45000)

# Yuqoridagi obyektlarni salon1 ga qo'shamiz
for avto in [avto1, avto2, avto3]: 
    salon1.add_avto(avto)