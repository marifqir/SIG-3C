"""
Created on Mon Oct 21 11:38:04 2019
@author: bakti
"""
import shapefile #Meng-import library shapefile

w=shapefile.Writer('soal10', shapeType = 5) #Membuat file dengan nama soal10.shp 
                                        #dan mendefinisikan shapefile 5 = POLYGON
w.field("kolom1","C") #Membuat tabel dengan kolom pertama
w.field("kolom2","C") #Membuat tabel dengan kolom kedua

w.record("entah","apa") #Mengisi table pada kolom satu=entah dan kolom dua=apa
w.record("yang","merasuki") #Mengisi table pada kolom satu=yang dan kolom dua=merasuki
w.record("mu","hingga") #Mengisi table pada kolom satu=mu dan kolom dua=hingga
w.record("kau","tega") #Mengisi table pada kolom satu=kau dan kolom dua=tega
w.record("mengkhianati","ku") #Mengisi table pada kolom satu=mengkhianati dan kolom dua=ku
w.record("yang(2)","tulus") #Mengisi table pada kolom satu=yang(2) dan kolom dua=tulus
w.record("men","cinta") #Mengisi table pada kolom satu=men dan kolom dua=cinta
w.record("i-mu","GWAK") #Mengisi table pada kolom satu=i-mu dan kolom dua=GWAK
"""
membuat garis dengan menghubungkan titik titik yang dibuat 
dan memberi warna di dalam garis yg di hubungkan
"""
w.poly([[[2,3],[2,7],[1,7],[1,3],[2,3]]]) 
w.poly([[[2,3],[6,3],[6,2],[2,2],[2,3]]]) 
w.poly([[[2,7],[6,7],[6,6],[2,6],[2,7]]]) 
w.poly([[[2,-2],[2,2],[1,2],[1,-2],[2,-2]]]) 
w.poly([[[-3,3],[1,3],[1,2],[-3,2],[-3,3]]]) 
w.poly([[[6,-2],[6,2],[5,2],[5,-2],[6,-2]]]) 
w.poly([[[-3,-1],[1,-1],[1,-2],[-3,-2],[-3,-1]]]) 
w.poly([[[-2,3],[-2,7],[-3,7],[-3,3],[-2,3]]]) 

w.close() #penutup