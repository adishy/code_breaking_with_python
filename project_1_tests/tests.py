from random import randrange

def test_convert_to_natural_index(test_func):
    for i in range(26):
        letter = chr(ord('a') + i)
        expected_output = i
        test_output = test_func(letter)
        if test_output != expected_output:
            print("❌ Your implementation produced incorrect output for:", letter)
            print("Expected output:", i, "Output generated:", test_output)
            return 
    print("✔✔ Your implementation is correct!")

def test_shift_letter_by_k(test_func):
    letter = chr(ord('a') + randrange(26))
    for i in range(52):
        letter_index = ord(letter) - ord('a')
        expected_output = chr(ord('a') + ((letter_index + i) % 26))
        test_output = test_func(letter, i)
        if test_output != expected_output:
            print("❌❌ Your implementation produced incorred output for:", letter, f"(shift: {i})")
            print("Expected output:", expected_output, "Output generated:", test_output)
            return 
    print("✔✔ Your implementation is correct!")
