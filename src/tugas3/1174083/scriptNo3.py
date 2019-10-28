# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:19:23 2019

@author: bakti
"""
import shapefile #mengimport shapefile

sf = shapefile.Reader("contohFile") #duntuk membaca file tanpa menggunakan ekstensi
sf.bbox #membaca boundary box atau batas kotak

# In[]