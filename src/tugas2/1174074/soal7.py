# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:40:29 2019

@author: Aspire E15
"""

import shapefile 
w=shapefile.Writer("soal7")  
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("satu","satu") 
  
w.line([[[1,3],[5,3],[1,2],[5,2]]]) 
w.close() 