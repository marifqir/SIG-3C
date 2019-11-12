# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:52:53 2019

@author: Ainul Filiani
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
isidata = sf.records() #mengambil data berisikan data dbf
print(isidata) #mencetak isi data dbf

# In[]