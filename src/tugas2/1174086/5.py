# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:30:16 2019

@author: acer
"""

import shapefile 
w=shapefile.Writer('soal5',shapeType=3) 
w.shapeType 

w.field("kolom1","C") 
w.field("kolom2","C") 

w.record("ngek","satu") 
 
 
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) 

w.close() 