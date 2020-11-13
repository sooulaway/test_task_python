# -*- coding: utf-8 -*-
# Ищем точки столкновения сферы и прямой линии
# Координаты считываются из файла coordinate.txt

# coord = '{sphere: {center: [0, 0, 0], radius: 10.67}, line: {[1, 0.5, 15], [43, -14.6, 0.04]}}'

import ast
import numpy as np
import matplotlib.pyplot as plt

with open('coordinate.txt', 'r', encoding='utf-8') as coordinate:
    coord = coordinate.readline()

coord = coord.replace('[', '(')
coord = coord.replace(']', ')')
coord = coord.replace('sphere', "'sphere'")
coord = coord.replace('center', "'center'")
coord = coord.replace('radius', "'radius'")
coord = coord.replace('line', "'line'")
coord = ast.literal_eval(coord)

c_x, c_y, c_z = coord['sphere']['center']
radius = coord['sphere']['radius']
dot1_x, dot1_y, dot1_z = list(coord['line'])[0]
dot2_x, dot2_y, dot2_z = list(coord['line'])[1]

# Параметрическое уравнение прямых
# X = dot1_x + t * (dot2_x-dot1_x) и аналогично для Y, Z
# dx = dot2_x-dot1_x
# Уравнение сферы:
# (X-c_x)**2 + (Y-c_y)**2 + (Z-c_z)**2 = radius**2
# Из них выражаем:
# (dx**2+dy**2+dz**2)*t**2 + 2*(dx*(dot1_x-c_x)+dy*(dot1_y-c_y)+dz*(dot1_z-c_z))*t +
# + ((dot1_x-c_x)**2 + (dot1_y-c_y)**2 + (dot1_z-c_z)**2 - radius**2) = 0
# Следовательно:

dx = dot2_x - dot1_x
dy = dot2_y - dot1_y
dz = dot2_z - dot1_z
a = dx ** 2 + dy ** 2 + dz ** 2
b = 2 * (dx * (dot1_x - c_x) + dy * (dot1_y - c_y) + dz * (dot1_z - c_z))
c = (dot1_x - c_x) ** 2 + (dot1_y - c_y) ** 2 + (dot1_z - c_z) ** 2 - radius ** 2
disc = (b ** 2) - (4 * a * c)
disc = round(disc, 2)
collision_1 = []
collision_2 = []
if disc < 0:
    print('Коллизий не найдено')
elif disc == 0:
    t1 = -b / (2 * a)
    collision_1 = (round(dot1_x + t1 * dx, 2), round(dot1_y + t1 * dy, 2), round(dot1_z + t1 * dz, 2))
    print(collision_1)
else:
    t1 = (-b + disc ** 0.5) / (2 * a)
    t2 = (-b - disc ** 0.5) / (2 * a)
    collision_1 = [round(dot1_x + t1 * dx, 2), round(dot1_y + t1 * dy, 2), round(dot1_z + t1 * dz, 2)]
    collision_2 = [round(dot1_x + t2 * dx, 2), round(dot1_y + t2 * dy, 2), round(dot1_z + t2 * dz, 2)]
    print(collision_1)
    print(collision_2)
scale = int(2* radius)
ax = plt.axes(projection="3d")
x_list = np.linspace(-radius, radius, scale)
y_list = np.linspace(-radius, radius, scale)
r = np.linspace(radius, radius, scale)
X, Y = np.meshgrid(x_list, y_list)
Z = (r ** 2 - X ** 2 - Y ** 2) ** 0.5
# TODO Выдает предупреждение из-за отрицательных элементов массива, не успел разобраться как исправить

ax.plot_wireframe(c_x + X, c_y + Y, c_z + Z, color="r")
ax.plot_wireframe(c_x + X, c_y + Y, c_z - Z, color="r")
if disc == 0:
    ax.scatter(collision_1[0], collision_1[1], collision_1[2], c='g', marker='o', s=40)
elif disc > 0:
    ax.scatter(collision_1[0], collision_1[1], collision_1[2], c='g', marker='o', s=40)
    ax.scatter(collision_2[0], collision_2[1], collision_2[2], c='g', marker='o', s=40)
line_x = np.linspace(-scale, scale, 2)
line_y = ((line_x-dot1_x)*(dot2_y-dot1_y)/(dot2_x-dot1_x))+dot1_y
line_z = ((line_x-dot1_x)*(dot2_z-dot1_z)/(dot2_x-dot1_x))+dot1_z
ax.plot(line_x, line_y, line_z)
plt.title('Рендер')
ax.set_xlim3d(-scale, scale)
ax.set_ylim3d(-scale, scale)
ax.set_zlim3d(-scale, scale)
plt.show()
