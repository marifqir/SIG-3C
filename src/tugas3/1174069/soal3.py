# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:47:03 2019

@author: FannyShafira
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
sf.bbox #membaca boundary box atau batas kotak

# In[]