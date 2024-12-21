# Algoritma rekursif Tabungan
def hitung_tabungan(nominal, hari, tipe):
    if tipe == "hari":
        if hari <= 0:
            return 0
        else:
            return nominal // hari  # Menggunakan pembagian integer
    elif tipe == "minggu" and hari >= 7:
        return hitung_tabungan(nominal, hari, "hari") * 7
    elif tipe == "bulan" and hari >= 30:
        return hitung_tabungan(nominal, hari, "hari") * 30
    elif tipe == "tahun" and hari >= 360:
        return hitung_tabungan(nominal, hari, "hari") * 360
    else:
        return 0

# Input dari pengguna
nominal = int(input("Masukkan nominal uang (dalam rupiah): "))
hari = int(input("Masukkan berapa hari akan menabung: "))

# Hitung tabungan
print("\nRincian Tabungan:")
print(f"Total uang yang ingin ditabung: Rp {nominal:,}")
print(f"Jumlah hari menabung: {hari} hari")

# Hitung tabungan per hari
tabungan_harian = hitung_tabungan(nominal, hari, "hari")
print(f"Tabungan per hari: Rp{tabungan_harian:,}")

# Hitung tabungan per minggu
if hari >= 7:
    tabungan_mingguan = hitung_tabungan(nominal, hari, "minggu")
    jumlah_minggu = hari // 7
    sisa_hari_minggu = hari % 7
    print(f"Tabungan per minggu: Rp{tabungan_mingguan:,} (untuk {jumlah_minggu} minggu)")
    if sisa_hari_minggu > 0:
        sisa_tabungan_mingguan = tabungan_harian * sisa_hari_minggu
        print(f"Sisa {sisa_hari_minggu} hari: Rp{sisa_tabungan_mingguan:,}")

# Hitung tabungan per bulan
if hari >= 30:
    tabungan_bulanan = hitung_tabungan(nominal, hari, "bulan")
    jumlah_bulan = hari // 30
    sisa_hari_bulanan = hari % 30
    print(f"Tabungan per bulan: Rp{tabungan_bulanan:,} (untuk {jumlah_bulan} bulan)")
    if sisa_hari_bulanan > 0:
        print(f"Sisa {sisa_hari_bulanan} hari:")
        if sisa_hari_bulanan >= 7:
            jumlah_minggu_sisa = sisa_hari_bulanan // 7
            sisa_hari_mingguan_bulanan = sisa_hari_bulanan % 7
            sisa_tabungan_mingguan = tabungan_mingguan * jumlah_minggu_sisa
            print(f"  - Rp{sisa_tabungan_mingguan:,} (untuk {jumlah_minggu_sisa} minggu)")
            if sisa_hari_mingguan_bulanan > 0:
                sisa_tabungan_harian = tabungan_harian * sisa_hari_mingguan_bulanan
                print(f"  - Rp{sisa_tabungan_harian:,} (untuk {sisa_hari_mingguan_bulanan} hari)")
        else:
            sisa_tabungan_harian = tabungan_harian * sisa_hari_bulanan
            print(f"  - Rp{sisa_tabungan_harian:,} (untuk {sisa_hari_bulanan} hari)")

# Hitung tabungan per tahun
if hari >= 360:
    tabungan_tahunan = hitung_tabungan(nominal, hari, "tahun")
    jumlah_tahun = hari // 360
    sisa_hari_tahunan = hari % 360
    print(f"Tabungan per tahun: Rp{tabungan_tahunan:,} (untuk {jumlah_tahun} tahun)")
    if sisa_hari_tahunan > 0:
        print(f"Sisa {sisa_hari_tahunan} hari:")
        if sisa_hari_tahunan >= 30:
            jumlah_bulan_sisa = sisa_hari_tahunan // 30
            sisa_hari_bulanan_tahunan = sisa_hari_tahunan % 30
            sisa_tabungan_bulanan = tabungan_bulanan * jumlah_bulan_sisa
            print(f"  - Rp{sisa_tabungan_bulanan:,} (untuk {jumlah_bulan_sisa} bulan)")
            if sisa_hari_bulanan_tahunan >= 7:
                jumlah_minggu_sisa = sisa_hari_bulanan_tahunan // 7
                sisa_hari_mingguan_tahunan = sisa_hari_bulanan_tahunan % 7
                sisa_tabungan_mingguan = tabungan_mingguan * jumlah_minggu_sisa
                print(f"  - Rp{sisa_tabungan_mingguan:,} (untuk {jumlah_minggu_sisa} minggu)")
                if sisa_hari_mingguan_tahunan > 0:
                    sisa_tabungan_harian = tabungan_harian * sisa_hari_mingguan_tahunan
                    print(f"  - Rp{sisa_tabungan_harian:,} (untuk {sisa_hari_mingguan_tahunan} hari)")
            elif sisa_hari_bulanan_tahunan > 0:
                sisa_tabungan_harian = tabungan_harian * sisa_hari_bulanan_tahunan
                print(f"  - Rp{sisa_tabungan_harian:,} (untuk {sisa_hari_bulanan_tahunan} hari)")
        else:
            sisa_tabungan_harian = tabungan_harian * sisa_hari_tahunan
            print(f"  - Rp{sisa_tabungan_harian:,} (untuk {sisa_hari_tahunan} hari)")
