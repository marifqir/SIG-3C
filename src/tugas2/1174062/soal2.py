# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:25:51 2019

@author: USER
"""

import shapefile
w=shapefile.Writer('Tugas 2',shapeType=1)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("ngok","dua")

w.point(1,1)
w.point(2,2)

w.close()