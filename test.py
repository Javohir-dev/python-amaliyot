# Python Amaliyotlari


# =============================================================================
# # Enter the number you want.
# # 45.2
# # 45
# # 45 ning kvadrati 2025 ga teng
# # 45 ning kubi 91125 ga teng
# 
# def count_number():
#     stop = True
#     while stop:
#         number = input('Hohlagan raqamingizni kiriting.\n>>> ')
#         if number:
#             number = float(number)
#             number = int(number // 1)
#             print(number)
#             print(f"{number} ning kvadrati {number**2} ga teng")
#             print(f"{number} ning kubi {number**3} ga teng")
#             break
#             
#         else:
#             print("==============================")
#             print("\nBo'sh ma'mulot qabul qila olmaymiz.\n")
#             print("==============================")
# =============================================================================


import datetime
# =============================================================================
# # Yoshingiz nechida?
# # 22
# # Siz 2001-yilda tug'ilgansiz.
# def find_birthdate():
#     now = datetime.datetime.now()
#     stop = True
#     while stop:
#         age = input("Yoshingiz nechida?\n>>> ")
#         if age:
#             age = float(age)
#             second_age = age // 1
#             if second_age == age:
#                 stop = False
#                 age = int(age)
#                 print(f"Siz {now.year - age}-yilda tug'ilgansiz.")
#             else:
#                 print("==============================")
#                 print("\nIltimos butun son kiriting.\n")
#                 print("==============================")
#         else:
#             print("==============================")
#             print("\nBo'sh ma'mulot qabul qila olmaymiz.\n")
#             print("==============================")
# =============================================================================


# =============================================================================
# # Funksiyalar
# def full_name(first_name, last_name="kiritilmagan"):
#     fullname = f"{first_name} {last_name}"
#     
#     return fullname
#     
# fullname = full_name("javohir", "khamidullaev") 
# # print(fullname.title())
# fullname = full_name(last_name="qahramoniy", first_name="azam") 
# # print(fullname.title()) 
# 
# 
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rangi,
#         'korobka':korobka,
#         'yil':yili,
#         'narh':narhi
#     }
#     
#     return avto
# 
# 
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# 
# print('Onlayn bozordagi mavjud avtomashinalar:')
# 
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
# 
# 
# def my_range(min, max, step=1):
#     sonlar = [] # bo'sh ro'yxat
#     while min < max:
#         sonlar.append(min)
#         min += step
#     return sonlar
# 
# 
# lst = my_range(0, 20, 2)
# 
# 
# def num(one, two, three):
#     n = {
#         'one': one,
#         'two': two,
#         'three': three ,   
#     }
#     
#     return n
# numbers = []
# one = 1
# two = 2
# three = 3
# numbers.append(num(one, two, three))
#     
# one = 10
# two = 20
# three = 30
# numbers.append(num(one, two, three))
# =============================================================================


# funsiya ro'yhatlar bilan
# =============================================================================
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baholar[ism] = int(input(f"{ism}ga nechi baho qo'yildi?\n>>> "))
#     
#     return baholar
# 
# talabalar = ["Javohir", "Bunyod", 'Jahongir', 'Akbar']
# baholandi = bahola(talabalar[:])
# =============================================================================

# =============================================================================
# # *args **kwargs
# def summa(x, y, *args):
#     return x + y + sum(args)
# 
# number = summa(1, 2, 3, 4, 56, 7, 8, 9)
# 
# def avto_info(kompaniya,model,**kwargs):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     kwargs['kompaniya']=kompaniya
#     kwargs['model']=model
#     return kwargs
# 
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000, km=13000)
# 
# =============================================================================

# Math
# =============================================================================
# import math as m
# 
# print(m.pi)
# 
# import random as r
# 
# num = r.randint(1, 1024)
# print(num)
# 
# name = ['olim','anvar','hasan','husan']
# 
# print(r.choice(name))
# 
# 
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))
# 
# 
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)
# 
# =============================================================================


