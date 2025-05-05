# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  10_loops.py - циклы

"""
from graph import *

def row ( y ):
  for x in range(40, 290, 60):
    circle(x, y, 20)

for y in range(40, 170, 60):
  row ( y )

run()

