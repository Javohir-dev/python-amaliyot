
def read_file(file_name):
    with open(file_name) as file:
        PI = file.read()
    
    x = PI.replace('\n', '')
    PI = float(x)
    
    return PI


def readline(filename):
    with open(filename) as file:
        for line in file:
            print(line)
            
    with open(filename) as file:
        talabalar = file.readlines()
        talabalar = [ talaba.rstrip() for talaba in talabalar ]
    
        return talabalar

def create_file(filename, firstname, lastname, age):
    with open(filename, 'w') as fayl:
        fayl.write(firstname + ' ')
        fayl.write(lastname + '\n')
        fayl.write(str(age) + '\n')

def add_data(filename, firstname, lastname, age):
    with open(filename, 'a') as fayl:
        fayl.write(firstname + ' ')
        fayl.write(lastname + '\n')
        fayl.write(str(age) + '\n')


import pickle

# talaba1 = {'ism': 'hasan', 'familiya': 'husanov', 'tyil': 2003, 'kurs': 2}
# talaba2 = {'ism': 'alijon', 'familiya': 'valiyev', 'tyil': 2004, 'kurs': 1}

# with open('info','wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)


with open('info','rb') as file:
    talaba2 = pickle.load(file)
    talaba1 = pickle.load(file)