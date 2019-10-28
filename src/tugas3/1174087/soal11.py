# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:18:24 2019

@author: PandA23
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("contohaja") #digunakan untuk membaca file 
isidata = sf.records() #sf.records maksudnya berisikan data dbf
#%%
print(isidata[0]) #untuk melihat data record pertama
#%%
print(isidata[0][0]) #untuk melihat data record spesifik