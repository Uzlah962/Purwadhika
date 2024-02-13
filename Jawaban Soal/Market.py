# Masukan Jumal Apel : 2
# Masukan Jumlah Jeruk : 3
# Masukan Jumlah Anggur : 5
# Detail Belanja 
# Apel : 2 x 10000 = 20000
# Jeruk : 3 x 15000 = 45000
# Jeruk : 5 x 20000 = 100000
# Total : 165000

#input jumlah smwnya
jumlahApel = int(input('Masukan Jumlah Apel : '))
jumlahJeruk = int(input('Masukan Jumlah Jeruk : '))
jumlahAnggur = int(input('Masukan Jumlah Anggur : '))

hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

totalHargaApel = jumlahApel * hargaApel
totalHargaJeruk = jumlahJeruk * hargaJeruk
totalHargaAnggur = jumlahAnggur * hargaAnggur
print('''
Detail Belanja
      
Apel : {jmlApel} x {hrgApel} = {totalhrgApel} 
Jeruk : {jmlJeruk} x {hrgJeruk} = {totalhrgJeruk}   
Anggur : {jmlAnggur} x {hrgAnggur} = {totalhrgAnggur}
      
Total : {totalHarga}
'''.format(jmlApel=jumlahApel, hrgApel=hargaApel, totalHrgApel=totalHargaApel, 
    jmlJeruk=jumlahJeruk, hrgJeruk=hargaJeruk, totalHrgJeruk=totalHargaJeruk,
    jmlAnggur=jumlahAnggur, hrgAnggur=hargaAnggur, totalHrgAnggur=totalHargaAnggur,
    totalHarga=(totalHargaAnggur+totalHargaApel+totalHargaJeruk)))


