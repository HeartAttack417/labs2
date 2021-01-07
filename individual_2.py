#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

AB = float(input("Длина первой стороны"))
AC = float(input("Длина второй стороны"))

print("Периметр прямоугольника", ((AB + AC) * 2))
print("Диоганаль прямоугольника", ((math.sqrt(AB ** 2 + AC ** 2))))
