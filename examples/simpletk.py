# -*- coding: utf-8 -*-
"""
Библиотека SIMPLETK
Версия 0.3

SIMPLETK - это "обертка" над стандартной библиотекой tkinter,
которая используется в языке Python для разработки приложений с
графическим интерфейсом. В ней упрощён доступ ко многим возможностям
библиотеки tkinter, в то же время сохранена возможность использования
всех средств tkinter.

ЛИЦЕНЗИЯ

Copyright (c) 2014-2016, Константин Поляков
Все права защищены.

Разрешается повторное распространение и использование как в виде исходного
кода, так и в двоичной форме, с изменениями или без, при соблюдении
следующих условий:
  1) При повторном распространении исходного кода должно оставаться указанное
     выше уведомление об авторском праве, этот список условий и последующий
     отказ от гарантий.
  2) При повторном распространении двоичного кода должна сохраняться указанная
     выше информация об авторском праве, этот список условий и последующий
     отказ от гарантий в документации и/или в других материалах,
     поставляемых при распространении.
  3) Ни название Организации, ни имена ее сотрудников не могут быть
     использованы в качестве поддержки или продвижения продуктов,
     основанных на этом ПО без предварительного письменного разрешения.

ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ ЛЮБОГО ВИДА
ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ
ГАРАНТИЯМИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ
И НЕНАРУШЕНИЯ ПРАВ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ
ОТВЕТСТВЕННОСТИ ПО ИСКАМ О ВОЗМЕЩЕНИИ УЩЕРБА, УБЫТКОВ ИЛИ ДРУГИХ ТРЕБОВАНИЙ
ПО ДЕЙСТВУЮЩИМ КОНТРАКТАМ, ДЕЛИКТАМ ИЛИ ИНОМУ, ВОЗНИКШИМ ИЗ, ИМЕЮЩИМ ПРИЧИНОЙ
ИЛИ СВЯЗАННЫМ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ПРОГРАММНОГО
ОБЕСПЕЧЕНИЯ ИЛИ ИНЫМИ ДЕЙСТВИЯМИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.
"""

from tkinter.constants import *
CLIENT = "client"

__all__ = [
# Symbolic constants for Tk
# Booleans
'NO', 'FALSE', 'OFF', 'YES', 'TRUE', 'ON',

# -anchor and -sticky
'N', 'S', 'W', 'E', 'NW', 'SW', 'NE', 'SE', 'NS', 'EW', 'NSEW', 'CENTER',

# -fill
'NONE', 'X', 'Y', 'BOTH', 'CLIENT',

# -side
'LEFT', 'TOP', 'RIGHT', 'BOTTOM',

# -relief
'RAISED', 'SUNKEN', 'FLAT', 'RIDGE', 'GROOVE', 'SOLID',

# -orient
'HORIZONTAL', 'VERTICAL',

# -tabs
'NUMERIC',

# -wrap
'CHAR', 'WORD',

# -align
'BASELINE',

# -bordermode
'INSIDE', 'OUTSIDE',

# Special tags, marks and insert positions
'SEL', 'SEL_FIRST', 'SEL_LAST', 'END', 'INSERT', 'CURRENT', 'ANCHOR',
'ALL', # e.g. Canvas.delete(ALL)

# Text widget and button states
'NORMAL', 'DISABLED', 'ACTIVE',
# Canvas state
'HIDDEN',

# Menu item types
'CASCADE', 'CHECKBUTTON', 'COMMAND', 'RADIOBUTTON', 'SEPARATOR',

# Selection modes for list boxes
'SINGLE', 'BROWSE', 'MULTIPLE', 'EXTENDED',

# Activestyle for list boxes
# NONE='none' is also valid
'DOTBOX', 'UNDERLINE',

# Various canvas styles
'PIESLICE', 'CHORD', 'ARC', 'FIRST', 'LAST', 'BUTT', 'PROJECTING',
'ROUND', 'BEVEL', 'MITER',

# Arguments to xview/yview
'MOVETO', 'SCROLL', 'UNITS', 'PAGES',

        'TApplication',
        'TLabel',
        'TButton',
        'TCanvas',
        'TImage',
        'TPanel',
        'TEdit',
        'TMemo',
        'TListBox',
        'TComboBox',
        'TRadioGroup',
        'TCheckBox',
        'TGroupBox',
        'PhotoImage'
        ]

import tkinter
from tkinter import ttk
try:
  from PIL import ImageTk, Image
except:
  pass

