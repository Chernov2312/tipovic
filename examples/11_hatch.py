# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  11_hatch.py - штриховка

"""
from graph import *

x1 = 100; y1 = 100
x2 = 300; y2 = 200
rectangle(x1,y1,x2,y2)

N = 10
h = (x2-x1)/(N+1)
x = x1 + h
for i in range(N):
  line(x, y1, x, y2)
  x += h

run()

