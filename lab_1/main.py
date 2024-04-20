import json

from cons import file_path

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def write_to_txt_file(text, file_name):
    try:
        with open(file_name + '.txt', 'w',encoding='utf-8') as file:
            file.write(text)
        print(f"Текст успешно записан в файл {file_name}.txt")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


def read_json_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return None


def write_json_file(data, file_name):
    try:
        with open(file_name, 'w',  encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Данные успешно записаны в файл {file_name}")
    except Exception as e:
        print(f"Произошла ошибка при записи файла: {e}")

def character_frequency_analysis(file_name, json_name):
    frequency = {}
    text=read_text_from_file(file_name)
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

def encrypt(name_file, key_file):
    try:
        key=read_json_file(key_file)
        text = read_text_from_file(name_file)
        encrypted_text = ""
        for char in text:
            encrypted_text += key[char]
        return encrypted_text
    except Exception as e:
        print(f"Произошла ошибка при шифровании: {e}")
        return None
    
def decrypt_text_with_key(name, key_file):
    try:
        key=read_json_file(key_file)
        text = read_text_from_file(name)
        decrypted_text = ""
        for char in text:
            decrypted_text += key[char]
        return decrypted_text
    except Exception as e:
        print(f"Произошла ошибка при расшифровке текста: {e}")
        return None


def main() -> None:
    path_of_file=read_json_file(file_path)
    text1=path_of_file["path_text_1"]
    key1=path_of_file["path_key_1"]
    encrypted_text=path_of_file["path_encrypted_text"]
    encrypted=encrypt(text1,key1)
    write_to_txt_file(encrypted,encrypted_text)
    text2=path_of_file["path_taxt_2"]
    key2=path_of_file["path_key_2"]
    decrupted_text=path_of_file["path_decrupted_text"]
    text = decrypt_text_with_key(text2,key2)
    write_to_txt_file(text,decrupted_text)


if __name__ == "__main__":
    main()