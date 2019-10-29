# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:18:03 2019

@author: Ainul Filiani
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
anu=sf.shapes() #mengambil semua record data geometri
dir(anu) #mengambil data objek yaitu anu
dir(anu[0])

# In[]