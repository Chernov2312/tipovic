import random
from examples.graph import *

x0 = 500
y0 = 500
kx = 25
ky = 25
windowSize(1000, 1000)
canvasSize(1000, 1000)
xmin = -500
xmax = 500


# построение координатных осей
def Axis():
    penColor("black")
    i = 0
    while i < 1000:
        line(i, y0 - 10, i, y0 + 10)
        line(x0 - 10, i, x0 + 10, i)
        i += 25
    line(0, y0, x0 + 500, y0)
    line(x0, 0, x0, y0 + 500)
    for i in range(0, 1000, 25):
        label(-500 // 25 + i // 25, i, y0 + 20)
        label(500 // 25 - i // 25, x0 - 30, i)
    label("X", x0 + 470, y0 - 30)
    label("Y", x0 + 10, y0 - 470)


def func(x):
    return x ** 2 - 7 * x + 2


def func2(x):
    return (-5) * x + 10


def DrawFunc(x):
    f = True
    h = 0.01
    penColor("blue")
    while x <= xmax:
        xe = x0 + x * kx
        ye = y0 - ky * func(x)
        if xe > 1000 or ye > 1000:
            break
        if f:
            moveTo(xe, ye)
            f = False
        else:
            lineTo(xe, ye)
        x += h


def DrawFunc2(x):
    f = True
    h = 0.01
    penColor("blue")
    while x <= xmax:
        xe = x0 + x * kx
        ye = y0 - ky * func2(x)
        if xe > 1000 or ye > 1000:
            break
        if f:
            moveTo(xe, ye)
            f = False
        else:
            lineTo(xe, ye)
        x += h


def BrushFunc(x):
    h = 0.0005

    penColor("red")
    while x <= xmax:
        xe = x0 + kx * x
        yp = random.randint(1, 1000)
        brushColor("red")
        if yp < y0 - ky * func(x) and yp > y0 - ky * func2(x):
            line(xe, y0 - ky * func(x), xe, y0 - ky * func2(x))
        x += h


def Square_left():
    a = 0
    b = 4
    n = 1000
    dx = (b - a) / n
    x_values = []
    i = a
    while i < b - dx:
        x_values.append(i)
        i += (b - dx) / n
    diff_values = []
    for i in x_values:
        diff_values.append(func2(i) - func(i))
    area = sum([i * dx for i in diff_values])
    label(f"Площадь между графиками функций методом левых прямоугольников: {area:.4f}", 0, 0)


def Square_right():
    a = 0
    b = 4
    n = 1000
    h = (b - a) / n
    area = 0
    for i in range(n):
        x_right = a + (i + 1) * h
        f_val = func2(x_right)
        g_val = func(x_right)
        area += abs(max(f_val, g_val) - min(f_val, g_val)) * h
    label(f"Площадь между графиками функций методом правых прямоугольников: {area:.4f}", 0, 50)


Axis()
DrawFunc(xmin)
DrawFunc2(xmin)
BrushFunc(xmin)
Square_left()
Square_right()
run()
