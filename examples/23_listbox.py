# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  23_listbox.py - список TListBox

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

app = TApplication("Использование списка TListBox")
app.position = (200, 200)
app.size = (300, 300)

lb = TListBox(app,
  values=["Item 0", 'Item 1', "Item 2", 'Item 3', 'Item 4'],
  selectmode='multiple', width = 15)
lb.background = "white"
lb.color = "black"
lb.font = ('Verdana', 12)
lb.position = (10, 10)
#lb.align="client"

def change(sender):
  print('selected now:', sender.selected)
  print('item[0]:', sender.item(0))
  print('items[0-2]:', sender.items(0, 2))
  if sender.selected and sender.selected[0] == 2:
     sender.selected = 1

lb.onMouseMove = mouseMove
lb.onClick = click
lb.onDblClick = dblClick
lb.onEnter = enter
lb.onLeave = leave
lb.onKey = keyPressed
lb.onChange = change

app.run()