#-------------------------------------------------------------
#   TAPPLICATION
#-------------------------------------------------------------
class TApplication(tkinter.Tk):

    def __init__(self, title0):
      tkinter.Tk.__init__(self)
      self.title(title0)
      self.__size = (200, 200)
      self.__position = (200, 200)
      self.__resizable = (True, True)
      self.__minsize = (1, 1)
      self.__maxsize = (self.winfo_screenwidth(),
                        self.winfo_screenheight())
      self.__background = ""
      self.__onCloseQuery = None
      self.protocol("WM_DELETE_WINDOW", self.__intOnCloseQuery)
      self.__default = None
      self.bind('<Return>', self.__onReturn)
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)
      self.__onResize = None
      self.bind('<Configure>', self.__intOnResize)

    def __setGeometry (self):
      pos = self.__position
      size = self.__size
      self.geometry("{:d}x{:d}+{:d}+{:d}".format(*(size+pos)))

    def __setPosition (self, pos):
      self.__position = pos
      self.__setGeometry()

    def __setSize (self, size):
      self.__size = size
      self.__setGeometry()

    def __setResizable (self, value):
      self.__resizable = value
      super(TApplication,self).resizable(width=value[0], height=value[1])

    def __setMinsize (self, value):
      self.__minsize = value
      super(TApplication,self).minsize(width=value[0], height=value[1])

    def __setMaxsize (self, value):
      self.__maxsize = value
      super(TApplication,self).maxsize(width=value[0], height=value[1])

    def __setBackground (self, value):
      self.__background = value
      super(TApplication,self).configure(background=value)

    def __onReturn(self, event):
      if self.__default:
        self.__default.invoke()
    def __setDefault(self, obj):
      self.__default = obj

    def __intOnCloseQuery(self):
      if self.__onCloseQuery:
        self.__onCloseQuery()
      else:
        self.destroy()
    def __setOnCloseQuery(self, func):
      self.__onCloseQuery = func

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def __intOnResize(self, event):
      if self.__onResize:
        self.__onResize(event)
    def __setOnResize(self, func):
      self.__onResize = func

    def Run(self):
      self.run()
    def run(self):
      self.mainloop()

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    resizable = property(lambda x: x.__resizable, __setResizable)
    minsize = property(lambda x: x.__minsize, __setMinsize)
    maxsize = property(lambda x: x.__maxsize, __setMaxsize)
    default = property(lambda x: x.__default, __setDefault)
    background = property(lambda x: x.__background, __setBackground)

    onCloseQuery = property(lambda x: x.__onCloseQuery, __setOnCloseQuery)
    onResize = property(lambda x: x.__onResize, __setOnResize)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TPANEL
#-------------------------------------------------------------
class TPanel(tkinter.Frame):

    def __init__(self, parent, **kw):
      tkinter.Frame.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (20, 20)
      self.__size = (kw.get("width") or 200,
                     kw.get("height") or 100)
      self.__align = None
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setBackground(self, value):
      self["bg"] = value
      print(self["bg"])

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    size = property(lambda x: x.__size, __setSize)
    position = property(lambda x: x.__position, __setPosition)
    align = property(lambda x: x.__align, __setAlign)
    background = property(lambda x: x["bg"], __setBackground)
    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TLABEL
#-------------------------------------------------------------
class TLabel(tkinter.Label):

    def __init__(self, parent, **kw):
      tkinter.Label.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__onClick = None
      self.__align = None
        #self.bind("<ButtonPress-1>", self.__intOnClick)
        #self.bind("<ButtonRelease-1>", self.__intOnClick)
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)

    def __setFont (self, value):
      self["font"] = value

    def __setText(self, value):
      self["text"] = value

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    text = property(lambda x: x["text"], __setText)
    font = property(lambda x: x["font"], __setFont)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TBUTTON
#-------------------------------------------------------------
class TButton(tkinter.Button):

    def __init__(self, parent, **kw):
      tkinter.Button.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__onClick = None
      self["command"] = self.__intOnClick
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)

    def __setFont (self, value):
      self["font"] = value

    def __setText(self, value):
      self["text"] = value

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self):
      if self.__onClick:
        self.__onClick(self)
    def click(self):
      self.__onClick(self)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    text = property(lambda x: x["text"], __setText)
    font = property(lambda x: x["font"], __setFont)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TCHECKBOX
