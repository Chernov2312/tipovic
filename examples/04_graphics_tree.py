# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  04_graphics_tree.py - дерево

"""
from graphics import *
from math import pi, sin, cos

def tree( window, x0, y0, угол, длина, уровни ):
  if уровни == 0: return
  x1 = x0 + длина*cos(угол*pi/180)
  y1 = y0 - длина*sin(угол*pi/180)
  line = Line( Point(x0, y0), Point(x1, y1) )
  line.draw( window )
  tree( window, x1, y1, угол-45, длина*0.6, уровни-1 )
  tree( window, x1, y1, угол+45, длина*0.6, уровни-1 )

window = GraphWin("Дерево", 400, 400)
window.setBackground("white")

tree( window, 200, 300, 90, 100, 5 )

window.getMouse()
window.close()