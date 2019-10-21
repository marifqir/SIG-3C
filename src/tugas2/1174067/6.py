import shapefile as shp #import library shapfile sebagai shp
w=shp.Writer('soal6', shapeType=5) #membuat file bernama soal6 yang berisi gambar polygon sesuai dengan shaptype 5 yaitu polygon
 
w.field("kolom1","C") #membuat table kolom pertama 
w.field("kolom2","C") #membuat table kolom kedua
 
w.record("ngek","satu") #isi untuk kolom pertama dan kedua

w.poly([[[1,3],[5,3]]]) #membuat garis dengan titik yang ada sebagai acuannya

w.close() #menutup writer
