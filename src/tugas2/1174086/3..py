# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:41:33 2019

@author: acer
"""

import shapefile 
w=shapefile.Writer('soal3',shapeType=3) 
w.shapeType 
w.shapeType=1
w.shapeType 

w.field("kolom1","C") 
w.field("kolom2","C") 

w.record("ngek","satu") 
w.record("ngok","dua") 

w.point(1,1) 
w.point(2,2) 

w.close()