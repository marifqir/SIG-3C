# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:07:30 2019

@author: ACER
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("no6.py") # menggunakan fungsi reader yang ada pada shapefile untuk membaca file no6.py
print(sf.fields) #mengeluarkan input field dari sf yang berisi no1.py

