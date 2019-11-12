# Mengimport modul shapefile
import shapefile

# Menjalankan function reader yang berada pada modul shapefile yang berguna untuk membuka file
sf = shapefile.Reader("read")

# Variabel yang menampung sebuah kolom
namakolom = sf.fields

# Menampilkan variabel namakolom
print(namakolom)