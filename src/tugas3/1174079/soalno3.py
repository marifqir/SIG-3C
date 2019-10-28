# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:19:42 2019

@author: ACER
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("no6.py") # menggunakan fungsi reader yang ada pada shapefile untuk membaca file no6.py
print(sf.bbox) #mengeluarkan values bbox  dari sf yang berisi no6.py
