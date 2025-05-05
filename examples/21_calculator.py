# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  21_calculator.py - калькулятор

"""
from model import calc
from simpletk import *

app = TApplication("Калькулятор")
app.size = (200, 150)

inp = TComboBox(app, values=[], height=1)
inp.align = "top"
inp.text = "2+2"

answers = TListBox(app)
answers.align = "client"

def doCalc(event):
  ENTER = 13
  if event.keycode == ENTER:
    expr = inp.text
    x = calc(expr)
    answers.insert(0, expr+"="+str(x))
    if not inp.findItem(expr):
      inp.addItem(expr)

inp.onKey = doCalc

app.run()
