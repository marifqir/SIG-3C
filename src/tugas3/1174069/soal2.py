# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:45:06 2019

@author: FannyShafira
"""

import shapefile #mengimprot shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
sf.shapeType #untuk membaca type shape berapakah yang digunakan

# In[]