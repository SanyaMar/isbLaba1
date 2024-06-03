import argparse
import json

from algoritms.rsa import AsymmetricKey
from algoritms.tripldes import SymmetricKey
from const import SETTINGS
import files_funct


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-pr', '--program', type=int, help='Выбор режима работы: '
                        '0 - Запускает режим генерации ключей'
                        '1 - Запускает режим шифрования'
                        '2 - Запускает режим дешифрования')
    parser.add_argument('-set', '--settings', default=SETTINGS,
                        type=str, help='Открывает .json файл')
    args = parser.parse_args()

    try:
        with open(args.settings, 'r', encoding='utf-8') as file:
            settings = json.load(file)
    except Exception as e:
        print(f"Произошла ошибка при загрузке: {e}")

    sym = SymmetricKey()
    asym = AsymmetricKey()

    match args.program:
        case 0:
            print("Генерация ключей гибридной системы")
            print()
            len_key = sym.selecting_key_len()
            sym_key = sym.generate_key(len_key)
            files_funct.write_bytes_to_file(settings['symmetric_key'], sym_key)
            public_key, private_key = asym.generate_keys()
            files_funct.serialization_rsa_public_key(
                public_key, settings['public_key'])
            files_funct.serialization_rsa_private_key(
                private_key, settings['secret_key'])
            asym.encrypt_symmetric_key(
                settings['symmetric_key'], settings['public_key'], settings['encryp_symmetric_key'])
        case 1:
            print(" Шифрование данных гибридной системой")
            print()
            asym.decrypt_symmetric_key(
                settings['encryp_symmetric_key'], settings['secret_key'], settings['decryp_symmetric_key'])
            sym.encrypt_text(
                settings['initial_file'], settings['encrypted_file'], settings['decryp_symmetric_key'])
        case 2:
            print()
            print("Дешифрование данных гибридной системой")
            asym.encrypt_symmetric_key(
                settings['symmetric_key'], settings['public_key'], settings['encryp_symmetric_key'])
            sym.decrypt_text(
                settings['encrypted_file'], settings['decrypted_file'], settings['decryp_symmetric_key'])
