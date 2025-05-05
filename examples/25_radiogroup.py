# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  25_radiogroup.py - группа радиокнопок TRadioGroup

"""
from simpletk import *

def mouseMove(event):
  print('(', event.x, ',', event.y, ')')

def click(event):
  print('* (', event.x, ',', event.y, ')')

def dblClick(event):
  print('** (', event.x, ',', event.y, ')')

def enter(event):
  print('enter')

def leave(event):
  print('leave')

def keyPressed(event):
  print(event.keycode, ',', event.keysym, ',', event.char)

app = TApplication("Использование радиогруппы TRadioGroup")
app.position = (200, 200)
app.size = (300, 300)

rg = TRadioGroup(app,
          values = ["Python", 'C++', "Java", 'Haskell', 'Kotlin'],
          width = 200, height = 200, padx = 10, pady = 10)
rg.position = (10, 10)
rg.background = "#FEFEE2"
rg.color = "black"
rg.font = ('Consolas', 12)
rg.selected = 2
#rg.align="client"

def change(sender):
  print('Selected now:', sender.selected,
                         sender.item(sender.selected))

rg.onMouseMove = mouseMove
rg.onClick = click
rg.onDblClick = dblClick
rg.onEnter = enter
rg.onLeave = leave
rg.onKey = keyPressed
rg.onChange = change

app.run()

