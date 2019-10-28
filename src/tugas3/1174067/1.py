import shapefile as shp # import library shapfile sebagai shp
r = shp.Reader("soal10.py") # vairabel dengan yang berisi shapfile reader untuk membaca file soal10.py
print(r.fields) # print fields dari variable r