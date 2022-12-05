#Задани №1
def chetni(i):
    b = []
    for h in range(0, len(i)):
        if h % 2 == 0:
            b.append(i[h])
        else:
            continue
    return b

