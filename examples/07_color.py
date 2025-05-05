# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  07_color.py - использование цвета

"""
from graph import *

penColor( "blue" )
penSize( 3 )
brushColor( "red" )
rectangle( 20, 20, 100, 40 )
circle( 60, 80, 30 )

run()