#-------------------------------------------------------------
class TCheckBox(tkinter.Checkbutton):

    def __init__(self, parent, **kw):
      self.__var = tkinter.IntVar()
      tkinter.Checkbutton.__init__(self, parent, **kw)
      self["onvalue"] = 1
      self["offvalue"] = 0
      self["variable"] = self.__var
      self.__parent = parent
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__onChange = None
      self["command"] = self.__intOnChange
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)

    def __setText(self, value):
      self["text"] = value

    def __setFont (self, value):
      self["font"] = value

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __setChecked (self, value):
      if self.__var != value:
        self.__var = int(value)
        if self.__onChange:
          self.__onChange(self)

    def __intOnChange(self):
      if self.__onChange:
        self.__onChange(self)
    def __setOnChange(self, func):
      self.__onChange = func

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    text = property(lambda x: x["text"], __setText)
    font = property(lambda x: x["font"], __setFont)
    checked = property(lambda x: x.__var.get() == 1, __setChecked)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    onChange = property(lambda x: x.__onChange, __setOnChange)

#-------------------------------------------------------------
#   TCANVAS
#-------------------------------------------------------------
class TCanvas(tkinter.Canvas):

    def __init__(self, parent, **kw):
      tkinter.Canvas.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == "client":
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TIMAGE
#-------------------------------------------------------------
def PhotoImage(file):
    return tkinter.PhotoImage(file = file)

class TImage(TCanvas):

    def __init__(self, parent, **kw):
      TCanvas.__init__(self, parent, **kw)
      self.__parent = parent
      self.__center = tkinter.NO
      self.__picture = None
      self.bind("<Configure>", self.__onResize)

    def __onResize(self, ev):
      self.redrawImage()

    def redrawImage(self):
      self.delete("all")
      pic = self.__picture
      if pic:
        x0, y0 = 0, 0
        if self.__center:
          self.update()
          x0 = max( 0, (self.winfo_width()-pic.width())//2 )
          y0 = max( 0, (self.winfo_height()-pic.height())//2 )
        try:
          self.create_image(x0, y0, anchor=tkinter.NW, image=pic)
        except: pass

    def __setCenter (self, value):
      if self.__center != value:
        self.__center = value
        self.redrawImage()

    def __setPicture (self, fName):
      try:
        if fName.lower().endswith('.gif'):
          self.__picture = tkinter.PhotoImage(file = fName)
        else:
          im = Image.open(fName)
          self.__picture = ImageTk.PhotoImage(im)
        self.redrawImage()
      except:
        self.delete("all")

    center = property(lambda x: x.__center == 1, __setCenter)
    picture = property(lambda x: x.__picture, __setPicture)

#-------------------------------------------------------------
#   TEDIT
#-------------------------------------------------------------
class TEdit(tkinter.Entry):

    def __init__(self, parent, **kw):
      tkinter.Entry.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (0, 0)
      self.__width = self["width"]
      self.__onChange = None
      self.__onValidate = None
      self.__var = tkinter.StringVar()
      self["textvariable"] = self.__var
      self.__text = self.__var.get()
      self.__var.trace("w", self.__trace)
      self.__align = None
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setWidth (self, width):
      self["width"] = width

    def __trace(self, *args):
      valid = tkinter.YES
      if self.__onValidate:
        valid = self.__onValidate()
      if valid:
        self.__text = self.__var.get()
        if self.__onChange:
          self.__onChange(self)
      else:
        self.__var.set(self.__text)

    def __setFont (self, value):
      self["font"] = value

    def __setText(self, value):
      self.__var.set(value)
      self.update()
      if self.__onChange:
        self.__onChange(self)

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange:
        self.__onChange(self)

    def __setOnValidate(self, func):
      self.__onValidate = func

    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    width = property(lambda x: x.__width, __setWidth)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    text = property(lambda x: x.__var.get(), __setText)
    font = property(lambda x: x["font"], __setFont)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    onChange = property(lambda x: x.__onChange, __setOnChange)
    onValidate = property(lambda x: x.__onValidate, __setOnValidate)

#-------------------------------------------------------------
#   TCOMBOBOX
#-------------------------------------------------------------
class TComboBox(ttk.Combobox):

    def __init__(self, parent, **kw):
      ttk.Combobox.__init__(self, parent, **kw)
      self.__parent = parent
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__onValidate = None
      self.__onChange = None
      self.__var = tkinter.StringVar()
      self["textvariable"] = self.__var
      self.__text = self.__var.get()
      self.__var.trace("w", self.__trace)
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == "client":
        self.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setText(self, value):
      self.set(value)
      self.update()

    def findItem(self, value):
      if not self["values"]:
        return False
      else:
        return value in self["values"]

    def addItem(self, value):
      if not self["values"]:
        self["values"] = (value,)
      else:
        self["values"] = self["values"] + (value,)

    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange:
        self.__onChange(self)

    def __setOnValidate(self, func):
      self.__onValidate = func

    def __setFont (self, value):
      self["font"] = value
      root = self.nametowidget(self.winfo_parent())
      root.option_add('*TCombobox*Listbox.font', value)

    def __trace(self, *args):
      valid = tkinter.YES
      if self.__onValidate:
        valid = self.__onValidate(self)
      if valid:
        self.__text = self.__var.get()
        if self.__onChange:
          self.__onChange(self)
      else:
        self.__var.set(self.__text)

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    text = property(lambda x: x.__var.get(), __setText)
    font = property(lambda x: x["font"], __setFont)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

    onChange = property(lambda x: x.__onChange, __setOnChange)
    onValidate = property(lambda x: x.__onValidate, __setOnValidate)

#-------------------------------------------------------------
#   TLISTBOX
#-------------------------------------------------------------
class TListBox(tkinter.Listbox):

    def __init__(self, parent, values, **kw):
      self.__panel = TPanel(parent)
      tkinter.Listbox.__init__(self, self.__panel, **kw)
      for item in values:
        self.insert(tkinter.END, item)
      self.__sbar = tkinter.Scrollbar(self.__panel, orient=tkinter.VERTICAL)
      self.__sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
      self.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
      self.__sbar.config(command=self.yview)
      self.configure(yscrollcommand=self.__sbar.set)
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)
      self.__onChange = None
      self.bind('<<ListboxSelect>>', self.__intOnChange)

    def __setPosition (self, pos):
      self.__position = pos
      self.__panel.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.__panel.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.__panel.pack(side=align, fill=tkinter.Y)
      elif align == "client":
        self.__panel.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __setFont (self, value):
      self["font"] = value

    def __setSelected(self, value):
      self.selection_clear(0, tkinter.END);
      try: iter(value)
      except: value = (value,)
      for val in value:
        self.selection_set(val);

    def item(self, itemNo):
      return self.get(itemNo); 

    def items(self, fromItem, toItem):
      return self.get(fromItem, toItem); 

    def __intOnChange(self, event):
      if self.__onChange:
        self.__onChange(self)
    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange:
        self.__onChange(self)

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    font = property(lambda x: x["font"], __setFont)
    selected = property(lambda x: x.curselection(), __setSelected)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onKey = property(lambda x: x.__onKey, __setOnKey)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)
    onChange = property(lambda x: x.__onChange, __setOnChange)

