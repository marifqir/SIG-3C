# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:51:31 2019

@author: Ainul Filiani
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
namakolom = sf.fields #melihat atribut table
print(namakolom) #mencetak nama kolom

# In[]