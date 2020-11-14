# -*- coding: utf-8 -*-
#  Сравнение двух строк
import re
from sys import argv

usage = str('\nВведите аргументы в следующем виде:\n'
            'python task4.py str1 str2\n'
            'где\n'
            'task4.py - путь к файлу программы\n'
            'str1 - первая строка\n'
            'str2 - вторая строка\n')


def clear_str(_str):
    new_str = ''
    for i, sign in enumerate(_str):
        if sign != '*':
            new_str += sign
        else:
            if i > 0:
                if _str[i - 1] != '*':
                    new_str += '.' + sign
            else:
                new_str += '.' + sign
    return new_str


def compare_str(_str1, _str2):
    _str2 = clear_str(_str2)
    result = re.search(_str2, _str1)
    if result is not None:
        result = result.group()
        if result == _str1:
            print('OK')
        else:
            print('KO')
    else:
        print('KO')


try:
    program, str1, str2 = argv
    compare_str(str1, str2)
except:
    print(usage)
