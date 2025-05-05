# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  19_viewer.py - просмотрщик рисунков

"""
from simpletk import *
from tkinter import filedialog

app = TApplication("Просмотр рисунков")
app.position = (200, 200)
app.size = (300, 300)

panel = TPanel(app, relief="raised", height=40, bd=1)
panel.align = "top"

image = TImage(app, bg="white")
image.align = "client"
# image.picture = "flower.gif"
# image.picture = "lamplogo.jpg" # только если есть PIL

def selectFile(sender):
  fname = filedialog.askopenfilename(
     filetypes=[("Файлы GIF", "*.gif"),
                ("Все файлы", "*.*")] )
     #filetypes=[("Файлы GIF", "*.gif"),  # если есть PIL
     #           ("Файлы JPEG", "*.jpg"),
     #           ("Файлы PNG", "*.png"),
     #           ("Все файлы", "*.*")] )
  if fname:
    image.picture = fname

openBtn = TButton(panel, width=13, text="Открыть файл")
openBtn.position = (5, 5)
openBtn.onClick = selectFile
openBtn.font = ('Helvetica', 10)

def cbChanged(sender):
  image.center = sender.checked
  image.redrawImage()

centerCb = TCheckBox(panel,text="В центре")
centerCb.position = (125, 8)
centerCb.onChange = cbChanged
centerCb.font = ('Courier New', 12)

app.run()

