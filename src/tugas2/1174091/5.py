# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:39:13 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor5', shapetype=3) #membuat shapefile dengan nama "nomor5" dengan shapetype 3 yaitu garis 
w.shapeType 
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
 
 
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #menghubungkan garis dengan menghubungkan titik koordinat yang ditulis
 
w.close()