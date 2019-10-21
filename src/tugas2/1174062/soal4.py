# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:37:22 2019

@author: USER
"""

import shapefile
w=shapefile.Writer('soal4', shapefile.POINTM)
w.shapeType=1

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("ngok","dua")

w.point(1,1)
w.point(2,2)

w.close()
