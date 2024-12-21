# Algoritma iteratif Tabungan
def hitung_tabungan(nominal, hari):
    """Menghitung dan menampilkan rincian tabungan."""

    if nominal <= 0 or hari <= 0:
        print("Nominal uang dan jumlah hari harus positif.")
        return

    print("\nRincian Tabungan:")
    print(f"Total uang yang ingin ditabung: Rp {nominal:,}")
    print(f"Jumlah hari menabung: {hari} hari")

    per_hari = nominal // hari
    print(f"Tabungan per hari: Rp{per_hari:,}")

    # Hitung tabungan per minggu dan sisa hari
    if hari >= 7:
        jumlah_minggu = hari // 7
        sisa_hari_minggu = hari % 7
        per_minggu = per_hari * 7
        print(f"Tabungan per minggu: Rp{per_minggu:,} (untuk {jumlah_minggu} minggu)")
        if sisa_hari_minggu > 0:
            sisa_per_hari_minggu = per_hari * sisa_hari_minggu
            print(f"Sisa {sisa_hari_minggu} hari: Rp{sisa_per_hari_minggu:,}")

    # Hitung tabungan per bulan (asumsi 30 hari per bulan) dan sisa hari
    if hari >= 30:
        jumlah_bulan = hari // 30
        sisa_hari_bulan = hari % 30
        per_bulan = per_hari * 30
        print(f"Tabungan per bulan: Rp{per_bulan:,} (untuk {jumlah_bulan} bulan)")
        if sisa_hari_bulan > 0:
            sisa_per_minggu_bulan = (sisa_hari_bulan // 7) * per_minggu
            sisa_per_hari_bulan = (sisa_hari_bulan % 7) * per_hari
            print(f"Sisa {sisa_hari_bulan} hari:")
            if sisa_hari_bulan >= 7:
                print(f"  - Rp{sisa_per_minggu_bulan:,} (untuk {sisa_hari_bulan // 7} minggu)")
            if sisa_hari_bulan % 7 > 0:
                print(f"  - Rp{sisa_per_hari_bulan:,} (untuk {sisa_hari_bulan % 7} hari)")

    # Hitung tabungan per tahun (asumsi 360 hari per tahun) dan sisa hari
    if hari >= 360:
        jumlah_tahun = hari // 360
        sisa_hari_tahun = hari % 360
        per_tahun = per_hari * 360
        print(f"Tabungan per tahun: Rp{per_tahun:,} (untuk {jumlah_tahun} tahun)")

        # Hitung sisa hari dalam konteks bulan, minggu, dan hari
        if sisa_hari_tahun > 0:
            sisa_bulan_tahun = (sisa_hari_tahun // 30) * per_bulan
            sisa_minggu_tahun = ((sisa_hari_tahun % 30) // 7) * per_minggu
            sisa_hari_akhir_tahun = (sisa_hari_tahun % 30) % 7 * per_hari

            print(f"Sisa {sisa_hari_tahun} hari:")
            if sisa_hari_tahun >= 30:
                print(f"  - Rp{sisa_bulan_tahun:,} (untuk {sisa_hari_tahun // 30} bulan)")
            if (sisa_hari_tahun % 30) >= 7:
                print(f"  - Rp{sisa_minggu_tahun:,} (untuk {(sisa_hari_tahun % 30) // 7} minggu)")
            if (sisa_hari_tahun % 30) % 7 > 0:
                print(f"  - Rp{sisa_hari_akhir_tahun:,} (untuk {(sisa_hari_tahun % 30) % 7} hari)")

# Input dari pengguna
nominal = int(input("Masukkan nominal uang (dalam rupiah): "))
hari = int(input("Masukkan berapa hari akan menabung: "))

# Panggil fungsi untuk menghitung tabungan
hitung_tabungan(nominal, hari)
