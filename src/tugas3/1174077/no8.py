# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:15:52 2019

@author: ASUS
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("tesaja") #membaca nama file dengan nama baca file
anu=sf.shapes() #mengambil semua record data geometri
anu[0].points #mengambil data berisikan shapefile

# In[]