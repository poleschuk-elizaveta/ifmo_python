__author__ = 'TeddyBear'
# -*- coding: utf-8 -*-
import math

#------Нахождение гипотенузы треугольника
#a = int(raw_input("Enter cathetus 1 "))
#b = int(raw_input("Enter cathetus 2 "))
#c = math.sqrt(a*a+b*b)
#print c

#------Рещение квадратного уравнения
"""a = int(raw_input("Enter a "))
b = int(raw_input("Enter b "))
c = int(raw_input("Enter c "))
try:
    D = math.sqrt(b*b-4*a*c)
    print "D = sqrt(", b*b, "-", 4*a*c, ") = ", D
    x1 = (-b+D)/(2*a)
    x2 = (-b-D)/(2*a)
    print "x1= ", x1, "; x2 = ", x2
except:
    print "Решения нет"
    """
#------Таблица умножения
"""while(1):
    if raw_input() == 'e':
        break
    M = int(raw_input("Введите число, для таблицы умножения "))
    a = int(raw_input("С какого числа "))
    b = int(raw_input("По какое "))
    for i in range(a,b+1):
        c = M*i
        print M, "*", i, "=", c
"""
#------Фраза в 3-х разных кодировках
"""str = u"Hello, cruel world! Привет"
arr = ["UTF-8", "Windows-1251", "UTF-16"]
for i in arr:
    print str.encode(i)
"""
#------Поиск максимума
"""arr=[15,12,1,2,3,22,33,11,1,0]
i=0
for j in range(len(arr)-1,0, -1):
    while(i<j):
        print i, j
        if arr[i]>arr[j]:
            d=arr[i]
            j-=1
            print "d, arr[j]", d, arr[j]
        else:
            d=arr[j]
            i+=1
print "Here is result", d
"""
#-----Самое длинное слово в строке
str="Hello, my darling"
arrStr = str.split(" ")
i=0
for j in range(len(arrStr)-1,0, -1):
    while(i<j):
        print i, j
        if len(arrStr[i])>len(arrStr[j]):
            d=arrStr[i]
            j-=1
            print "d, word[j]", d, arrStr[j]
        else:
            d=arrStr[j]
            i+=1
print "Here is result", d

