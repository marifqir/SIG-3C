# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:16:15 2019

@author: Aulyardha Anindita
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
anu=sf.shapes() #mengambil semua record data geometri
len(anu) #menghitung jumlah variabel anu

# In[]