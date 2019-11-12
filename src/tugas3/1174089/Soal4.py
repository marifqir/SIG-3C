# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:42:58 2019

@author: ADVENT
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("No10") # untuk membaca file dari nama filenya tanpa ekstensi
anu=sf.shapes() # Menyimpan hasil yang dibaca kedalam variable anu
len(anu) # Berguna untuk menghitung jumlah yang ada dalam variable anu