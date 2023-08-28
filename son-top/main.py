from functions import son_top_my, son_top_pc, result

def main(x, y):
    pc_ball, user_ball = 0, 0
    while True:
        pc = son_top_pc(x, y)
        user = son_top_my(x, y)
        if pc == user:
            pc_ball += 1
            user_ball += 1
        elif pc > user:
            pc_ball += 1
        elif pc < user:
            user_ball += 1
        print(result(pc_ball, user_ball))
        stop = input("O'yinni davom ettiramizmi? ha(y) yoki yo'q(n): ")
        if stop.lower() == 'n':
            break
    
def run():
    """
    Bu o'yinda birinchi men `x`dan `y`gacha bo'lgan son o'ylayman siz topasiz, men topishga harakat qilaman.
    Keyin esa siz `x`dan `y`gacha bo'lgan son o'ylaysiz men topaman.
    """
    while True:
        x = input("X = ? ")
        y = input("Y = ? ")
        if x.isnumeric() and y.isnumeric():
            x = int(x)
            y = int(y)
            main(x, y)
            break
        else:
            print("Faqat butun son kiriting.")
