def bitwise_hamming_distance(bytes1, bytes2):
    """Returns the bitwise Hamming distance between two bytes objects.
    Based on this definition from https://en.wikipedia.org/wiki/Hamming_distance:
    "For binary strings a and b the Hamming distance is equal to the number of ones (population count) in a XOR b."
    """
    bitwise_xor_byte_integers = [(a ^ b) for a, b in zip(bytes1, bytes2)]
    distance = 0
    for byte in bitwise_xor_byte_integers:
        distance += bin(byte).count('1')  # bin() generates a binary string from a byte
    return distance

b1 = bytearray("this is a test")
b2 = bytearray("wokka wokka!!!")

ans = bitwise_hamming_distance(b1, b2)
print(ans)