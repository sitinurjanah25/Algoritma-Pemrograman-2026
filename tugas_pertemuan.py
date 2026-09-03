import math

def rasionalisasi_akar():
    print("=" * 60)
    print("PROGRAM RASIONALISASI PENYEBUT PECAHAN BENTUK AKAR")
    print("=" * 60)
    
    try:
        c = float(input("Masukkan pembilang (c): "))
        a = float(input("Masukkan koefisien penyebut (a): "))
        b = float(input("Masukkan nilai di dalam akar (b): "))
        
        print("\nPilih bentuk penyebut:")
        print("1. Tambah (+), bentuk c / (a + √b)")
        print("2. Kurang (-), bentuk c / (a - √b)")
        pilihan = int(input("Pilihan Anda (1 atau 2): "))
    except ValueError:
        print("\n[Error] Masukkan harus berupa angka yang valid!")
        return

    # Validasi nilai akar
    if b < 0:
        print("\n[Error] Nilai b di dalam akar tidak boleh negatif!")
        return

    penyebut_baru = (a ** 2) - b
    if penyebut_baru == 0:
        print("\n[Error] Penyebut bernilai 0. Pecahan tidak terdefinisi!")
        return

    k1 = c * a
    k2 = c

    print("\n--- Hasil Perhitungan ---")
    if pilihan == 1:
        print("Bentuk Asli:")
        print(f"  {c}")
        print("  " + "-" * 10)
        print(f"  {a} + √{b}\n")
        
        print("Hasil Rasionalisasi Aljabar:")
        print(f"  {k1} - {k2}√{b}")
        print("  " + "-" * 15)
        print(f"  {penyebut_baru}\n")
        
        nilai_desimal = c / (a + math.sqrt(b))
        
    elif pilihan == 2:
        print("Bentuk Asli:")
        print(f"  {c}")
        print("  " + "-" * 10)
        print(f"  {a} - √{b}\n")
        
        print("Hasil Rasionalisasi Aljabar:")
        print(f"  {k1} + {k2}√{b}")
        print("  " + "-" * 15)
        print(f"  {penyebut_baru}\n")
        
        nilai_desimal = c / (a - math.sqrt(b))
        
    else:
        print("\n[Error] Pilihan tanda hanya 1 atau 2!")
        return

    print(f"Nilai Desimal Akhir = {nilai_desimal:.4f}")

# DUA BARIS INI WAJIB ADA AGAR PROGRAM BISA JALAN
if __name__ == "__main__":
    rasionalisasi_akar()