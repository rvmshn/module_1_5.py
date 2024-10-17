immutable_var = 1, 'two', 3, True, [5.5, 'seven']
print(immutable_var)
# immutable_var[0] = 2
# Кортеж неизменяем, т.к содержит ссылку на список, а не сам список
# Однако, список внутри кортежа можно изменить
mutable_list = ['morning', 'afternoon', 'evening', 'night', 1984, True]
mutable_list[0]='conquest'
mutable_list[1]='war'
mutable_list[2]='famine'
mutable_list[3]='death'
mutable_list[4]=2024
mutable_list[5]= False
mutable_list.append('banana')
print(mutable_list)