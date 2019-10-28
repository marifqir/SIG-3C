# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:19:32 2019

@author: ASUS
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("tesaja") #membaca nama file dengan nama baca file
isidata = sf.records() #mengambil semua record
print(isidata[0]) #mencetak isi data record
print(isidata[0][0]) 

# In[]