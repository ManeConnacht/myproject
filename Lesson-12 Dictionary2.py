enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
    'image': ['pic1.jpg', 'pic2.jpg', 'pic3.jpg']   # к каждой из pic1-3 можно обращаться или менять отдельно
}

all_enemies = [] # Создаем массив


# all_enemies.append(enemy) # ручное зополнение массива


for x in range (0, 10):       #зополнение через for
    #all_enemies.append(enemy) #Создаются клоны а не копии, меняещь одну меняются все.
    all_enemies.append(enemy.copy())  # Создаются копииа не клоны, меняещь одну меняются только он.


all_enemies[2]['health'] = 30 # Мы изменили значение в массиве у одного а изменилось у всех :) нужна .copy при создании
all_enemies[9]['name'] = 'SuperDildo'
all_enemies[9]['loc_y'] += 10 #Сокращенная запись '+='означает x = x + 1
for ene in all_enemies:
    print(ene)


