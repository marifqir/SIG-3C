# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:39:15 2019

@author: Aspire E15
"""

import shapefile

w=shapefile.Writer('soal3', shapeType = 3)
w.shapeType
w.shapeType=1
w.shapeType

# In[]

w.field("kolom1","C")
w.field("kolom2","C")

w.record("satu","satu")
w.record("dua","dua")

w.point(1,1)
w.point(2,2)

# In[]
w.close()