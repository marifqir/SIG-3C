# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:57:37 2019

@author: lenovo
"""

import shapefile 
w=shapefile.Writer("soal7")  
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
  
w.line([[[1,3],[5,3],[1,2],[5,2]]]) 
w.close() 