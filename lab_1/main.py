import json


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

    for char, freq in sorted_freq.items():
        print(f" '{char}':  {freq:.6f}")
character_frequency_analysis("lab_1/task2/text2.txt","lab_1/task2/frequency_analysis.json")