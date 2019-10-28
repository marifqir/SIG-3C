# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:34:23 2019

@author: ACER
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("no6.py") # menggunakan fungsi reader yang ada pada shapefile untuk membaca file no6.py
isidataajeebambang = sf.records() #mengambil data berisikan data record
print(isidataajeebambang) #mencetak isi data isidataajeebambang 