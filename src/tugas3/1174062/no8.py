# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:31:54 2019

@author: USER
"""

import shapefile 
sf = shapefile.Reader("soal4") 
anu=sf.shapes() 
anu[0].points #untuk mengambil data berisikan shapefile

# In[]