# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:14:05 2019

@author: lenovo
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