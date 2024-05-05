import json
import math
import mpmath


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
# print(bit_frequency_test("lab_2/sequences.json"))
# def frequency_bitwise_test(name: str) -> float:
#     """
#  The function checks whether the sequence is random enough
#  Args:
#  name: path .json file
#  Returns:
#  float: P-value is the probability that the
#  generator produces values comparable
#  to the reference
#     """
#     s = abs(sum(1 if i == "1" else -1 for i in name)) / math.sqrt(len(name))
#     return math.erfc(s / math.sqrt(2))
name="01110010110011101001001101011001011010011101100100001110111001100101110011011010111000100000001110001110100110001010010100000100"
print(bit_frequency_test(name))