immutable_var=(1,2,3,'svetka')
print(tuple(immutable_var))
#immutable_var[0]=200 Кортеж не поддерживает обращение по элементам.

mutable_list=[100,200,300,'svetka']
print(list(mutable_list))
mutable_list[2]='vovka'
print(mutable_list)