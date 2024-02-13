import math

jmlHari = 485
sisaHari = jmlHari

# math.floor = membulatkan kebawah
tahun = math.floor(jmlHari/360)
# print(tahun)

# sisa hari harus int = 125 ini tu cuma untuk nentuiin ada berapa sisa hari
sisaHari %= 360

#sisa bulan
# 125 / 30 = 4.167 math.floor ngebulatin kebawah = 4

bulan = math.floor(sisaHari/30)
# print(bulan)

# sisa hari  = 5
sisaHari %= 30

# sisa minggu 

minggu = math.floor(sisaHari/7)
# print(minggu)

# sisa hari
hari = sisaHari % 7
# print(hari)

print(str(jmlHari) + ' Hari Adalah')
print('{} Tahun'. format(tahun))
print('{} Bulan'. format(bulan))
print('{} Minggu'. format(minggu))
print('{} Hari'. format(hari))