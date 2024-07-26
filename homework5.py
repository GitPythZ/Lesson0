immutable_var = 1, 2, 'apple', True
print(immutable_var)
print(immutable_var[0])
#immutable_var[0][2] = 'pear'
# Операция не работает, т.к. кортеж, в отлияие от списка структура стабильная - неизменяемая
# В самом кортеже могут хранить изменяемые элементы (например, списки), но в нашем слкчае строки и цифры, а они тоже неизменяемые элементы
mutable_list = [1, 2, 'три', 'ч', 'е', 'т', 'ы','р','е', 5, False]
print(mutable_list)
mutable_list[2]=3
print(mutable_list)


