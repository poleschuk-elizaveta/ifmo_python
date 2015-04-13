#coding:utf-8
import math
#diameters of circles
d1 = 7
d2 = 49
d3 = 112
#we guess that our internal circles's radiuses must be in inscribed polygon
# (мы считаем, что радиусы  наших внутренних кругов должны лежать на сторонах многоугольника, вписанного (описанного)
# в окружность радиуса d3/2-d1/2 и так далее)

r1 = d1/2
r2 = d2/2
r3 = d3/2
r = r3-3.5
i=2
arrR = list()
arrR.append(r)
arrR.append(r-7)
#try:
while 1:
    print '_______'
    print i
    arrR.append(arrR[i-1]-7)
    if arrR[i] <= 0:
       break
    print arrR[i]
    n = 180/math.asin(7/arrR[i])
    i += 1


#except:
  #  print "Не получилось"


#for i in range(r3-3.5, 7, -7):
   # print i


