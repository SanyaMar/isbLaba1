import json

from cons import file_path


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
        print(f"Произошла ошибка: {e}")


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


def write_json_file(data: str, file_name: str) -> None:
    """
    This function writes data to a .json file

    Arguments:
        data: the data that we write to the file
        file_name: location the .json file in which we write the data
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Данные успешно записаны в файл {file_name}")
    except Exception as e:
        print(f"Произошла ошибка при записи файла: {e}")


def character_frequency_analysis(file_name: str, json_name: str) -> dict[str, str]:
    """
    This function performs a frequency analysis of the received text and outputs the frequency index of the character

    Arguments:
        file_name: the location of the file in which the text under study is located
        json_name: the location of the file where the analysis result is recorded
    Returns:
        dict: the dictionary in which the characters and their frequency are recorded
    """
    frequency = {}
    text = read_text_from_file(file_name)
    total_chars = len(text)

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char, count in frequency.items():
        frequency[char] = count / total_chars

    sorted_freq = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    write_json_file(sorted_freq, json_name)

    # for char, freq in sorted_freq.items():
    #     print(f" '{char}':  {freq:.6f}")


# character_frequency_analysis("lab_1/task2/text2.txt","lab_1/task2/frequency_analysis.json")


def encrypt(name_file: str, key_file: str) -> str:
    """
    This function encrypts the specified text using a key

    Arguments:
        name_file: the location of the file in which the text is to be encrypted
        key_file: the location of the file where the encryption key is recorded
    Returns:
        encrypted_text: key-encrypted text
    """
    try:
        key = read_json_file(key_file)
        text = read_text_from_file(name_file)
        encrypted_text = ""
        for char in text:
            encrypted_text += key[char]
        return encrypted_text
    except Exception as e:
        print(f"Произошла ошибка при шифровании: {e}")
        return None


def decrypt_text_with_key(name: str, key_file: str) -> str:
    """
    This function decrypts the specified text using a key

    Arguments:
        name: the location of the file in which the text is to be decrypted
        key_file: the location of the file where the decryption key is recorded
    Returns:
        encrypted_text: key-decrypted text
    """
    try:
        key = read_json_file(key_file)
        text = read_text_from_file(name)
        decrypted_text = ""
        for char in text:
            decrypted_text += key[char]
        return decrypted_text
    except Exception as e:
        print(f"Произошла ошибка при расшифровке текста: {e}")
        return None


def main() -> None:
    path_of_file = read_json_file(file_path)
    text1 = path_of_file["path_text_1"]
    key1 = path_of_file["path_key_1"]
    encrypted_text = path_of_file["path_encrypted_text"]
    encrypted = encrypt(text1, key1)
    write_to_txt_file(encrypted, encrypted_text)
    text2 = path_of_file["path_taxt_2"]
    key2 = path_of_file["path_key_2"]
    decrupted_text = path_of_file["path_decrupted_text"]
    text = decrypt_text_with_key(text2, key2)
    write_to_txt_file(text, decrupted_text)


if __name__ == "__main__":
    main()
