# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:38:40 2019

@author: acer
"""

import shapefile 
w=shapefile.Writer('soal2', shapeType=1) 
w.shapeType 

w.field("kolom1","C") 
w.field("kolom2","C") 

w.record("ngek","satu") 
w.record("ngok","dua") 

w.point(1,1) 
w.point(2,2) 

w.close() 
 