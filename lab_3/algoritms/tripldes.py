import os
from files_funct import read_text_from_file, read_bytes_from_file, write_bytes_to_file, write_to_txt_file
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class SymmetricKey:
    def selecting_key_len(self):
        while True:
            key_len = int(input("Введите длину ключа (16, 32, 64, 128, или 192): "))
            if key_len == 16 or key_len == 32 or key_len == 64 or key_len == 128 or key_len == 192:
                break
            else:
                print("Неверный ввод. Пожалуйста, попробуйте снова.")
        return key_len

    def generate_key(self, key_len):
        key = os.urandom(16)
        return key
    
    def encrypt_text(self, path_text,path_en_text, path_key):
        text=bytes(read_text_from_file(path_text),'UTF-8')
        key=read_bytes_from_file(path_key)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(text) + padder.finalize()
        
        cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
        encryptor = cipher.encryptor()
        encrypt_text = encryptor.update(padded_data) + encryptor.finalize()
        write_bytes_to_file(path_en_text, encrypt_text)
        
    def decrypt_text(self, path_en_text, path_text,path_key):
        encrypt_text=read_bytes_from_file(path_en_text)
        key=read_bytes_from_file(path_key)
        cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypt_text) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        rez_text=data.decode('UTF-8')
        write_to_txt_file(rez_text,path_text)
        
