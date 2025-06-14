# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  13_func_curve.py - график функции

"""
from graph import *

x0 = 150 # начало координат
y0 = 250
k = 50   # масштаб
xmin = -2; xmax = 2 # пределы по x
line(0, y0, x0+150, y0)
line(x0, 0, x0, y0+20)

x = xmin  # начальное значение x
h = 0.02  # шаг изменения x
penColor("red")
while x <= xmax:
  y = x*x  # функция
  xe = x0 + k*x
  ye = y0 - k*y
  point(xe, ye) # точка на экране
  x += h   # к следующей точке

run()

