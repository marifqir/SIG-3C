# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:54:15 2019

@author: lenovo
"""

import shapefile

w=shapefile.Writer("soal1")
# In[]

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("ngok","dua")

w.point(1,1)
w.point(2,2)

# In[]
w.close()