import json


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