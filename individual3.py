#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from array import *
d=int(input("Введите день"))
m=int(input("Введите месяц"))
y=int(input("Введите год"))
if d>31: print("Ошибка")
elif m>12: print("Ошибка")
data = array('i', [31,28,31,30,31,30,31,31,30,31,30,31])
k=0
while m > 1:
    k+=data[m-2]
    m -= 1
k+=d
if y%4==0 and y%100==0 and y%400!=0: k=k
else:k=k+1
print("Порядковый номер даты, начиная с начала года",k)