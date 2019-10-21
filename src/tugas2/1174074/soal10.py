# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:41:24 2019

@author: Aspire E15
"""

import shapefile 
w = shapefile.Writer('soal10', shapeType=5) 

w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("joker","batman")
w.record("bane","robin")
w.record("titik","garis")
w.record("besar","kecil")

w.poly([[[1,1],[3,1],[3,3],[1,3],[1,1]]])  
w.poly([[[5,1],[7,1],[7,3],[5,3],[5,1]]])   
w.poly([[[9,1],[11,1],[11,3],[9,3],[9,1]]]) 
w.poly([[[1,5],[3,5],[3,7],[1,7],[1,5]]])    

w.close() 