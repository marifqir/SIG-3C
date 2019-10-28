# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:30:31 2019

@author: USER
"""

import shapefile 
sf = shapefile.Reader("soal4") 
anu=sf.shapes() #untuk mengambil semua record data geomtric
anu[0].parts #untuk mengambil data berisikan shaoefile

# In[]