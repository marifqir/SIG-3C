# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:39:44 2019

@author: Aspire E15
"""

import shapefile 

w=shapefile.Writer('soal5', shapeType = 3) 

w.field("kolom1","C") 
w.field("kolom2","C") 

w.record("satu","satu") 
 
 
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.close() 