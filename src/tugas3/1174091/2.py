# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:38:54 2019

@author: User
"""

import shapefile #mengimport library shapefile
sf = shapefile.Reader("Nomor10") #membaca nama file
print(sf.shapeType) #membaca type shape
