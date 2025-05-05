# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  17_animate_demand.py - анимация, управление по требованию

"""
from graph import *

def update():
  moveObjectBy(obj, dx , dy )

def keyPressed(event):
  global dx, dy
  if event.keycode == VK_LEFT:
    dx = -5; dy = 0
  elif event.keycode == VK_RIGHT:
    dx = 5; dy = 0
  elif event.keycode == VK_UP:
    dx = 0; dy = -5
  elif event.keycode == VK_DOWN:
    dx = 0; dy = 5
  elif event.keycode == VK_ESCAPE:
    close()  # закрыть окно

brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
dx = dy = 0
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)

onTimer( update, 50 )
onKey( keyPressed )

run()

