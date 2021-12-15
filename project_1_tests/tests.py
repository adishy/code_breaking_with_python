from random import randrange, sample

def test_convert_to_natural_index(test_func):
    for i in range(26):
        letter = chr(ord('a') + i)
        expected_output = i
        test_output = test_func(letter)
        if test_output != expected_output:
            print("❌ Your implementation produced incorrect output for:", letter)
            print("Expected output:", i)
            print("Output generated:", test_output)
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
            print("Expected output:", expected_output)
            print("Output generated:", test_output)
            return 
    print("✔✔ Your implementation is correct!")

def test_encrypt_word(test_func):
    dictionary_filename = "dictionary.txt"
    dictionary = open(dictionary_filename).read().splitlines()
    sampled = sample(dictionary, 25)

    for i, word in enumerate(sampled):
        word = word.strip()
        sanitized_word = ""

        # Make sure word contains only letters
        for letter in word:
            if letter.isalpha():
                mix  = False
                # 25% chance that some letters in the last 5 words will be capitalized
                if i >= 20 and 25 < randrange(100):
                        mix = True
                if mix:
                    sanitized_word += letter.upper()
                else:
                    sanitized_word += letter

        expected_output = ""
        shift = randrange(250) 

        for letter in sanitized_word:
            letter = letter.lower()
            char_index  = ord(letter) - ord('a')
            shifted_letter = chr(ord('a') + ((char_index + shift) % 26))
            expected_output += shifted_letter
        
        test_output = test_func(sanitized_word, shift)

        if expected_output != test_output:
            print("❌ Your implementation produced incorrect output for word:", f"\"{sanitized_word}\"", f"(shift: {shift})")
            print("Expected output:", expected_output)
            print("Output generated:", test_output)
            return

    print("✔✔ Your implementation is correct!")
