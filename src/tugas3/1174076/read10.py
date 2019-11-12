# Mengimport modul shapefile
import shapefile

# Menjalankan function reader yang berada pada modul shapefile yang berguna untuk membuka file
sf = shapefile.Reader("read")

# Variabel yang berisi data records yang berada di dbf
isidata = sf.records()

# Menampilkan variabel isidata
print(isidata)