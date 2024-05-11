import json
import math
import mpmath

from const import M, PI

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
    

def bit_frequency_test(sequence):
    """
    
    """
    try:
        n = len(sequence)
        s=0
        for e in sequence:
            if e=="1":
                xi=1
            else:
                xi=-1
            s+=xi
        sn=abs(s/(math.sqrt(n)))
        return math.erfc(sn / math.sqrt(2))
    except Exception as e:
        print(f"Произошла ошибка во время теста: {e}")


def ident_con_bits_test(E):
    """
    
    """
    try:
        n = len(E)
        s=(E.count("1")/n)
        if abs(s-0.5)>=(2/math.sqrt(n)):
            return
        vn = 0
        for i in range(0, n - 1):
            if E[i] != E[i + 1]:
                vn += 1
        pv = math.erfc(abs(vn - 2 * n * s * (1 - s))/ (2 * math.sqrt(2*n)* s * (1 - s)))
        return pv
    except Exception as e:
        print(f"Произошла ошибка во время теста: {e}")


def find_max_consecutive_ones(block):
    max_ones = 0
    current_ones = 0
    
    for bit in block:
        if bit == '1':
            current_ones += 1
            max_ones = max(max_ones, current_ones)
        else:
            current_ones = 0
    
    return max_ones
def unit_sequence_test(E):
    """
    
    """
    try:
        n = len(E)
        observed_freq = [0, 0, 0, 0]
        for i in range(0,n,M):
            block = E[i : (i+M)]
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

name="01110010110011101001001101011001011010011101100100001110111001100101110011011010111000100000001110001110100110001010010100000100"
print(unit_sequence_test(name))