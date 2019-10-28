
# Mengimport modul shapefile
import shapefile

# Menjalankan function reader yang berada pada modul shapefile yang berguna untuk membuka file
sf = shapefile.Reader("read")

# Untuk mengetahui jenis file shp
sf.shapeType