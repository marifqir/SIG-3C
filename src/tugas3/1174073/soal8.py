# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:50:28 2019

@author: Ainul Filiani
"""

import shapefile #mengimport kelas shapefile
sf = shapefile.Reader("baca file") #membaca nama file dengan nama baca file
anu=sf.shapes() #mengambil semua record data geometri
anu[0].points #mengambil data berisikan shapefile

# In[]