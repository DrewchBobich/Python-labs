#Задание №1
def chetni(i):   # i - список
    b = []
    for h in range(0, len(i)):
        if h % 2 == 0:
            b.append(i[h])
        else:
            continue
    return b

a = [1, 2, 3, 4]
print(chetni(a))    


#Задание №2
def bolshe(i):    # i - список
    b = []
    for h in range(len(i)-1):
        if i[h + 1] > i[h]:
            b.append(i[h + 1])
        else:
            continue
    return b

a = [1, 2, 3, 4]
print(bolshe(a))


#Задание №3
def prikol(i):    # i - список
    bolsh = max(i)
    mensh = min(i)
    b = i.index(min(i))
    a = i.index(max(i))
    i[b] = bolsh
    i[a] = mensh
    return i  

a = [1, 2, 3, 4]
print(prikol(a))


#Задание №4
d = {1: 'bebra', 2: 'bobra', 3: 'dobra', 4: 'dora'}
key = int(input('Введите ключ, чтобы получить значение: '))

def get_value(dictionary):
    value = dictionary.get(key)
    print(value)

get_value(d)
