#                          Задайте список из вещественных чисел. Напишите программу, 
#          которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#   Пример:

#   - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 10.01]
maximum = 0
minimum = 10  
for i in my_list:
    count = round(i % 1, 2)  
    if count > maximum:
        maximum = count
    else:
        minimum = count
print(f"Максимум = {maximum}\nМинимум = {minimum}\nРазница = {maximum - minimum}")
