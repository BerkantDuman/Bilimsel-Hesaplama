from scipy.linalg import solve
import math


def f(x,y):
    return 4 - x**2 - y**2


def g(x,y):
    return 1 - math.exp(x) - y


def dFx(x):
    return -2*x


def dFy(y):
    return -2*y


def dGx(x):
    return -math.exp(x)


def dGy(y):
    return -1



x0 = float(input("x'in başlangıç değerini giriniz: "))
y0 = float(input("y'nin başlangıç değerini giriniz: "))

deltaX = 1
deltaY = 1
counter = 0

while abs(deltaX) > 00000.1 and abs(deltaY) > 00000.1:
    
    counter += 1
    matris1 = [[dFx(x0), dFy(y0)], [dGx(x0), dGy(y0)]]
    matris2 = [-f(x0,y0), -g(x0,y0)]
    
    result = solve(matris1, matris2)
    deltaX = result[0]
    deltaY = result[1] 
     
    x0 = x0 + deltaX
    y0 = y0 + deltaY

print(x0, y0, counter) 
