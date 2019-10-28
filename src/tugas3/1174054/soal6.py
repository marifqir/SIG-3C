# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:47:25 2019

@author: Aulyardha Anindita
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
anu=sf.shapes() #mengambil semua record data geometri
anu[0].shapeType #membaca shapetype anu

# In[]