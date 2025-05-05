# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  15_animate.py - анимация

"""
from graph import *

def update():
  moveObjectBy( obj, 5, 0 )
  if xCoord(obj) >= 380: # если вышел
     close()

def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()  # закрыть окно

def EscPressed(event):
  close()  # закрыть окно

brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)

onTimer( update, 50 )

# onKey( keyPressed )
onKey( "Escape", EscPressed )

run()

