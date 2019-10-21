# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:48:54 2019

@author: lenovo
"""

import shapefile 
w=shapefile.Writer('soal10', shapeType=5)  
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("slebew","satu") 
w.record("slebew","dua")
w.record("slebew","tiga")
w.record("prett","empat")
w.record("prett","lima")
w.record("prett","enam")
w.record("blubuk","tujuh")


  
w.poly([[[0,0],[6,0],[0,4],[0,0]]])
w.poly([[[0,7],[6,7],[0,11],[0,7]]])
w.poly([[[0,14],[6,14],[0,18],[0,14]]]) 
w.poly([[[7,7],[13,7],[7,11],[7,7]]])
w.poly([[[7,14],[13,14],[7,18],[7,14]]])
w.poly([[[14,14],[20,14],[14,18],[14,14]]]) 
w.poly([[[14,0],[20,0],[14,4],[14,0]]])
w.close() 