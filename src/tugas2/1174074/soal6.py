# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:39:59 2019

@author: Aspire E15
"""

import shapefile 

w=shapefile.Writer("soal6")  
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("satu","satu") 
  
w.line([[[1,3],[5,3]]]) 
w.close() 