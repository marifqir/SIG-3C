# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:53:59 2019

@author: Aulyardha Anindita
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
isidata = sf.records() #mengambil semua record
print(isidata[0]) #mencetak isi data record
print(isidata[0][0]) 

# In[]