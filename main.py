# Membuat kamus sandi Sungai Pramuka
kamus_sungai_pramuka = {
    'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g',
    'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l',
    'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q',
    'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v',
    'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b'
}

# Fungsi untuk mengenkripsi pesan dengan sandi Sungai Pramuka
def enkripsi_sungai_pramuka(pesan):
    pesan = pesan.lower()
    pesan_terenkripsi = ''
    for c in pesan:
        if c.isalpha():
            pesan_terenkripsi += kamus_sungai_pramuka[c]
        else:
            pesan_terenkripsi += c
    return pesan_terenkripsi

# Fungsi untuk mendekripsi pesan dengan sandi Sungai Pramuka
def dekripsi_sungai_pramuka(pesan_terenkripsi):
    pesan_terdekripsi = ''
    for c in pesan_terenkripsi:
        if c.isalpha():
            for key, value in kamus_sungai_pramuka.items():
                if value == c:
                    pesan_terdekripsi += key
        else:
            pesan_terdekripsi += c
    return pesan_terdekripsi

# Main program
pesan = input('Masukkan pesan yang ingin dienkripsi/didekripsi: ')
operasi = input('Pilih tipe operasi (E: enkripsi, D: dekripsi): ').lower()
if operasi == 'e':
    pesan_terenkripsi = enkripsi_sungai_pramuka(pesan)
    print(f'Pesan terenkripsi: {pesan_terenkripsi}')
elif operasi == 'd':
    pesan_terdekripsi = dekripsi_sungai_pramuka(pesan)
    print(f'Pesan terdekripsi: {pesan_terdekripsi}')
else:
    print('Tipe operasi tidak valid.')

