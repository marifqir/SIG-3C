# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:12:28 2019

@author: ASUS
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("tesaja") #membaca nama file dengan nama baca file
anu=sf.shapes() #mengambil semua record data geometri
dir(anu) #mengambil data objek yaitu anu
dir(anu[0])

# In[]