# Создание списка
my_list = []

# Добавление элементов в список
my_list.append(1)
my_list.insert(0, 0)
my_list.extend([2, 3, 4, 5])

# Удаление элементов из списка
my_list.pop(0)
my_list.pop()
my_list.clear()

# Изменение элементов списка
my_list[0] = "Goodbye"
my_list = [10, 11, 12, 13, 14]

# Доступ к элементам списка
print(my_list[0])
print(my_list[-1])
print(my_list[1:3])

# Цикл for
for item in my_list:
    print(item)
for item in my_list[1:3]:
    print(item)

# Сортировка списка
my_list.sort()
my_list.sort(reverse=True)

# Копирование списка
new_list = my_list.copy()
new_list = my_list[:]

# Объединение списков
new_list = my_list + [15, 16, 17]
new_list = my_list[:] + [15, 16, 17]

# Методы списков
print(my_list.empty())
print(len(my_list))
print(my_list.index("Goodbye"))
print(my_list.count("Goodbye"))
my_list.remove("Goodbye")
print(my_list.unique())
