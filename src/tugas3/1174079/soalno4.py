# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:21:00 2019

@author: ACER
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("no6.py") # menggunakan fungsi reader yang ada pada shapefile untuk membaca file no6.py
eaaaaaaaaa=sf.shapes() # mengambil data tentang shapes yang ada pada variable sf yang berisi no6.py

print (len(eaaaaaaaaa)) # mengeluarkan output dengan hasil perhitungan variable eaaaaaaaaa yang berisi shapes, jumlah shapes akan dihitung
