import json

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key



def read_text_from_file(file_path: str) -> str:
    """
    This function reads the file format .txt

    Arguments:
        file_path: location the .txt file whose contents you want to find out
    Returns:
        text: content .txt file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


def write_to_txt_file(text: str, file_name: str) -> None:
    """
    This function writes data to a .txt file

    Arguments:
        text: the data that we write to the file
        file_name: location the .txt file in which we write the data
    """
    try:
        with open(file_name + ".txt", "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Текст успешно записан в файл {file_name}.txt")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


def read_json_file(file_name: str) -> dict[str, str]:
    """
    This function reads the file format .json

    Arguments:
        file_name: location the .json file whose contents you want to find out
    Returns:
        data: dictionary of keys
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return None


def read_bytes_from_file(file_path: str) -> bytes:
    """
    This function reads the file with bytes

    Arguments:
        file_path: location the file whose contents you want to find out
    Returns:
        num_bytes: content file
    """
    try:
        with open(file_path, 'rb') as file:  
            return file.read()
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return None


def write_bytes_to_file(file_path: str, data: bytes) -> None:
    """
    This function writes bytes to file

    Arguments:
        file_path: the bytes that we write to the file
        data: location the file in which we write bytes
    """
    try:
        with open(file_path, 'wb') as file: 
            file.write(data)
        print(f"Успешно записано в файл {data}.txt")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


def read_rsa_public_key(filename: str) -> rsa.RSAPublicKey:
    """
    
    """
    try:
        with open(filename, 'rb') as pem_in:
            public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)
            return d_public_key
    except Exception as e:
        print(f"Произошла ошибка при чтении: {e}")

def write_rsa_public_key(filename: str, key: rsa.RSAPublicKey) -> None:
    """
    
    """
    try:
        with open(filename, 'wb') as public_out:
            public_out.write(key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))

    except Exception as e:
        print(f"Произошла ошибка: {e}")


def read_rsa_private_key(filename: str) -> rsa.RSAPrivateKey:
    """
    
    """
    try:
        with open(filename, 'rb') as pem_in:
            private_bytes = pem_in.read()
            d_private_key = load_pem_private_key(private_bytes,password=None,)
        return d_private_key
    except Exception as e:
        print(f"Произошла ошибка при чтении: {e}")



def write_rsa_private_key(filename: str, key: rsa.RSAPublicKey) -> None:
    """
    
    """
    try:
        with open(filename, 'wb') as private_out:
            private_out.write(filename.private_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()))
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")