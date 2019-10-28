# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:44:21 2019

@author: User
"""

import shapefile #mengimport library
sf = shapefile.Reader("Nomor1") #membaca file
print(sf.bbox) #mengeluarkan values bbox