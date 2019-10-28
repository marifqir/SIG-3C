# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:16:09 2019

@author: PandA23
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("contohaja") #digunakan untuk membaca file 
isidata = sf.records() #sf.records maksudnya berisikan data dbf
print(isidata) #mencetak isi data