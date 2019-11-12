import shapefile as shp # import library shapfile sebagai shp
r = shp.Reader("soal10.py") # vairabel dengan yang berisi shapfile reader untuk membaca file soal10.py
print(r.bbox) # print value box dari variable yang dipanggil