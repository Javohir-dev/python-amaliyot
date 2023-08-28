import random as r

def son_top_pc(x, y):
    urinish = 1
    savol = f"{x}dan {y}gacha bo'lgan bir son o'yladim topa olasizmi?\n>>> "
    num = r.randint(x, y)
    while True:
        javob = int(input(savol))
        if javob >= x and javob <= y:
            if javob == num:
                print("=========================")
                print(f"Ha to'g'ri topdingiz men {num}ni o'ylagan edim. Siz {urinish}ta urinishda topdingiz.")
                print("=========================")
                return urinish
                break
            elif javob < num:
                print("=========================")
                print("Xato! Bu sondan kattaroq.")
                print("=========================")
                urinish += 1
            elif javob > num:
                print("==========================")
                print("Xato! Bu sondan kichikroq.")
                print("==========================")
                urinish += 1
        else:
            print("Noto'gri qiymat kiritdingiz! Iltimos qaytadan urinib ko'ring.")
            
# sontop = son_top_pc(1, 10)

def son_top_my(x, y):
    print(f"{x}dan {y}gacha bo'lgan bir son o'ylang. Endi men topishga urinib ko'raman.")
    input("Tayyor bo'lsangiz Enterni bosing. ")
    urinish2 = 0
    while True:
        num = r.randint(x, y)
        javob = input(f"\nSiz {num} sonini o'ylagansiz: to'g'ri bo'lsa (T), katta bo'lsa (+), kichik bo'lsa (-)\n>>> ")
        urinish2 += 1
        if javob:
            if javob.lower() == 't':
                print(f"\nO'ylagan soningizni {urinish2}ta urinish bilan topdim!")
                return urinish2
                break                
            elif javob == '+':
                x = num + 1
            elif javob == '-':
                y = num - 1
            else:
                print("Noto'gri qiymat kiritdingiz! Iltimos qaytadan urinib ko'ring.")
        else:
            print("Siz bo'sh qiymat berdingiz.\n\n")
            
# test = son_top_my(1, 10) 

def result(pc, user):
    if pc == user:
        return f"Sizda {user} ball, menda ham {pc} ball, demak durrang."
    elif pc > user:
        return f"Sizda {user} ball, menda {pc} ball, Men sizni yutyapman."
    elif pc < user:
        return f"Sizda {user} ball, menda {pc} ball, Siz yutyapsiz.."
