# Fungsi untuk konversi jumlah hari menjadi tahun, bulan, dan sisa hari
def konversi_hari(jumlah_hari):
    # jumlah tahun
    tahun = jumlah_hari // 365
    
    # sisa hari setelah menghitung tahun
    sisa_hari = jumlah_hari % 365
    
    # jumlah bulan
    bulan = sisa_hari // 30
    
    # sisa hari setelah menghitung bulan
    sisa_hari %= 30
    
    return tahun, bulan, sisa_hari

# Jumlah hari 
jumlah_hari_input = 485

# Panggil fungsi konversi_hari
tahun, bulan, sisa_hari = konversi_hari(jumlah_hari_input)

# Tampilkan hasil
print(f"{jumlah_hari_input} hari setara dengan:")
print(f"Tahun: {tahun} tahun")
print(f"Bulan: {bulan} bulan")
print(f"Sisa Hari: {sisa_hari} hari")
