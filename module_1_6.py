my_dict = {'Ольга' : 1985, 'Людмила' : 1960, 'Владимир' : 1955}
print(my_dict)
print(my_dict['Владимир'])
print(my_dict.get('Владимир'))
print(my_dict.get('Елена'))
print(my_dict.get('Елена', "Такого имени нет"))
my_dict['Анна'] = 2004
my_dict['Егор'] = 2006
print(my_dict)
my_dict.update({'Ирина' : 1971, 'Татьяна' : 1970})
print(my_dict)
tat_brthd = my_dict.pop('Татьяна')
print('Татьяна :', tat_brthd)
print(my_dict)
print('')
my_set = {'Ольга', 234, True, (2,3,4)}
print(my_set)
my_set.add('Елена')
my_set.add(7)
print(my_set)
my_set.update({'Анастасия', False})
print(my_set)
my_set.remove(7)
print(my_set)