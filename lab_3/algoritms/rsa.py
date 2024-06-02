from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

import files_funct

class AsymmetricKey:
    def __init__(self):
        """
        Constructor for the AsymmetricKey class.
        """

    def generate_keys(self) -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Generates a pair of asymmetric keys: private and public.
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
        return (public_key, private_key)

    def encrypt_symmetric_key(self, symmetric_key_path: str, public_key_path: str, encrypt_text_path: str) -> None:
        """
        Encrypts the given symmetric key using the provided public key and saves the result to the specified path.
        """
        public_key=files_funct.deserialization_rsa_public_key(public_key_path)
        sym_key=files_funct.read_bytes_from_file(symmetric_key_path)
        c_text = public_key.encrypt(sym_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        files_funct.write_bytes_to_file(encrypt_text_path,c_text)


    def decrypt_symmetric_key(self, symmetric_key_path: str, private_key_path: str, decrypt_text_path: str) -> None:
        """
        Decrypts the given symmetric key using the provided private key and saves the result to the specified path.
        """
        priv_key=files_funct.deserialization_rsa_private_key(private_key_path)
        sym_key=files_funct.read_bytes_from_file(symmetric_key_path)
        c_text = priv_key.decrypt(sym_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        files_funct.write_bytes_to_file(decrypt_text_path,c_text)
  