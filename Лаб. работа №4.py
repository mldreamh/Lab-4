import rubles_txt
employees_num = int(input('Введите количество сотрудников от 1 до 1000 '))
summma = 0
distance_list = []
price_list = []
for i in range(employees_num):
    distance = int(input('Введите расстояние до дома {0}-го сотрудника '.format(i+1)))
    distance_list.append(distance)
for i in range(employees_num):
    price = int(input('Введите тариф {0}-го такси '.format(i+1)))
    price_list.append(price)
c_distance_list = distance_list[:]
c_price_list = price_list[:]
index_list_d = []
index_list_p = []
max_distance = 0
for i in range(employees_num):                              
    index = c_distance_list.index(max(c_distance_list))
    index_list_d.append(index)
    c_distance_list[index] = 0
for i in range(employees_num):
    index = c_price_list.index(min(c_price_list))
    index_list_p.append(index)
    c_price_list[index] = 10**10
print('Такси для сотрудников по порядку:')
for i in range(employees_num):
    taxi_num = index_list_p[index_list_d.index(i)]
    print(taxi_num+1)
for i in range(employees_num):
    summma += distance_list[index_list_d[i]]*price_list[index_list_p[i]]
print(summma)
print('Сумма к оплате:')
rubles_txt.out(summma)