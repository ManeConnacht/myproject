cities = ['New York','Moscow', 'new Deli', 'Saratov', 'Kurgan', 'Moscow']
for i in range(len(cities)):
    print(cities[i])

print(cities[-3].title()) #выведет new Deli c большой буквы
print(cities[0].lower()) # выведет  new york строчными буквами

cities[-2] = 'Tulastan'
cities.append('Paragwai')    #добавить Paragwai  в конец
cities.insert(2, "Kali")    # добавит Kali на место 2
del cities[-1]              #сотрет Pargwai
cities.remove('Moscow')   #уберет из списка Moscowб но только первую
print(cities)

del_city = cities.pop() # Стирает и дает последний город Mocsow или выбранный город если передать значение в функцию
print("Deleted city: "+ del_city)
cities.sort() #сортировка по алфавиту
cities.sort(reverse=True) #сортировка в обратном порядке
#cities.reverse() делает тоже самое что и строка 18
print(cities)

