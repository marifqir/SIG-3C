# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:40:27 2019

@author: USER
"""

import shapefile
w=shapefile.Writer("soal10", shapeType=5)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("ngok","dua")
w.record("hallo","tiga")
w.record("hai","empat")
w.record("you","lima")
w.record("they","enam")

w.poly([[[1,1],[3,1], [3,3],[1,3],[1,1]]])
w.poly([[[5,1],[7,1], [5,3],[5,3],[5,1]]])
w.poly([[[5,2],[6,3], [8,4],[7,5],[8,2]]])
w.poly([[[4,9],[7,6], [7,3],[2,6],[2,9]]])
w.poly([[[5,5],[3,5], [5,8],[3,8],[5,5]]])
w.poly([[[9,5],[4,5], [2,7],[6,7],[9,5]]])

w.close()

#1174062