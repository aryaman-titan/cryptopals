
hex_string = raw_input("Enter string : ")
decoded = hex_string.decode("hex")
b64_string = decoded.encode("base64")

print(b64_string)
