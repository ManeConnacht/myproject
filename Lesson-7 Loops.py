for i in range(100, 10,-2):
    print('Print num X= '+str(i))
    if i == 50:
        break

x=0
while True:   #вечный цикл выход только по условию
    print(x)
    x += 1
    if x == 100:
        break