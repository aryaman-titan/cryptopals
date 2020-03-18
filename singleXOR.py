#This is solution to Set-1->Challenge-2


def single_xorOperation(string, xor_key):
    length = len(string)
    res = bytearray(length)
    for i in range(length):
        res[i] = string[i]^xor_key
    return res
    


hex_encoded_str = raw_input("Enter the encoded string :")

string = bytearray.fromhex(hex_encoded_str)

print(string)

for x in range(256):
    res = single_xorOperation(string, x)
    print(res, "encoded by", x)

