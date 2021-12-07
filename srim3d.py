# -*- coding: utf-8 -*-
# srim3d.py by Gustav Lindberg
# https://github.com/Gustav-Lindberg/Srim3D.py

import numpy as np
import re as RegExp

def extractData(file="Ioniz-3D.txt"):
    data = []
    with open(file) as file:
        hasStarted = False
        topRegex = RegExp.compile(r"^-+\s-+$")
        spaceRegex = RegExp.compile(r"\s+")
        for line in file:
            if(topRegex.match(line)):
                hasStarted = True
                continue
            elif(not hasStarted):
                continue
            numbers = list(map(lambda s: float(s), spaceRegex.split(line.strip())))
            data.append(numbers[1:])
    return np.array(data)

def ions(data):
    return np.array(list(map(lambda row: sum(row), data)))

def transverseIons(data):
    return np.array(list(map(lambda column: sum(column), data.T)))
