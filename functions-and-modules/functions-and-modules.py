""" З А Д А Н И Е 1.
Напишите программу компьютерной игры "Угадай число",
в которой компьютер генерирует случайное целое число от 1 до 15,
а пользователь должен его угадать.
После каждой неудачной попытки пользователя, программа должна
сообщать ему о том, больше это число, или меньше загаданного,
а в случае угадывания - поздравлять с выигрышем.
"""
import os
import random


# Решение
def guess_the_number() -> None:
    number: int = random.randint(1, 15)
    user_number: int = -1
    while user_number != number:
        user_number = int(input('Введите число: '))
        if user_number > number:
            print('Меньше')
        elif user_number < number:
            print('Больше')
        else:
            print('Поздравляю!')


""" З А Д А Н И Е 2.
Создайте в директории /content папку my_folder и запишите в ней 10 файлов.
"""


# Решение
def create_dir_and_files() -> None:
    os.chdir('../content')
    os.mkdir('my_folder')
    print('Папка my_folder создана в текущей директории.')
    os.chdir('my_folder')
    for i in range(10):
        f = open(f'file_{i + 1}.txt', 'w')
        print(f'Файл file_{i + 1}.txt создан и записан.')
    os.chdir('..')
    print('Вернулись в исходную директорию.')


""" З А Д А Н И Е 3.
Создайте код, который применяет функцию map к списку слов
и использует анонимную функцию lambda для инвертирования 
порядка букв в каждом слове.
"""


# Решение
def invert_words_in_list() -> None:
    lst: list[str] = ['дом', 'квартира', 'поместье']
    inverted_lst = list(map(lambda x: x[::-1], lst))
    print(inverted_lst)


""" З А Д А Н И Е 4.
Напишите программу, которая рассчитывает расход бензина и стоимость
поездки на автомобиле в зависимости от пройденного расстояния и типа дороги. 
Программа должна принимать на вход два аргумента: 
    distance - расстояние в километрах
    city - флаг, указывающий на тип дороги (0 - трасса, 1 - город). 
Программа должна использовать следующие данные:
Расход бензина на трассе: 5.5 литров на 100 км 
Расход бензина в городе: 8 литров на 100 км 
Цена бензина: 53 рубля за литр 
Программа должна выводить на экран количество потраченного 
бензина в литрах и стоимость поездки в рублях, округляя значения 
до одного и двух знаков после запятой соответственно. Программа должна 
использовать функцию car(), которая реализует логику расчетов и вывода результатов.
"""


# Решение
def car(distance: int, city: int) -> None:
    if city == 0:
        print(round((distance / 100) * 5.5, 1), round((distance / 100) * 5.5 * 53, 2))
    else:
        print(round((distance / 100) * 8, 1), round((distance / 100) * 8 * 53, 2))


""" З А Д А Н И Е 5.
мне лень.
"""
