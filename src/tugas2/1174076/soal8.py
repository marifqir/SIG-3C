# Mengimport modul shapefile
import shapefile

# Inisiasikan variabel w, untuk membuat file shapefile baru
w = shapefile.Writer("soal8")

# Mengecek set variabel w, apakah point, line atau polygon, Kalau koosong berarti tidak di set
w.shapeType=5

# Membuat field tabel atau file dengan format .dbf, C = Tipe data Character
w.field("kolom1","C")
w.field("kolom2","C")

# Membuat row tabel atau isi tabel
w.record("ngek","satu")

# Membuat sejumlah titik, lalu dihubungkan dengan garis, dan kembali ke titik awal
w.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]])

# Menutup function writer
w.close()
