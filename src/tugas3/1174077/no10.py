# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:18:05 2019

@author: ASUS
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("tesaja") #membaca nama file dengan nama baca file
isidata = sf.records() #mengambil data berisikan data dbf
print(isidata) #mencetak isi data dbf

# In[]