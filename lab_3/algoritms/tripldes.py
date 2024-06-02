import os
from files_funct import read_text_from_file, read_bytes_from_file, write_bytes_to_file, write_to_txt_file
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class SymmetricKey:
    def __init__(self, key_length):
        self.key_length = key_length

    def generate_key(self):
       
        self.key = os.urandom(self.key_length)
        return self.key

    def encrypt_text(self, path_text,path_en_text, path_key):
        text=bytes(read_text_from_file(path_text),'UTF-8')
        key=read_bytes_from_file(path_key)

        padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
        padded_data = padder.update(text) + padder.finalize()

        cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
        encryptor = cipher.encryptor()
        encrypt_text = encryptor.update(padded_data) + encryptor.finalize()
        write_bytes_to_file(encrypt_text,path_en_text)
        return encrypt_text

    def decrypt_text(self, path_en_text, path_text,path_key):
        encrypt_text=read_bytes_from_file(path_en_text)
        key=read_bytes_from_file(path_key)
        cipher = Cipher(algorithms.TripleDES(key), modes.ECB())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypt_text) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        write_to_txt_file(data,path_text)
        return data
