import math

# Jam Berapa A & B bertabrakan
# Jarak A & B = 120km
# A Berjalan 60km/h dari Timur
# B Berjalan 40km/h dari Barat
# A & B Start Pukul 9 WIB

jamAwal = 9
jarakKM = 120
kecepatanTotalKMperJam = 100
kecepatanTotalKMperDetik = kecepatanTotalKMperJam/3600

DetikTotal = jarakKM / kecepatanTotalKMperDetik
lamaJam = math.floor(DetikTotal / 3600)
lamaMenit = math.floor((DetikTotal%3600)/60)
lamaDetik = math.floor((DetikTotal%3600)%60)

print('Lama Waktu' + str(lamaJam) + 'jam, ' + str(lamaMenit) + 'Menit, ' + str(lamaDetik) + 'Detik')
print('Tabrak Pukul {}:{}:{}'.format(jamAwal + lamaJam,lamaMenit,lamaDetik))
