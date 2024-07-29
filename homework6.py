# Работа со словорями
my_dict = {'Mama': 1973, 'Papa' : 1972,
           'Bro': 2006, 'Wife': 1997,
           'Me': 1998}
print(my_dict)
my_dict.setdefault('Ruslan', 1998) # или my_dict['Ruslan'] = 1998
keys = ['Mama', 'Ruslan']
values = list(map(my_dict.get, keys))
print(values)
my_dict.update({'Vlad' : 1998,
                'Grandmaa' : 1943})
print(my_dict)
del my_dict['Me']
print(my_dict)
popped_dict = my_dict.pop('Vlad')
print(popped_dict) #Вывел значение ключа

# Работа с множествами
my_set = {1,2,3,4,0, 'set', True, False, (5,6,7,8,9)}
print(my_set)
my_set.update(['True','and', 'False'])
print(my_set)
my_set.remove('and')
print(my_set)






