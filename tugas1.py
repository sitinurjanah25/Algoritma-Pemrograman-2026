import math

def rasionalkan_akar():
    print("=" * 45)
    print("  PROGRAM MERASIONALKAN BENTUK AKAR (a / √b)")
    print("=" * 45)

    try:
        a = float(input("Masukkan nilai pembilang (a): "))
        b = float(input("Masukkan nilai penyebut dalam akar (b): "))
    except ValueError:
        print("\n[Error] Input harus berupa angka!")
        return

    if b <= 0:
        print("\n[Error] Nilai di dalam akar (b) harus lebih besar dari 0!")
    else:
        # Perhitungan rasionalisasi: (a / √b) = (a√b) / b
        koefisien = a / b
        
        print("\n--- Hasil Rasionalisasi ---")
        print(f"Bentuk Sederhana : ({a}√{b}) / {b}")
        print(f"Bentuk Desimal   : {koefisien:.2f}√{b}")

if __name__ == "__main__":
    rasionalkan_akar()