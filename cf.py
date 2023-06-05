# Mendefinisikan daftar penyakit dan gejalanya
penyakit = [
    {"code": "P01", "name": "A", "Gejala": ["G01", "G03"]},
    {"code": "P02", "name": "B", "Gejala": ["G02", "G03", "G06"]},
    {"code": "P03", "name": "C", "Gejala": ["G02", "G04", "G01", "G05"]},
    {"code": "P04", "name": "D", "Gejala": ["G06", "G05"]}
]

# Mendefinisikan daftar gejala dan nilai ahlinya
gejala = [
    {"code": "G01", "name": "Pusing",        "value": 0.8},
    {"code": "G02", "name": "Keringat Dingin", "value": 0.6},
    {"code": "G03", "name": "Menggigil",     "value": 0.5},
    {"code": "G04", "name": "Dehidrasi",     "value": 0.2},
    {"code": "G05", "name": "Batuk",         "value": 0.5},
    {"code": "G06",    "name": "Nyeri Tenggorokan", "value": 0.5}
]

# Mendefinisikan gejala pasien dan nilai-nilainya
pasien = [
    {"code": "G01", "name": "Pusing",        "value": 0.5},
    {"code": "G05", "name": "Batuk",         "value": 0.8},
    {"code": "G04", "name": "Dehidrasi",     "value": 0.4},
    {"code": "G02", "name": "Keringat Dingin", "value": 0.3},
    {"code": "G03", "name": "Menggigil",     "value": 0.2}
]

# Mendefinisikan fungsi untuk menghitung faktor kepastian suatu penyakit berdasarkan gejala pasien


def certainty_factor(penyakit, pasien):
    # Menginisialisasi faktor kepastian menjadi nol
    cf = 0
    # Melakukan perulangan melalui gejala penyakit
    for gejala_penyakit in penyakit["Gejala"]:
        # Mencari gejala yang sesuai dalam daftar gejala pasien
        for p in pasien:
            # Jika kode gejala sesuai
            if p["code"] == gejala_penyakit:
                # Mencari gejala yang sesuai dalam daftar ahli
                for g in gejala:
                    # Jika kode gejala sesuai
                    if g["code"] == gejala_penyakit:
                        # Menghitung hasil perkalian nilai gejala pasien dengan nilai ahli
                        produk = p["value"] * g["value"]
                        # Memperbarui faktor kepastian menggunakan rumus: fk = fk + produk * (1 - abs(fk))
                        cf = cf + produk * (1 - abs(cf))
                        # Keluar dari perulangan dalam
                        break
        # Tidak keluar dari perulangan luar
        # Melanjutkan perhitungan untuk semua gejala
    # Mengembalikan faktor kepastian
    return cf


# Melakukan perulangan melalui daftar penyakit dan mencetak nama penyakit beserta faktor kepastiannya
for penyakit in penyakit:
    print(penyakit["name"], str(certainty_factor(penyakit, pasien)*100) + '%')
