my_dict = {'Dima' : 1999, 'Vanya' : 2001, 'Masha' : 2000}
print(my_dict)
print(my_dict.get('Dima' , 'Такого ключа нет'))
print(my_dict.get('Nikita' , 'Такого ключа нет'))
my_dict.update({'Nikita' : 1998, 'Anton' : 2000})
a = my_dict.pop('Dima')
print(a, 'Удаленный ключ')
print(my_dict)
my_set = {1, 1, 2, 2, 3, 3, 4, 5, 'Dasha', 'Dasha', True, 'Nikita'}
print(my_set)
my_set.add('Dima')
my_set.add(7)
my_set.remove(1)
print(my_set)
