# -*- coding: utf-8 -*-
# Анализ лога
from sys import argv
from time import strptime
import re
import csv

usage = str('\nВведите аргументы в следующем виде:\n'
            'python task3.py log.log from_time to_time\n'
            'где\n'
            'task3.py - путь к файлу программы\n'
            'log.log - путь к файлу лога\n'
            'from_time - начало периода\n'
            'to_time - конец периода\n'
            'формат даты: 2020-11-14T19:45:12\n')


def log_parser(_file, _from_time, _to_time):
    _from_time = strptime(_from_time, "%Y-%m-%dT%H:%M:%S")
    _to_time = strptime(_to_time, "%Y-%m-%dT%H:%M:%S")
    count = 0
    count_try_top_up = 0
    count_try_scoop = 0
    count_fail = 0
    sum_water_top_up = 0
    sum_water_scoop = 0
    sum_water_not_top_up = 0
    sum_water_not_scoop = 0
    delta_volume_from_period = 0
    with open(_file, 'r', encoding='cp1251') as log:
        for i, line in enumerate(log):
            if i == 2:
                water_volume = int(line[:2])
            elif i > 2:
                line_time = strptime(line[:23], "%Y-%m-%dT%H:%M:%S.%f")
                if line_time < _from_time:
                    delta_volume = re.findall(r'\d+', line[47:])
                    delta_volume = int(delta_volume[0])
                    if 'top up' in line:
                        if 'успех' in line:
                            water_volume += delta_volume
                    elif 'scoop' in line:
                        if 'успех' in line:
                            water_volume -= delta_volume
                elif _from_time <= line_time <= _to_time:
                    delta_volume = re.findall(r'\d+', line[47:])
                    delta_volume = int(delta_volume[0])
                    count += 1
                    if 'top up' in line:
                        count_try_top_up += 1
                        if 'успех' in line:
                            sum_water_top_up += delta_volume
                            delta_volume_from_period += delta_volume
                        elif 'фейл' in line:
                            sum_water_not_top_up += delta_volume
                    if 'фейл' in line:
                        count_fail += 1
                    if 'scoop' in line:
                        count_try_scoop += 1
                        if 'успех' in line:
                            sum_water_scoop += delta_volume
                            delta_volume_from_period -= delta_volume
                        elif 'фейл' in line:
                            sum_water_not_scoop += delta_volume

    if count == 0:
        print('В указанный период операций с бочкой не было')
    else:
        percent_fail = round((count_fail / count) * 100, 2)
        water_volume_end = water_volume + delta_volume_from_period
        result = {}
        result.update({'count_try_top_up': count_try_top_up,  # Количество попыток налить воду в бочку
                       'percent_fail': percent_fail,  # Процент ошибок
                       'sum_water_top_up': sum_water_top_up,  # Количество воды налитой в бочку
                       'sum_water_not_top_up': sum_water_not_top_up,  # Количество воды которую пытались налить в бочку
                       'count_try_scoop': count_try_scoop,  # Количество попыток набрать воды
                       'sum_water_scoop': sum_water_scoop,  # Количество воды набранной из бочки
                       'sum_water_not_scoop': sum_water_not_scoop,  # Обьем воды которую пытались набрать из бочки
                       'water_volume_start': water_volume,  # Объем воды в бочке на начало периода
                       'water_volume_end': water_volume_end})  # Объем воды в бочке на конец периода
        with open("result.csv", mode="w", encoding='utf-8') as result_file:
            header = result.keys()
            file_writer = csv.DictWriter(result_file, delimiter=";", lineterminator="\r", fieldnames=header)
            file_writer.writeheader()
            file_writer.writerow(result)


try:
    program, file, from_time, to_time = argv
    log_parser(file, from_time, to_time)
except:
    print(usage)
