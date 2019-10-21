# Mengimport modul shapefile
import shapefile

# Inisiasikan variabel w, untuk membuat file shapefile baru
w = shapefile.Writer("soal6")

# Mengecek set variabel w, apakah point, line atau polygon, Kalau koosong berarti tidak di set
w.shapeType=5

# Membuat field tabel atau file dengan format .dbf, C = Tipe data Character
w.field("kolom1","C")
w.field("kolom2","C")

# Membuat row tabel atau isi tabel
w.record("ngek","satu")

# Membuat dua buah titik, lalu dihubungkan dengan sebuah garis (POLYLINE)
w.poly([[[1,3],[5,3]]])
