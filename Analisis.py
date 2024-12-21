import time
import matplotlib.pyplot as plt

def hitung_tabungan_iteratif(nominal, hari):
    """Menghitung tabungan secara iteratif."""
    if nominal <= 0 or hari <= 0:
        return 0
    return nominal // hari

def hitung_tabungan_rekursif(nominal, hari):
    """Menghitung tabungan secara rekursif."""
    if hari <= 0:
        return 0
    return nominal // hari

def ukur_waktu_iteratif(nominal, hari):
    start_time = time.time()
    hitung_tabungan_iteratif(nominal, hari)
    end_time = time.time()
    return end_time - start_time

def ukur_waktu_rekursif(nominal, hari):
    start_time = time.time()
    hitung_tabungan_rekursif(nominal, hari)
    end_time = time.time()
    return end_time - start_time

def analisis_performa():
    ukuran_masukan = [1, 10, 100, 1000, 10000]
    waktu_iteratif = []
    waktu_rekursif = []

    nominal = 1000000  # Contoh nominal tetap untuk semua uji coba

    for hari in ukuran_masukan:
        waktu_iteratif.append(ukur_waktu_iteratif(nominal, hari))
        waktu_rekursif.append(ukur_waktu_rekursif(nominal, hari))

    # Menampilkan hasil dalam bentuk grafik
    plt.plot(ukuran_masukan, waktu_iteratif, label="Iteratif", marker='o')
    plt.plot(ukuran_masukan, waktu_rekursif, label="Rekursif", marker='o')
    plt.xlabel("Input (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison: Recursive vs Iterative")
    plt.legend()
    plt.grid()
    plt.show()

    # Menampilkan hasil dalam tabel
    print("+------------------+--------------------+--------------------+")
    print("| Input (n)       | Iterative Time (s) | Recursive Time (s) |")
    print("+------------------+--------------------+--------------------+")
    for i in range(len(ukuran_masukan)):
        print(f"| {ukuran_masukan[i]:<16} | {waktu_iteratif[i]:<18.6e} | {waktu_rekursif[i]:<18.6e} |")
    print("+------------------+--------------------+--------------------+")

# Menjalankan analisis performa
analisis_performa()
