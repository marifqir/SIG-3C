# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:05:14 2019

@author: ASUS
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("tesaja") #membaca nama file dengan nama baca file
sf.bbox #membaca titik koordinat

# In[]