import shapefile as shp #import library shapfile sebagai shp
w=shp.Writer('soal5',shapeType=3) #membuat file bernama soal5 yang berisi gambar polyline sesuai dengan shaptype 3 yaitu polyline
 
w.field("kolom1","C") #membuat table kolom pertama 
w.field("kolom2","C") #membuat table kolom kedua
 
w.record("ngek","satu") #isi untuk kolom pertama dan kedua

w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat garis dengan titik yang ada sebagai acuannya

w.close() #menutup writer
