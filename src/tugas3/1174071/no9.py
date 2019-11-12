# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:32:05 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") 
# In[] : menampilkan fields/kolom dari shape file
namakolom = sf.fields
print(namakolom)