# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:48:42 2019

@author: Ainul Filiani
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
anu=sf.shapes() #mengambil semua record data geometri
anu[0].parts #membuat dua record menjadi satu

# In[]