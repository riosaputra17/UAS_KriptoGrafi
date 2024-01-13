def otp_encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[
            i % len(key)
        ]  # Gunakan modulus untuk loop kunci jika pesan lebih panjang

        # Operasi XOR antara karakter pesan dan kunci
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)

        encrypted_message += encrypted_char
    return encrypted_message


def otp_decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_char = key[
            i % len(key)
        ]  # Gunakan modulus untuk loop kunci jika pesan lebih panjang

        # Operasi XOR antara karakter terenkripsi dan kunci
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)

        decrypted_message += decrypted_char
    return decrypted_message


print("Implementasi One Time Pad")
print("")
# Memasukkan plain text dan kunci secara manual
plain_text = input("Masukkan plain text: ")
key = input("Masukkan kunci: ")

# Enkripsi
encrypted_text = otp_encrypt(plain_text, key)
print("Pesan Terenkripsi:", encrypted_text)

# Dekripsi
decrypted_text = otp_decrypt(encrypted_text, key)
print("Pesan Terdekripsi:", decrypted_text)

# Note : plain teks dan kata kunci harus memiliki jumlah karakter yang sama
