def int_to_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman = ""
      
    while number:
        div = number // num[i]
        number %= num[i]
  
        while div:
            roman += sym[i]
            div -= 1
        i -= 1
    
    return roman

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    num = 0

    while i < len(s):
        # Caso seja uma subtração.
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            num += roman[s[i + 1]] - roman[s[i]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num

if __name__ == "__main__":
    number = 1913
    roman = int_to_roman(number)
    print("O número convertido para romano é:", roman)
    integer = roman_to_int(roman)
    print("O símbolo romano convertido de volta para inteiro é:", integer)

