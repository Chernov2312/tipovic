# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  03_graphics_square.py - квадрат

"""
from graphics import *

window = GraphWin("Квадрат", 400, 400)
window.setBackground("white")

line1 = Line( Point(20, 20), Point(60, 20) )
line2 = Line( Point(60, 20), Point(60, 60) )
line3 = Line( Point(60, 60), Point(20, 60) )
line4 = Line( Point(20, 60), Point(20, 20) )

line1.draw( window )
line2.draw( window )
line3.draw( window )
line4.draw( window )

window.getMouse()
window.close()