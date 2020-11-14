# -*- coding: utf-8 -*-
# Функция, которая конвертирует число (без знака) из одной системы исчисления в любую другую.

from sys import argv

usage = str('\nВведите аргументы в следующем виде:\n'
            'python task1.py numb from_base to_base\n'
            'где\n'
            'task1.py - путь к файлу программы\n'
            'numb- число для перевода\n'
            'from_base - входная система счисления(число от 2 до 36)\n'
            'to_base - выходныя система счисления(число от 2 до 36, котики)')


def convert(nb, from_base, to_base):
    nb = str(nb)
    from_base = int(from_base)
    n = int(nb, from_base)
    if to_base != 'котики':
        to_base = int(to_base)
        if to_base > 36:
            print(usage)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return convert(n // to_base, from_base=10, to_base=to_base) + alphabet[n % to_base]
    else:
        return convert_cat(n)


def convert_cat(n):
    if n == 0:
        return 'нет котиков'
    elif n < 4:
        return 'мало котиков'
    elif n < 9:
        return 'несколько котиков'
    elif n < 19:
        return 'группа котиков'
    elif n < 50:
        return 'толпа котиков'
    elif n < 99:
        return 'орда котиков'
    elif n < 200:
        return 'сотни котиков'
    elif n < 500:
        return 'туча котиков'
    elif n < 1000:
        return 'тьма котиков'
    else:
        return 'легион котиков'


try:
    program, input_numb, input_base, result_base = argv
    print('Результат: ', convert(input_numb, input_base, result_base))
except:
    print(usage)
