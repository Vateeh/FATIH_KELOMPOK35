class ATM:
    def _init_(self, saldo_awal):
        self.saldo = saldo_awal

    def cek_saldo(self):
        return self.saldo

    def tarik_tunai(self, jumlah_tarik):
        if jumlah_tarik > self.saldo:
            print("Saldo tidak mencukupi")
        else:
            self.saldo -= jumlah_tarik
            print(f"Tarik tunai berhasil. Sisa saldo: {self.saldo}")

    def setor_tunai(self, jumlah_setor):
        self.saldo += jumlah_setor
        print(f"Setor tunai berhasil. Sisa saldo: {self.saldo}")

def main():
    saldo_awal = 1000000
    atm = ATM(saldo_awal)

    while True:
        print("\nKelompok 35")
        print("Ahmad Fatih Binasrillah")
        print("Azzam Syaiful Islam")
        print("Farrel Farros Fausto")
        print("Muhammad Noufal Khairy")
       
        print("\n=== Mesin ATM ===")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")

        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            saldo = atm.cek_saldo()
            print(f"Saldo Anda saat ini: {saldo}")
        elif pilihan == 2:
            jumlah_tarik = int(input("Masukkan jumlah tarik tunai: "))
            atm.tarik_tunai(jumlah_tarik)
        elif pilihan == 3:
            jumlah_setor = int(input("Masukkan jumlah setor tunai: "))
            atm.setor_tunai(jumlah_setor)
        elif pilihan == 4:
            print("Terima kasih telah menggunakan layanan ATM.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if _name_ == "_main_":
    main()
