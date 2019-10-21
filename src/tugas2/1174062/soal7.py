# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:31:54 2019

@author: USER
"""

import shapefile
w=shapefile.Writer("Soal7")
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")

w.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]])

w.close()