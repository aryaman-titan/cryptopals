def xor_2_str(x, y):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y))

str = raw_input("Enter the string :")
xor = raw_input("Enter the xorString :")

str = str.decode("hex")
xor = xor.decode("hex")

outputString = xor_2_str(str, xor)
print(outputString.encode("hex"))
