# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:31:40 2019

@author: ACER
"""


import shapefile # Meng-import library shapefile
sf = shapefile.Reader("no6.py") # menggunakan fungsi reader yang ada pada shapefile untuk membaca file no6.py
namakolom = sf.fields
print (namakolom) # membaca parts yang ada