# -*- coding: utf-8 -*-
"""
  Программа к докладу "Программирование простой графики на языке Python",
  учительский день в рамках XI Международной конференции по
  преподаванию информатики в школе, 09.10.2018, Санкт-Петербург
  Автор: К.Ю. Поляков
  E-mail: kpolyakov@mail.ru
  Web: http://kpolyakov.spb.ru

  20_rgb.py - цветовая модель RGB

"""
from simpletk import *

app = TApplication("RGB-кодирование")
app.size = (210, 90)
app.position = (200, 200)

def onChange(sender):
  s = "?"
  bkColor = "SystemButtonFace"
  try:
    r = int(rEdit.text)
    g = int(gEdit.text)
    b = int(bEdit.text)
    if r in range(256) and \
       g in range(256) and b in range(256):
      s = "#{:02X}{:02X}{:02X}".format(r, g, b)
      bkColor = s
  except:
     pass
  rgbLabel.text = s
  rgbRect.background = bkColor

fSans = ("MS Sans Serif", 12)
lblR = TLabel(app, text="R = ", font=fSans )
lblR.position = (5, 5)
lblG = TLabel(app, text="G = " )
lblG.font = fSans
lblG.position = (5, 30)
lblB = TLabel(app, text="B = ", font=fSans )
lblB.position = (5, 55)

fCourier = ("Courier New", 16, "bold")
rgbLabel = TLabel(app, text="#000000", font=fCourier, fg="navy" )
rgbLabel.position = (100, 5)

rgbRect = TLabel(app, text="", width =15, height = 3 )
rgbRect.position = (105, 35)

rEdit = TEdit(app, font=fSans, width=5)
rEdit.position = (45, 5)
rEdit.text = "123"

gEdit = TEdit(app, width=5)
gEdit.position = (45, 30)
gEdit.text = "56"
gEdit.font = fSans

bEdit = TEdit(app, font=fSans, width=5)
bEdit.text = "80"
bEdit.position = (45, 55)

rEdit.onChange = onChange
gEdit.onChange = onChange
bEdit.onChange = onChange

app.run()