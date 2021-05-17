#Урок №1
print ('Задача №1. Вывод информации о промежутке времени выраженном в секундах и его преобразование в годах, днях, часах, минутах')
print ()

duration = int(input ('Введите промежуток времени в секундах: '))
minute = 60; hour = minute**2; day = hour*24; year = day*365
minute_rez = duration // minute
hour_rez = duration // hour
day_rez = duration // day
year_rez = duration // year

print (f'промежуток времени в годах {year_rez} в днях {day_rez} в часах {hour_rez} в минутах {minute_rez}')
print ()

print ('Задача №2. Создать список, состоящий из кубов нечетных чисел от 0 до 1000 и произвести вычисления согласно условиям')
print ()

my_list  = []
for i in range (0,1001):
    if not i % 2 == 0:
        my_list.append (i ** 3)
print (*my_list, sep = ',')

sum_my_list = 0
for element in range (len(my_list)):
    elem_list = 0
    a = str(my_list[element])
    for i in a:
        elem_list +=  int(i)
    if elem_list % 7 == 0:
        sum_my_list += my_list[element]
print (f'сумма цифр которых делится нацело на 7: {sum_my_list}')

sum_my_list1 = 0
for element in range (len(my_list)):
    elem_list = 0
    a = str(my_list[element] + 17)
    for i in a:
        elem_list +=  int(i)
    if elem_list % 7 == 0:
        sum_my_list1 += my_list[element]
print (f'сумма цифр которых делится нацело на 7 c добавением числа 17: {sum_my_list1}')
print ()

print ('Задача №3. Реализовать склонение слова «процент» для чисел до 20')
print ()

a = int(input('введите значение от 0 до 20: '))
if a > 20:
    print ('вы ввели число больше 20 (двадцати)')
elif a == 1:
    print (a, 'процент')
elif a==0 or a>=5:
    print (a, 'процентов')
else:
    print (a, 'процента')
