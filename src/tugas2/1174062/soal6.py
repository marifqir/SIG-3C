# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:18:09 2019

@author: USER
"""

import shapefile
w=shapefile.Writer('soal6', shapeType=5)

w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngke","satu")

w.poly([[[1,3],[5,3]]])

w.close()