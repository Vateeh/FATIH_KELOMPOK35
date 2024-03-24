import math

# Function untuk menghitung luas lingkaran
def hitung_luas(r):
    return math.pi * r**2

# Function untuk menghitung keliling lingkaran
def hitung_keliling(r):
    return 2 * math.pi * r

# Method untuk mencetak hasil perhitungan luas dan keliling lingkaran
class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def cetak_luas(self):
        print("Luas lingkaran dengan jari-jari {} adalah {:.2f}".format(self.jari_jari, hitung_luas(self.jari_jari)))

    def cetak_keliling(self):
        print("Keliling lingkaran dengan jari-jari {} adalah {:.2f}".format(self.jari_jari, hitung_keliling(self.jari_jari)))

# Contoh penggunaan
def main():
    jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
    lingkaran_saya = Lingkaran(jari_jari)
    lingkaran_saya.cetak_luas()
    lingkaran_saya.cetak_keliling()

if __name__ == "__main__":
    main()
