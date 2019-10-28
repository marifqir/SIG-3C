# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:03:26 2019

@author: ASUS
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("tesaja") #membaca nama file dengan nama baca file
anu=sf.shapes() #mengambil semua record data geometri
anu[0].shapeType #membaca shapetype anu

# In[]