#-------------------------------------------------------------
#   TRADIOGROUP
#-------------------------------------------------------------
class TRadioGroup(TPanel):

    def __init__(self, parent, values, **kw):
      self.__parent = parent
      self.__var = tkinter.IntVar()
      TPanel.__init__(self, parent, **kw)
      self.buttons = []
      self.pack_propagate(0) 
      for code, text in enumerate(values):
        btn = tkinter.Radiobutton(self, text=text,
            variable=self.__var, value=code,
            command=self.__intOnChange)        
        btn.pack(anchor=tkinter.W)
        self.buttons.append(btn)
      if len(values):
        self.__var.set(values[0])

    def __setBackground(self, value):
      self["bg"] = value
      for btn in self.buttons:
        btn["bg"] = value

    def __setColor(self, value):
      for btn in self.buttons:
        btn["fg"] = value

    def __setFont (self, value):
      for btn in self.buttons:
        btn["font"] = value

    def __setSelected (self, value):
      self.__var.set(value)

    def __intOnChange(self):
      if self.__onChange:
        self.__onChange(self)
    def __setOnChange(self, func):
      self.__onChange = func
      if self.__onChange:
        self.__onChange(self)

    def item(self, itemNo):
      return self.buttons[itemNo]["text"]; 

    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    selected = property(lambda x: x.__var.get(), __setSelected)
    font = property(lambda x: x["font"], __setFont)

    onChange = property(lambda x: x.__onChange, __setOnChange)

