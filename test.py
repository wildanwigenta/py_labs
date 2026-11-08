print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2026 - int(tahun_lahir)

print(f"Selamat datang {nama} dalam program Python, per 2026 umur Anda adalah {umur} tahun.\n")
print("Terima kasih telah menggunakan program Python!")

#function
def minimal(a, b):
    if a <= b:
        return a
    return b
test1 = minimal(10, 20)
print(f"Nilai minimal dari 10 dan 20 adalah {test1}.\n")