import argparse

from algoritms.rsa import AsymmetricKey
from algoritms.tripldes import SymmetricKey
from files_funct import FilesFunct
from const import SETTINGS


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-pr', '--program', type=int, help='Выбор режима работы: '
                        '0 - Генерация симметричного ключа'
                        '1 - Генерация асимметричного ключа'
                        '2 - Шифрование симметричного ключа'
                        '3 - Дешифрование симметричного ключа'
                        '4 - Шифрования текста'
                        '5 - Дешифрования текста')
    parser.add_argument('-set', '--settings', default=SETTINGS,
                        type=str, help='Открывает .json файл')

    args = parser.parse_args()
    settings = FilesFunct.read_json_file(args.settings)
    sym = SymmetricKey()
    asym = AsymmetricKey()

    match args.program:
        case 0:
            print("Генерация симметричного ключа")
            sym_key = sym.generate_key(sym.selecting_key_len())
            FilesFunct.write_bytes_to_file(settings['symmetric_key'],
                                           sym_key)
            print()
        case 1:
            print("Генерация асимметричного ключа")
            public_key, private_key = asym.generate_keys()
            FilesFunct.serialization_rsa_public_key(
                public_key, settings['public_key'])
            FilesFunct.serialization_rsa_private_key(
                private_key, settings['secret_key'])
            print()
        case 2:
            print("Шифрование симметричного ключа")
            asym.encrypt_symmetric_key(
                settings['symmetric_key'],
                settings['public_key'],
                settings['encryp_symmetric_key']
            )
            print()
        case 3:
            print("Дешифрование симметричного ключа")
            asym.decrypt_symmetric_key(
                settings['encryp_symmetric_key'],
                settings['secret_key'],
                settings['decryp_symmetric_key']
            )
            print()
        case 4:
            print("Шифрования текста")
            sym.encrypt_text(
                settings['initial_file'],
                settings['encrypted_file'],
                settings['decryp_symmetric_key']
            )
            print()
        case 5:
            print("Дешифрования текста")
            sym.decrypt_text(
                settings['encrypted_file'],
                settings['decrypted_file'],
                settings['decryp_symmetric_key']
            )
            print()
