# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:16:44 2019

@author: ASUS
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("tesaja") #membaca nama file dengan nama baca file
namakolom = sf.fields #melihat atribut table
print(namakolom) #mencetak nama kolom

# In[]