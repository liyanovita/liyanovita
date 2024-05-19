import numpy as np
import pandas as pd

# Inisialisasi data
kriteria = ['Luas Tanah', 'Harga', 'Tipe', 'Sumber Air', 'Kamar Tidur', 'Kamar Mandi', 'Pos Satpam', 'Lokasi']
bobot = [0.2904, 0.2133, 0.1708, 0.0441, 0.1399, 0.0293, 0.0624, 0.0498]

matriks = [
    [7, 7, 9, 7, 1, 9, 1, 6],
    [4, 3, 5, 3, 3, 10, 7, 4],
    [5, 5, 7, 4, 9, 2, 6, 1],
    [9, 5, 10, 9, 7, 8, 6, 7],
    [10, 1, 9, 2, 10, 6, 10, 2],
    [6, 7, 2, 7, 10, 2, 8, 7],
    [10, 9, 10, 2, 6, 7, 10, 4],
    [7, 6, 6, 4, 7, 2, 3, 9],
    [4, 9, 9, 1, 6, 1, 6, 1],
    [9, 8, 2, 4, 5, 3, 2, 5],
    [4, 4, 2, 5, 4, 10, 6, 5],
    [10, 6, 9, 9, 10, 10, 2, 6],
    [6, 8, 8, 5, 4, 9, 2, 3],
    [8, 6, 3, 3, 6, 7, 8, 7],
    [4, 9, 3, 5, 10, 5, 10, 6],
    [6, 2, 7, 6, 5, 6, 5, 9],
    [8, 4, 1, 8, 3, 10, 7, 4],
    [4, 1, 8, 5, 10, 5, 2, 6],
    [9, 8, 9, 5, 1, 3, 10, 6],
    [3, 1, 10, 4, 7, 5, 10, 8]
]

# Ubah daftar menjadi array numpy
matriks = np.array(matriks)
bobot = np.array(bobot)

# Langkah 1: Hitung solusi rata-rata (AV)
def calculate_av(matriks):
    return np.mean(matriks, axis=0)

# Langkah 2: Hitung jarak positif (PDA) dan negatif (NDA) dari rata-rata
def calculate_pda_nda(matriks, AV, kriteria):
    PDA = np.zeros_like(matriks, dtype=float)
    NDA = np.zeros_like(matriks, dtype=float)

    for j in range(matriks.shape[1]):
        if kriteria[j] == 'Harga':  # Assuming 'Harga' is the only cost criterion
            PDA[:, j] = np.maximum(0, (AV[j] - matriks[:, j]) / AV[j])
            NDA[:, j] = np.maximum(0, (matriks[:, j] - AV[j]) / AV[j])
        else:  # benefit criteria
            PDA[:, j] = np.maximum(0, (matriks[:, j] - AV[j]) / AV[j])
            NDA[:, j] = np.maximum(0, (AV[j] - matriks[:, j]) / AV[j])
    return PDA, NDA

# Langkah 3: Hitung jumlah tertimbang PDA dan NDA (SP, SN)
def calculate_sp_sn(PDA, NDA, bobot):
    SP = np.sum(PDA * bobot, axis=1)
    SN = np.sum(NDA * bobot, axis=1)
    return SP, SN

# Langkah 4: Normalisasikan nilai SP dan SN (NSP, NSN)
def normalize_sp_sn(SP, SN):
    NSP = SP / np.max(SP)
    NSN = 1 - (SN / np.max(SN))
    return NSP, NSN

# Langkah 5: Hitung skor penilaian (AS)
def calculate_as(NSP, NSN):
    return 0.5 * (NSP + NSN)

# Langkah 6: Perangkingan
def ranking(AS):
    return np.argsort(-AS)

# Main menu
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Menentukan solusi rata-rata average solution (AV)")
        print("2. Menentukan jarak positif / negatif dari rata-rata (PDA / NDA)")
        print("3. Menentukan jumlah terbobot dari PDA / NDA (SP / SN)")
        print("4. Normalisasi nilai SP / SN (NSP / NSN)")
        print("5. Menghitung nilai skor penilaian (AS)")
        print("6. Perangkingan")
        print("7. Keluar")

        choice = int(input("Pilih opsi (1-7): "))

        if choice == 1:
            AV = calculate_av(matriks)
            print("\nSolusi rata-rata (AV):")
            print(AV)

        elif choice == 2:
            AV = calculate_av(matriks)
            PDA, NDA = calculate_pda_nda(matriks, AV, kriteria)
            print("\nJarak positif dari rata-rata (PDA):")
            print(PDA)
            print("\nJarak negatif dari rata-rata (NDA):")
            print(NDA)

        elif choice == 3:
            AV = calculate_av(matriks)
            PDA, NDA = calculate_pda_nda(matriks, AV, kriteria)
            SP, SN = calculate_sp_sn(PDA, NDA, bobot)
            print("\nJumlah terbobot dari PDA (SP):")
            print(SP)
            print("\nJumlah terbobot dari NDA (SN):")
            print(SN)

        elif choice == 4:
            AV = calculate_av(matriks)
            PDA, NDA = calculate_pda_nda(matriks, AV, kriteria)
            SP, SN = calculate_sp_sn(PDA, NDA, bobot)
            NSP, NSN = normalize_sp_sn(SP, SN)
            print("\nNormalisasi nilai SP (NSP):")
            print(NSP)
            print("\nNormalisasi nilai SN (NSN):")
            print(NSN)

        elif choice == 5:
            AV = calculate_av(matriks)
            PDA, NDA = calculate_pda_nda(matriks, AV, kriteria)
            SP, SN = calculate_sp_sn(PDA, NDA, bobot)
            NSP, NSN = normalize_sp_sn(SP, SN)
            AS = calculate_as(NSP, NSN)
            print("\nNilai skor penilaian (AS):")
            print(AS)

        elif choice == 6:
            AV = calculate_av(matriks)
            PDA, NDA = calculate_pda_nda(matriks, AV, kriteria)
            SP, SN = calculate_sp_sn(PDA, NDA, bobot)
            NSP, NSN = normalize_sp_sn(SP, SN)
            AS = calculate_as(NSP, NSN)
            ranking_result = ranking(AS)
            print("\nPerangkingan:")
            for idx, rank in enumerate(ranking_result):
                print(f"Alternatif {rank + 1}: {AS[rank]}")

        elif choice == 7:
            print("Keluar.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
