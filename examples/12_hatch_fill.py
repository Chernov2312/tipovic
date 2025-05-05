# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  12_hatch_fill.py - штриховка и цвет

"""
from graph import *

x1 = 100; y1 = 100
x2 = 300; y2 = 200
rectangle(x1,y1,x2,y2)

N = 10
h = (x2-x1)/(N+1)
hc = 255 // N
x = x1
c = 0
for i in range(N):
  brushColor(c, c, c)
  rectangle(x, y1, x+h, y2)
  x += h
  c += hc

run()

