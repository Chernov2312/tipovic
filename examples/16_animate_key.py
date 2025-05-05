# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  16_animate_key.py - анимация, управление с клавиатуры

"""
from graph import *

def keyPressed(event):
  if event.keycode == VK_LEFT:
    moveObjectBy(obj, -5, 0)
  elif event.keycode == VK_RIGHT:
    moveObjectBy(obj, 5, 0)
  elif event.keycode == VK_UP:
    moveObjectBy(obj, 0, -5)
  elif event.keycode == VK_DOWN:
    moveObjectBy(obj, 0, 5)
  elif event.keycode == VK_ESCAPE:
    close()  # закрыть окно

brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)

onKey( keyPressed )

run()

