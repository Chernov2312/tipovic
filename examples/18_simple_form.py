# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  18_simple_form.py - простая форма

"""
from simpletk import *
from tkinter.messagebox import askokcancel

def askOnExit():
  if askokcancel ( "Подтверждение", "Хотите выйти из программы?" ):
    app.destroy()

def mouseMove(event):
  print('(', event.x, ',', event.y, ')')

def click(event):
  print('* (', event.x, ',', event.y, ')')

def dblClick(event):
  print('** (', event.x, ',', event.y, ')')

def keyPressed(event):
  print('key', event.keycode, ',', event.keysym, ',', event.char)

def resize(event):
  print('resize (', event.x, ',', event.y, ',', event.width, ',', event.height, ')')

def enter(event):
  print('enter')

def leave(event):
  print('leave')

app = TApplication("Первая форма")

app.position = (100, 300)
app.size = (500, 200)
app.minsize = (100, 200)
app.maxsize = (900, 700)
app.resizable = (True, False)
app.background = "white"

app.onCloseQuery = askOnExit
app.onMouseMove = mouseMove
app.onClick = click
app.onDblClick = dblClick
app.onResize = resize
app.onKey = keyPressed
app.onEnter = enter
app.onLeave = leave

app.run()

