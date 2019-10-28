# -*- coding: utf-8 -*-
"""
@author: D. Irga B. Naufal Fakhri
"""
# In[0]
import shapefile # Meng-import library shapefile
sf = shapefile.Reader("Nomor10") # Berguna untuk membaca file dari nama filenya tanpa ekstensi
sf.shapeType # Berguna untuk membaca type shape yang digunakan pada file pyshp tersebut