


enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
}

print('Loc X: ' + str(enemy['loc_x'])) #Видим что опять надо преобразоваывыть в строку
print('Loc Y: ' + str(enemy['loc_y']))
print('Name Enemy: ' + str(enemy['name']))


enemy['Level'] = 1 #добавляем новый item через ввод [ключа] и значения.
print(enemy)

del enemy['color'] #тут все логично удаляем
print(enemy)


enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 80
if enemy['health'] < 50:                #играемся с ifelse
    enemy['color'] = 'yellow'
elif enemy['health'] < 20:
    enemy['color'] = 'red'
else:
    enemy['color'] = 'green'

print(enemy)

print(enemy.keys()) #вывести только ключи
print(enemy.values()) #тут только  значения

