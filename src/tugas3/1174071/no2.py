# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:01:09 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") # untuk membaca shape file
# In[] : untuk mengetahui type shape file yang digunakan
sf.shapeType 