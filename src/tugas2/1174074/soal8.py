# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:40:49 2019

@author: Aspire E15
"""

import shapefile 
w=shapefile.Writer('soal8', shapeType = 5)  
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("satu","satu") 
  
w.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]]) 
w.close() 