# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:15:29 2019

@author: Ainul Filiani
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
sf.bbox #membaca titik koordinat

# In[]