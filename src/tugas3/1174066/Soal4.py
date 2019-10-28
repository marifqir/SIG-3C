# -*- coding: utf-8 -*-
"""
@author: D. Irga B. Naufal Fakhri
"""
# In[0]
import shapefile # Meng-import library shapefile
sf = shapefile.Reader("Nomor10") # Berguna untuk membaca file dari nama filenya tanpa ekstensi
anu=sf.shapes() # Menyimpan hasil yang dibaca kedalam variable anu
len(anu) # Berguna untuk menghitung jumlah yang ada dalam variable anu