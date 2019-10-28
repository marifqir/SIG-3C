# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:33:26 2019

@author: USER
"""

import shapefile 
sf = shapefile.Reader("soal4") 
namakolom = sf.fields #untuk melihat atribut table
print(namakolom) #untuk mecetak nama kolom

# In[]
 