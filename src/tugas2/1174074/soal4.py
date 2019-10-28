# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:39:25 2019

@author: Aspire E15
"""

import shapefile

w=shapefile.Writer('soal4', shapefile.POINTM)
w.shapeType=1

w.field("kolom1","C") 
w.field("kolom2","C") 

w.record("satu","satu") 
w.record("dua","dua") 

w.point(1,1) 
w.point(2,2) 

w.close() 