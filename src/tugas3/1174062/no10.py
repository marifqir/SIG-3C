# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:34:42 2019

@author: USER
"""

import shapefile 
sf = shapefile.Reader("soal4") 
isidata = sf.records() #untuk mengambil data berisikan data dbf
print(isidata) #untuk mencetak isi data dbf

# In[]