# =============================================================================
# # Lambda
# result = lambda x, y: x ** y
# 
# # print(result(12, 2))
# n = result(6, 2)
# 
# def daraja(n):
#     return lambda x : x**n
# 
# kvadrat = daraja(2)
# kub = daraja(3)
# # print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")
# 
# def func(i):
#     return lambda x : x + i
# 
# ikki = func(2)
# olti = func(6)
# # print(f"3 + 2 = {ikki(3)}\n3 + 6 = {olti(3)}")
# 
# numbers = list(range(11))
# kvadrat = list(map(lambda x : x*x, numbers))
# 
# import random as r
# numbers2 = r.sample(range(101), 10)
# juft_son = list(filter(lambda num: num%2==0, numbers2))
# print(juft_son)
# 
# 
# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
# 
# mevalar_b = list(filter(lambda meva:meva.startswith('a'),mevalar))
# print(mevalar_b)
# =============================================================================



import json
from pprint import pprint

# x = 10
# x_json = json.dumps(x)

# ism = "anvar"
# ism_json = json.dumps(ism)

# sonlar = [12, 45, 23, 67]
# sonlar_json = json.dumps(sonlar)

# bemor = {
#   "ism": "Alijon Valiyev",
#   "yosh": 30,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }

# bemor_json = json.dumps(bemor)
# with open('bemor.json','w') as f:
#     json.dump(bemor,f)

# sonlar = json.loads(sonlar_json)
# bemor = json.loads(bemor_json)
# # pprint(bemor)



# import pickle

# talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
# talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

# with open('info','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)

# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
    
# print(talaba1)

# =============================================================================
# age = input("Yoshingizni kiriting: ")
# 
# try:
#     print(int(age))
# except ValueError:
#     print("Butun son kiriting!")
# print(int(age))
# print("Dastur ishlayapti.")
# =============================================================================


# def main(N):
#     x = 0
#     for n in list(range(1, N+1)):
#         x += n
    
#     return x

# def main(N):
#     return N*(N+1)//2

# # print(main(100))

# def sarala(lst):
#     return sorted(lst)

# numbers = [1, 2, 5, 6, 8, 3, 9]

# # print(sarala(numbers))

# text = "Khamidullaev Javohir"
# text = text.replace(" ", "")
# lst = list(text)
# # print(lst)

# def tub_sonlar_oraliq(olcham):
#     tublar = []
#     for son in range(2, olcham + 1):
#         tub = True
#         for i in range(2, int(son**0.5) + 1):
#             if son % i == 0:
#                 tub = False
#                 break
#         if tub:
#             tublar.append(son)
#     return tublar

# olcham = 30
# natija = tub_sonlar_oraliq(olcham)
# print(natija)  # Natija: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def faktorial(son):
    if son == 0:
        return 1
    else:
        return son * faktorial(son - 1)

def faktoriallar(N):
    fakt = 1
    i = 1
    while i != N+1:
        fakt *= i
        i += 1

    return fakt



def  main(N):
    if N == 0:
        return 1
    else:
        return N * main(N - 1)
    
# print(main(5))
# print(faktoriallar(5))


def fibanachi(x):
    fib = [0, 1]
    while len(fib) < x:
        fib.append(fib[-1] + fib[-2])
    
    return fib

# print(fibanachi(10))
    
    
    
    
def toplam_top(toplam):
 
    return sum(toplam)

n = [2, 3, 5, 7, 11, 13, 17, 19, 23, 28]

    
    
def test(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        
    return fib


def test1(x):
    tublar = []
    for t in list(range(1, x+1)):
        if t / 1 % 2 == 0 and t / t % 2 == 0:
            tublar.append(t)
    
    return tublar




def tub_sonlar_top(n):
    tublar = []
    for son in range(2, n + 1):
        is_tub = True
        for i in range(2, int(son ** 0.5) + 1):
            if son % i == 0:
                is_tub = False
                break
        if is_tub:
            tublar.append(son)
    return tublar

# n = int(input("N raqamini kiriting: "))
# tublar = tub_sonlar_top(n)
# print(f"{n} gacha bo'lgan tub sonlar: {tublar}")

class Test:
    def __init__(self, ism, familiya):
        self.familiya = familiya
        self.__ism = ism
        
    def show_name(self):
        return self.__ism
        
    def __repr__(self):
        
        return f"{self.__ism} {self.familiya}"
        



man = Test("Javohir", "Khamidullaev")





