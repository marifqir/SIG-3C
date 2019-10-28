import shapefile as shp # import library shapfile sebagai shp
r   = shp.Reader("soal10.py") # vairabel dengan yang berisi shapfile reader untuk membaca file soal10.py
namakolom = r.fields # implemenntasi fields sebagai variabel
print (namakolom) # print variable namakolom
