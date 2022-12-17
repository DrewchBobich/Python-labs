#Задание №1
def chetni(i):   # i - список
    b = []
    for h in range(0, len(i)):
        if h % 2 == 0:
            b.append(i[h])
        else:
            continue
    return b

#Задание №2
def bolshe(i):    # i - список
    b = []
    for h in range(len(i)-1):
        if i[h + 1] > i[h]:
            b.append(i[h + 1])
        else:
            continue
    return b

#Задание №3
def prikol(i):    # i - список
    bolsh = max(i)
    mensh = min(i)
    b = i.index(min(i))
    a = i.index(max(i))
    i[b] = bolsh
    i[a] = mensh
    return i  

#Задание №4
def chtoto(i, b):    # i - словарь, b - ключ
  print(i[b])

