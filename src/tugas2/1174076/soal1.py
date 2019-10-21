# Mengimport modul shapefile
import shapefile

# Inisiasikan variabel w, untuk membuat file shapefile baru
w = shapefile.Writer('soal1', shapeType=1)

# Mengecek set variabel w, apakah point, line atau polygon, Kalau koosong berarti tidak di set
w.shapeType

# Membuat field tabel atau file dengan format .dbf, C = Tipe data Character
w.field("kolom1","C")
w.field("kolom2","C")

# Membuat row tabel atau isi tabel
w.record("ngek","satu")
w.record("ngok","dua")

# Mengisi file berformat .shp dengan point(titik), dengan koordinat x, y
w.point(1,1)
w.point(2,2)

# Untuk menutup writer
w.close()
