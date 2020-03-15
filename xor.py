#This is solution for Set-1->Challenge-2



def xorOperation(string, xor_key):
    res = bytearray(len(string))
    
    for i in range(0, len(string)):
        res[i] = string[i]^xor_key[i]
    return res


hex_str = raw_input("Enter string 1 : ")
xor_str = raw_input("Enter string 2 : ")

string = bytearray.fromhex(hex_str)
xor_key = bytearray.fromhex(xor_str)

print (string)
print (xor_key)


 
res = bytes(xorOperation(string, xor_key))
output = res.encode("hex")
print(res)

print (output)

