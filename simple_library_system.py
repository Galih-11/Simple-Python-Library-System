class manusia:
    def __init__(self, nama, no_hp, jekel):
        self.nama = nama
        self.no_hp = no_hp
        self.jekel = jekel

    def get_info(self):
        pass

class mahasiswa(manusia):
    def __init__(self, nama, no_hp, jekel, npm, fakultas, prodi):
        super().__init__(nama, no_hp, jekel)
        self.__npm = npm
        self.__fakultas = fakultas
        self.__prodi = prodi
        self.buku_dipinjam = []  

    def get_info(self):
        print("=== Data Mahasiswa ===")
        return (
            f"\nNama: {self.nama}"
            f"\nNo HP: {self.no_hp}"
            f"\nJenis Kelamin: {self.jekel}"
            f"\nNPM: {self.__npm}"
            f"\nFakultas: {self.__fakultas}"
            f"\nProdi: {self.__prodi}"
        )

    def tampilkan_data(self):
        print(self.get_info())

    def tampilkan_koleksi(self):
        print("=== Koleksi Buku Yang Ada Disini ===")
        print(self.rak_buku)

    def pinjam_buku(self, admin, buku):
        if buku in admin.rak_buku:
            admin.rak_buku.remove(buku)
            self.buku_dipinjam.append(buku)
            print(f"Buku '{buku}' berhasil dipinjam!")
        else:
            print("Maaf, buku tidak tersedia!")

    def kembalikan_buku(self, admin, buku):
        if buku in self.buku_dipinjam:
            self.buku_dipinjam.remove(buku)
            admin.rak_buku.append(buku)
            print(f"Buku '{buku}' berhasil dikembalikan!")
        else:
            print("Buku tidak ditemukan di tas!")

class admin(manusia):
    def __init__(self, nama, no_hp, jekel, nik, alamat, rak_buku):
        super().__init__(nama, no_hp, jekel)
        self.__nik = nik
        self.__alamat = alamat
        self.rak_buku = rak_buku
        self.buku = []

    def get_info(self):
        print("=== Data Admin ===")
        return (
            f"\nNama: {self.nama}"
            f"\nNo HP: {self.no_hp}"
            f"\nJenis Kelamin: {self.jekel}"
            f"\nNIK: {self.__nik}"
            f"\nAlamat: {self.__alamat}"
        )

    def tampilkan_data(self):
        print(self.get_info())

    def tambah_buku(self, buku):
        buku = input("Masukan buku baru: ")
        self.rak_buku.append(buku)
        print(f"Buku '{buku}' berhasil ditambahkan!")

    def tampilkan_koleksi(self):
        print("=== Koleksi Buku Yang Ada Disini ===")
        print(self.rak_buku)

    def update_buku(self):
        print(f"Koleksi Buku Di Rak Buku {self.rak_buku}")
        buku_lama = input("Masukkan nama buku lama: ")
        buku_baru = input("Masukkan nama buku baru: ")
        if buku_lama in self.rak_buku:
            Buklam = self.rak_buku.index(buku_lama)
            self.rak_buku[Buklam] = buku_baru
            print(f"Buku '{buku_lama}' berhasil diganti menjadi '{buku_baru}'!")
        else:
            print("Buku lama tidak ditemukan!")

    def delete_buku(self, buku):
        if buku in self.rak_buku:
            self.rak_buku.remove(buku)
            print(f"Buku '{buku}' berhasil dihapus!")
        else:
            print("Buku tidak ditemukan!")

mhs = mahasiswa("Mahasiswa", "0101010101", "Laki-Laki", "010101001", "Sains dan Teknologi", "Informatika Medis")
adm = admin("Admin Perpus", "01010101", "Laki-Laki", "01010101", "Jl. Perpustakaan No. 1",
            ["Pemrograman Python", "Struktur Data", "Algoritma"])

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Mahasiswa")
    print("2. Admin")
    print("3. Keluar")

    pilihan = input("Masukan Pilihan Menu anda: ")

    if pilihan == "1":
        while True:
            print("\n=== Menu Mahasiswa ===")
            print("1. Tampilkan Data Mahasiswa")
            print("2. Tampilkan Koleksi Buku")
            print("3. Pinjam Buku")
            print("4. Kembalikan Buku")
            print("5. Lihat Tas")
            print("6. Kembali Ke Menu")

            pm = input("Masukan Pilihan Anda: ")

            if pm == "1":
                mhs.tampilkan_data()
            elif pm == "2":
                adm.tampilkan_koleksi()
            elif pm == "3":
                buku = input("Masukan nama buku: ")
                mhs.pinjam_buku(adm, buku)
            elif pm == "4":
                buku = input("Masukan buku yg akan dikembalikan: ")
                mhs.kembalikan_buku(adm, buku)
            elif pm == "5":
                print("Tas:", mhs.buku_dipinjam)
            elif pm == "6":
                break

    elif pilihan == "2":
        while True:
            print("\n=== Menu Admin ===")
            print("1. Tampilkan Data Admin")
            print("2. Tambah Buku")
            print("3. Tampilkan Koleksi Buku")
            print("4. Update Buku")
            print("5. Hapus Buku")
            print("6. Lihat Rak Buku")
            print("7. Kembali Ke Menu Utama")

            pa = input("Masukan Pilihan Anda: ")

            if pa == "1":
                adm.tampilkan_data()
            elif pa == "2":
                adm.tambah_buku(buku)
            elif pa == "3":
                adm.tampilkan_koleksi()
            elif pa == "4":
                adm.update_buku()
            elif pa == "5":
                buku = input("Masukan buku yg dihapus: ")
                adm.delete_buku(buku)
            elif pa == "6":
                print("Rak Buku:", adm.rak_buku)
            elif pa == "7":
                break

    elif pilihan == "3":
        print("Terimakasih Sudah Menggunakan Program Ini")
        break