# Mengimport modul shapefile
import shapefile

# Inisiasikan variabel w, untuk membuat file shapefile baru
w = shapefile.Writer("soal9")

# Mengecek set variabel w, apakah point, line atau polygon, Kalau koosong berarti tidak di set
w.shapeType=5

# Membuat field tabel atau file dengan format .dbf, C = Tipe data Character
w.field("kolom1","C")
w.field("kolom2","C")

# Membuat row tabel atau isi tabel
w.record("ngek","satu")
w.record("ngok","dua")

# Membuat sebuah persegi panjang
w.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]])

# Membuat sebuah persegi 
w.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]])

# Menutup function writer
w.close()
