# Программа генерирует лог
import os
from random import randint
from datetime import datetime, timedelta


class Barrel:
    def __init__(self, volume, water, time):
        self.volume = volume
        self.water = water
        self.time = time

    def __str__(self):
        return 'В бочке осталось {} литра'.format(self.water)


class Man:
    def __init__(self, _barrel, _name):
        self.barrel = _barrel
        self.name = _name

    def top_up(self):
        scoop = randint(1, 50)
        time = self.add_time()
        act = 'top up'
        if self.barrel.water + scoop > 200:
            result = 'фейл'
            self.print_log(time, act, scoop, result)
        else:
            self.barrel.water += scoop
            result = 'успех'
            self.print_log(time, act, scoop, result)

    def scoop(self):
        scoop = randint(1, 50)
        time = self.add_time()
        act = 'scoop'
        if self.barrel.water - scoop < 0:
            result = 'фейл'
            self.print_log(time, act, scoop, result)
        else:
            self.barrel.water -= scoop
            result = 'успех'
            self.print_log(time, act, scoop, result)

    def add_time(self):
        period = randint(10 ** 4, 10 ** 6)
        self.barrel.time += timedelta(microseconds=period)
        time = self.barrel.time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
        return time

    def print_log(self, time, act, scoop, result):
        with open('log.log', mode='a', encoding='cp1251') as log:
            log.write('{}Z - [{}] - wanna {} {}l ({})\n'.format(time, self.name, act, scoop, result))


now = datetime.now()
real_barrel = Barrel(200, 32, now)
people = [Man(real_barrel, 'username1'), Man(real_barrel, 'username2')]
with open('log.log', mode='w', encoding='cp1251') as file:
    file.write(
        'META DATA:\n{} (объем бочки)\n{} (текущий объем воды в бочке)\n'.format(real_barrel.volume, real_barrel.water)
    )
size = os.path.getsize('log.log')
while size < 1024 ** 2:
    size = os.path.getsize('log.log')
    for man in people:
        dice = randint(1, 2)
        if dice == 1:
            man.scoop()
        else:
            man.top_up()
