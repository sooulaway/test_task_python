# -*- coding: utf-8 -*-
# Функция, которая конвертирует число (без знака) из одной системы исчисления в любую другую.

def convert(nb, from_base, to_base=10):
    nb = str(nb)
    from_base = int(from_base)
    n = int(nb, from_base)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert(n // to_base, from_base=10, to_base=to_base) + alphabet[n % to_base]


def restart():
    allow_answer = ['да', 'нет']
    answer = input('Хотите попробовать ещё раз?\nОтвечайте только да или нет: ')
    while answer not in allow_answer:
        answer = input('Отвечайте только да или нет:')
    if answer == 'да':
        main()


def main():
    input_numb = input('Введите число:  ')
    input_base = input('Введите систему счисления из которой необходимо перевести:  ')
    result_base = int(input('Введите систему счисления в какую необходимо перевести\n '
                            'это должно быть число от 2 до 36:  '))
    try:
        print('Вот ваше число в десятичной системе: ', convert(input_numb, input_base, result_base))
        restart()
    except:
        print('usage')
        restart()


main()
