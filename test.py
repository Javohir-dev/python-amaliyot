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


# Funksiyalar
def full_name(first_name, last_name="kiritilmagan"):
    fullname = f"{first_name} {last_name}"
    
    return fullname
    
fullname = full_name("javohir", "khamidullaev") 
# print(fullname.title())
fullname = full_name(last_name="qahramoniy", first_name="azam") 
# print(fullname.title()) 


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'korobka':korobka,
        'yil':yili,
        'narh':narhi
    }
    
    return avto


avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]

print('Onlayn bozordagi mavjud avtomashinalar:')

for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


def my_range(min, max, step=1):
    sonlar = [] # bo'sh ro'yxat
    while min < max:
        sonlar.append(min)
        min += step
    return sonlar


lst = my_range(0, 20, 2)


def num(one, two, three):
    n = {
        'one': one,
        'two': two,
        'three': three ,   
    }
    
    return n
numbers = []
one = 1
two = 2
three = 3
numbers.append(num(one, two, three))
    
one = 10
two = 20
three = 30
numbers.append(num(one, two, three))