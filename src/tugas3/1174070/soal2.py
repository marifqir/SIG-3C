# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:46:40 2019

@author: User
"""

import shapefile #mengimprot shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
sf.shapeType #untuk membaca type shape berapakah yang digunakan

# In[]