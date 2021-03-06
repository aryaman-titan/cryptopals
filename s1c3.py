character_frequency_English = {
        'e' : 12.0,
        't' : 9.10,
        'a' : 8.12,
        'o' : 7.68,
        'i' : 7.31,
        'n' : 6.95,
        's' : 6.28,
        'r' : 6.02,
        'h' : 5.92,
        'd' : 4.32,
        'l' : 3.98,
        'u' : 2.88,
        'c' : 2.71,
        'm' : 2.61,
        'f' : 2.30,
        'y' : 2.11,
        'w' : 2.09,
        'g' : 2.03,
        'p' : 1.82,
        'b' : 1.49,
        'v' : 1.11,
        'k' : 0.69,
        'x' : 0.17,
        'q' : 0.11,
        'j' : 0.10,
        'z' : 0.07,
}

def xor_2_str(string, xorKey):
    flag = ''
    score = 0
    for x in range(len(string)):
        iter = chr(ord(string[x])^xorKey)
        if(iter in character_frequency_English):
            score += character_frequency_English.get(iter)
        flag += iter
    return flag, score



str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
str = str.decode("hex")

for i in range(256):
    flag, score = xor_2_str(str, i)
    if(score > 100):
        print(flag, " : ", i, score)
        
