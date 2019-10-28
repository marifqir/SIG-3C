# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:13:12 2019

@author: PandA23
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("contohaja") #digunakan untuk membaca file
anu=sf.shapes() #menyimpan didalam varaible anu
#%%
len(anu) #menghitung jumlah variable anu