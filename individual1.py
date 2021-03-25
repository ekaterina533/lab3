#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input("введите число экзаменов:"))
if N == 1: print("мы успешно сдали",N, "экзамен")
elif N>20:print("Ошибка")
elif N>4: print("мы успешно сдали",N, "экзаменов")
elif N<5:print("мы успешно сдали",N, "экзамена")
elif N==0:print("мы успешно сдали",N, "экзаменов")
elif N>21:print("Ошибка")