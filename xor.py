#This is a test program

hex_str = "1c0111001f010100061a024b53535009181c"

decoded = hex_str.decode("hex")
test = decoded.encode("hex")
print (decoded)
print(test)