#-------------------------------------------------------------
#   TGROUPBOX
#-------------------------------------------------------------
class TGroupBox(tkinter.LabelFrame):

    def __init__(self, parent, **kw):
      tkinter.LabelFrame.__init__(self, parent, **kw)
      self.__position = (0, 0)
      self.__size = (self["width"], self["height"])
      self.__align = None
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.place( x = self.__position[0], y = self.__position[1] )

    def __setSize (self, size):
      self.__size = size
      self["width"] = size[0]
      self["height"] = size[1]

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.pack(side=align, fill=tkinter.Y)
      elif align == CLIENT:
        self.pack(fill=tkinter.BOTH, expand=YES)

    def __setFont (self, value):
      self["font"] = value

    def __setText(self, value):
      self["text"] = value

    def __setBackground(self, value):
      self["bg"] = value

    def __setColor(self, value):
      self["fg"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    position = property(lambda x: x.__position, __setPosition)
    size = property(lambda x: x.__size, __setSize)
    align = property(lambda x: x.__align, __setAlign)
    text = property(lambda x: x["text"], __setText)
    font = property(lambda x: x["font"], __setFont)
    color = property(lambda x: x["fg"], __setColor)
    background = property(lambda x: x["bg"], __setBackground)
    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onKey = property(lambda x: x.__onKey, __setOnKey)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

#-------------------------------------------------------------
#   TMEMO
#-------------------------------------------------------------
class TMemo(tkinter.Text):

    def __init__(self, parent, **kw):
      self.__panel = TPanel(parent)
      tkinter.Text.__init__(self, self.__panel, **kw)
      self.__sbar = tkinter.Scrollbar(self.__panel, orient=tkinter.VERTICAL)
      self.__sbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
      self.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
      self.__sbar.config(command=self.yview)
      self.configure(yscrollcommand=self.__sbar.set)
      self.__position = (0, 0)
      self.__onEnter = None
      self.bind('<Enter>', self.__intOnEnter)
      self.__onLeave = None
      self.bind('<Leave>', self.__intOnLeave)
      self.__onKey = None
      self.bind('<Key>', self.__intOnKey)
      self.__onClick = None
      self.bind('<Button>', self.__intOnClick)
      self.__onDblClick = None
      self.bind('<Double-Button>', self.__intOnDblClick)
      self.__onMouseMove = None
      self.bind('<Motion>', self.__intOnMouseMove)

    def __setPosition (self, pos):
      self.__position = pos
      self.__panel.place( x = self.__position[0], y = self.__position[1] )

    def __setAlign(self, align):
      self.__align = align
      if align == tkinter.TOP  or  align == tkinter.BOTTOM:
        self.__panel.pack(side=align, fill=tkinter.X)
      elif align == tkinter.LEFT  or  align == tkinter.RIGHT:
        self.__panel.pack(side=align, fill=tkinter.Y)
      elif align == "client":
        self.__panel.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def __getText(self):
      text = self.get(1.0, tkinter.END)
      return text

    def __setText(self, text):
      self.delete(1.0, tkinter.END)
      self.insert(tkinter.INSERT, text)

    def getLine(self, lineNo):
      text = self.get(1.0, tkinter.END).splitlines()
      if lineNo < len(text):
        return text[lineNo]
      else:
        return ""

    def insertLine(self, lineNo, s):
      text = self.get(1.0, tkinter.END).splitlines()
      text.insert(lineNo, s)
      self.text = "\n".join(text)

    def deleteLine(self, lineNo):
      text = self.get(1.0, tkinter.END).splitlines()
      if lineNo < len(text):
        del text[lineNo]
        self.text = "\n".join(text)

    def __setFont (self, value):
      self["font"] = value

    def __intOnEnter(self, event):
      if self.__onEnter:
        self.__onEnter(event)
    def __setOnEnter(self, func):
      self.__onEnter = func

    def __intOnLeave(self, event):
      if self.__onLeave:
        self.__onLeave(event)
    def __setOnLeave(self, func):
      self.__onLeave = func

    def __intOnKey(self, event):
      if self.__onKey:
        self.__onKey(event)
    def __setOnKey(self, func):
      self.__onKey = func

    def __intOnMouseMove(self, event):
      if self.__onMouseMove:
        self.__onMouseMove(event)
    def __setOnMouseMove(self, func):
      self.__onMouseMove = func

    def __intOnClick(self, event):
      if self.__onClick:
        self.__onClick(event)
    def __setOnClick(self, func):
      self.__onClick = func

    def __intOnDblClick(self, event):
      if self.__onDblClick:
        self.__onDblClick(event)
    def __setOnDblClick(self, func):
      self.__onDblClick = func

    align = property(lambda x: x.__align, __setAlign)
    position = property(lambda x: x.__position, __setPosition)
    text = property(__getText, __setText)
    font = property(lambda x: x["font"], __setFont)

    onKey = property(lambda x: x.__onKey, __setOnKey)

    onEnter = property(lambda x: x.__onEnter, __setOnEnter)
    onLeave = property(lambda x: x.__onLeave, __setOnLeave)
    onMouseMove = property(lambda x: x.__onMouseMove, __setOnMouseMove)
    onClick = property(lambda x: x.__onClick, __setOnClick)
    onDblClick = property(lambda x: x.__onDblClick, __setOnDblClick)

