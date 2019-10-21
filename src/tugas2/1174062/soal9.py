# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:01:43 2019

@author: USER
"""

import shapefile
w=shapefile.Writer("soal9")
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("ngok","dua")

w.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])
w.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])

w.close()