# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

# for i in range(1,6):
#     print(i, '00000')

# **********************************************************************************************
# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

# sum_5=0
# for i in range(10):
#     zifra=input('Введите цифру')
#     zifra=int(zifra)
#     if zifra ==5: sum_5+=1
# print('Количество введеных цифр 5(пять) равно', sum_5)

# **********************************************************************************************
# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

# sum=0
# for i in range(1,101,1):
#     sum+=i
# print('Сумма ряда чисел от 1 до 100 равен ', sum)

# **********************************************************************************************
# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

# proizved=1
# for i in range(1,11,1):
#     proizved*=i
# print('Произведение ряда чисел от 1 до 10 равен ', proizved)

# **********************************************************************************************
# Задача 5
# Вывести цифры числа на каждой строчке.

# number = input('Введите целое число')
# number=int(number)
# num_back=''
# num_oststok=0
#
# # Подготовка числа для вывода
# while number>0:
#     num_oststok=number%10
#     ost=str(num_oststok)
#     num_back+=ost
#     number=number//10
#
# number=int(num_back)
#
# # Вывод цифр чисела на каждой строке
# while number>0:
#     print(number%10)
#     number=number//10

# **********************************************************************************************
# Задача 6
# Найти сумму цифр числа.

# number = input('Введите целое число')
# number=int(number)
# sum_chisla=0
#
# while number>0:
#     sum_chisla+=number%10
#     number=number//10
# print('Сумма цифр числа равна ', sum_chisla)

# **********************************************************************************************
# Задача 7
# Найти произведение цифр числа.

# number = input('Введите целое число')
# number=int(number)
# proizv_chisla=1
#
# while number>0:
#     proizv_chisla*=number%10
#     number=number//10
# print('Произведение цифр числа равна ', proizv_chisla)

# **********************************************************************************************
# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?

number = input('Введите целое число')
number=int(number)

while number>0:
    if number%10 == 5:
        print('В данном числе есть цифра 5(пять)')
        break
else: print('В данном числе нет цифры 5(пять)')