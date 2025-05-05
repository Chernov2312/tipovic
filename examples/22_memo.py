# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  22_memo.py - использование текстового редактора TMemo

"""
from model import calc
from simpletk import *

app = TApplication("Использование TMemo")
app.size = (500, 200)

panel = TPanel(app, relief="raised", height=35, bd=1)
panel.align = "top"

def insertText(event):
  memo.insert(INSERT, lineEdit.text)

def deleteText(event):
  try:
    memo.delete(SEL_FIRST, SEL_LAST)
  except: pass

def copyText(event):
  text = memo.get(1.0, END)  # 1.0 - строка 1 (первая), столбец 0 (первый)
  saveMemo.text = text
  print(saveMemo.getLine(1))

def insertLine(event):
  saveMemo.insertLine(1, lineEdit2.text)

def deleteLine(event):
  saveMemo.deleteLine(1)

fSans = ("MS Sans Serif", 12)
lineEdit = TEdit(panel, font=fSans, width=5)
lineEdit.position = (5, 5)
lineEdit.text = "Петя"

insBtn = TButton(panel, width=5, text="Ins")
insBtn.position = (60, 5)
insBtn.onClick = insertText

delBtn = TButton(panel, width=5, text="Del")
delBtn.position = (100, 5)
delBtn.onClick = deleteText

copyBtn = TButton(panel, width=5, text="Copy")
copyBtn.position = (140, 5)
copyBtn.onClick = copyText

saveMemo = TMemo(app, width = 25, height = 5, # размеры
                  bg = "white",           # фон
                  fg = 'navy',            # цвет символов
                  wrap = "word"           # перенос по словам
                  )
saveMemo.align = "bottom"

savePanel = TPanel(app, relief="raised", height=35, bd=1)
savePanel.align = "bottom"

lineEdit2 = TEdit(savePanel, font=fSans, width=10)
lineEdit2.position = (5, 5)
lineEdit2.text = "Вася"

insBtn2 = TButton(savePanel, width=8, text="Ins line 1")
insBtn2.position = (120, 5)
insBtn2.onClick = insertLine

delBtn2 = TButton(savePanel, width=8, text="Del line 1")
delBtn2.position = (200, 5)
delBtn2.onClick = deleteLine

memo = TMemo(app, width = 25, height = 5, # размеры
                  bg = "white",           # фон
                  fg = 'navy',            # цвет символов
                  wrap = "word"           # перенос по словам
                  )
memo.align = "client"
memo.font = ('Times New Roman', 12)

app.run()
