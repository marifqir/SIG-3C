# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:12:00 2019

@author: PandA23
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("contohaja") #digunakan untuk membaca file 
#%%
sf.bbox #membaca boundary box atau batas kotak