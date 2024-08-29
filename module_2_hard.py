
vhod_chislo=0
priznak_vhod_chislo = 0
password = []
perebor = 1
ferst_zn_sp = []
ferst_zn_sp_Old = []
second_zn_sp = []
ferst_zn = 0
second_zn = 0
passwordStr = ''

def vvod_chisla():
    global vhod_chislo
    vhod_chislo = int(input('Введите число (от 3 до 20):'))
def proverka_vhod_chislo():
    global priznak_vhod_chislo
    if vhod_chislo >= 3 and vhod_chislo <= 20:
        priznak_vhod_chislo = 1
    else:
        print('Число введено НЕВЕРНО ...')

def create_ferst_zn_sp(x):
    global ferst_zn_sp
    for i in range(1,x):
        ferst_zn_sp.append(i)

def create_password(x):
    global password
    global ferst_zn_sp
    global second_zn_sp
    for i in ferst_zn_sp:
        ferst_zn = i
        rem_in_second_zn_sp(ferst_zn)
        for j in second_zn_sp:
            second_zn = j
            summa = ferst_zn + second_zn
            if x%summa == 0:
                    password.append(ferst_zn)
                    password.append(second_zn)
                    rem_in_second_zn_sp(ferst_zn)

def rem_in_second_zn_sp(x):
    global second_zn_sp
    new = []
    for d in range(0,len(second_zn_sp)):
        if second_zn_sp[d] != x:
            new.append(second_zn_sp[d])
    second_zn_sp = new

def create_passwordStr():
    global passwordStr
    for i in password:
        passwordStr = passwordStr + str(i)

while priznak_vhod_chislo == 0:
    vvod_chisla()
    proverka_vhod_chislo()
create_ferst_zn_sp(vhod_chislo)
second_zn_sp = ferst_zn_sp
create_password(vhod_chislo)
create_passwordStr()
print(str(vhod_chislo)+' - '+str(passwordStr))
