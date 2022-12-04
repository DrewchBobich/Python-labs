#Задание №1
massive = []
for i in range(10):
  massive.append(int(input("Введите число: ")))
print(sum(massive))

#Задание №2
massive = []
for i in range(10):
  massive.append(int(input("Введите число: ")))
print(massive.count(0))

#Задание №3
b = int(input("Введите натуральное число: "))
for i in range(1,b+1):
    g = [str(b + 1) for b in range(i)]
    s = ''
    print(s.join(g))

#Задание №4
b = int(input("Введите натуральное число: "))
for i in range(1,b+1):
    g = [" " for b in range(i, b+1)] + [str(h+1) for h in range(0,i-1)] + [str(i)] + [str((i-1)-k) for k in range(0, i-1)]
    s = ''
    print(s.join(g))

