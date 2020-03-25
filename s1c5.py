def xor_2_str(x, y):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y))

def xorKey(str, Key):
    strlen, keylen = len(str), len(Key)
    output = (1 + (strlen//keylen))*Key
    return output[:strlen]

str = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
xorKey = xorKey(str, "ICE")
print((xor_2_str(str,xorKey)).encode("hex"))