# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:07:35 2019

@author: lenovo
"""

import shapefile

w=shapefile.Writer('soal2', shapeType=1)


w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("ngok","dua")

w.point(1,1)
w.point(2,2)

w.close()