import json
import math
import mpmath

from const import M, PI,PATH


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
    

def bit_frequency_test(e: str)-> float:
    """
 The function checks the sequence for randomness
 Arguments:
 sequence string
 Returns:
 float: P value of the generator 
    """
    try:
        n = len(e)
        s=0
        for e in e:
            if e=="1":
                xi=1
            else:
                xi=-1
            s+=xi
        sn=abs(s/(math.sqrt(n)))
        return math.erfc(sn / math.sqrt(2))
    except Exception as e:
        print(f"Произошла ошибка во время теста: {e}")


def ident_con_bits_test(e: str)->float:
    """
    The function searches for sequences of all the same bits
 Arguments:
 sequence string
 Returns:
 float: P value of the generator 
    """
    try:
        n = len(e)
        s=(e.count("1")/n)
        if abs(s-0.5)>=(2/math.sqrt(n)):
            return
        vn = 0
        for i in range(0, n - 1):
            if e[i] != e[i + 1]:
                vn += 1
        pv = math.erfc(abs(vn - 2 * n * s * (1 - s))/ (2 * math.sqrt(2*n)* s * (1 - s)))
        return pv
    except Exception as e:
        print(f"Произошла ошибка во время теста: {e}")


def find_max_consecutive_ones(block:str)-> int:
    max_ones = 0
    current_ones = 0
    
    for bit in block:
        if bit == '1':
            current_ones += 1
            max_ones = max(max_ones, current_ones)
        else:
            current_ones = 0
    return max_ones


def unit_sequence_test(e:str)->float:
    """
    
    """
    try:
        n = len(e)
        observed_freq = [0, 0, 0, 0]
        for i in range(0,n,M):
            block = e[i : (i+M)]
            max_ones = find_max_consecutive_ones(block)
            
            if max_ones <= 1:
                observed_freq[0] += 1
            elif max_ones == 2:
                observed_freq[1] += 1
            elif max_ones == 3:
                observed_freq[2] += 1
            else:
                observed_freq[3] += 1
        x_squary=0
        for i in range(4):
            x_squary+=((observed_freq[i]-16*PI[i])**2)/(16*PI[i])
        pv=mpmath.gammainc(3/2, x_squary/2)
        return pv
    except Exception as e:
        print(f"Произошла ошибка во время теста: {e}")


def main()->None:
    path_c=read_json_file(PATH)
    seq_cpp=path_c["cpp"]
    seq_java=path_c["java"]
    print("Результаты тестов: ")
    print(bit_frequency_test(seq_cpp))
    print(bit_frequency_test(seq_java))
    print()
    print(ident_con_bits_test(seq_cpp))
    print(ident_con_bits_test(seq_java))
    print()
    print(unit_sequence_test(seq_cpp))
    print(unit_sequence_test(seq_java))


if __name__ == "__main__":
    main()
 
