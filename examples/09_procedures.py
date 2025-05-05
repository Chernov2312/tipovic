# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  09_procedures.py - процедуры

"""
from graph import *

def treug(x, y, c):
  brushColor(c)
  polygon([(x,y), (x,y-60),
           (x+100,y), (x,y)] )

penColor ( "black" )
treug ( 100, 100, "blue" )
treug ( 200, 100, "green" )
treug ( 200, 160, "red" )

run()

