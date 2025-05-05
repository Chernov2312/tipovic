# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  01_turtle_square.py - Черепаха рисует квадрат

"""
from turtle import *

for i in range(4):
  fd(60)
  rt(90)

exitonclick()