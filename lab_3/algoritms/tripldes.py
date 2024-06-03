import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from files_funct import (
    read_text_from_file,
    read_bytes_from_file,
    write_bytes_to_file,
    write_to_txt_file,
    deserial_sym_key
)


class SymmetricKey:
    def selecting_key_len(self):
        while True:
            key_len = int(input("Введите длину ключа ( 64, 128, или 192): "))
            if key_len == 64 or key_len == 128 or key_len == 192:
                break
            else:
                print("Неверный ввод. Пожалуйста, попробуйте снова.")
        return key_len

    def generate_key(self, key_len):
        key = os.urandom(key_len//8)
        return key

    def encrypt_text(self, path_text, path_en_text, path_key):
        text = bytes(read_text_from_file(path_text),"UTF-8")
        key = deserial_sym_key(path_key)

        padder = padding.PKCS7(64).padder()
        padded_data = padder.update(text) + padder.finalize()
        iv = os.urandom(8)
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encrypt_text = iv + encryptor.update(padded_data) + encryptor.finalize()
        write_bytes_to_file(path_en_text, encrypt_text)

    def decrypt_text(self, path_en_text, path_dec_text, path_key):
        encrypt_text = read_bytes_from_file(path_en_text)
        key = deserial_sym_key(path_key) 
        iv = encrypt_text[:8]
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(encrypt_text[8:]) + decryptor.finalize()


        unpadder = padding.PKCS7(64).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        write_to_txt_file(unpadded_dc_text.decode("UTF-8"), path_dec_text)
