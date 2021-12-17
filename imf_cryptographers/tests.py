import json
from random import randrange, sample
from imf_cryptographers.solution import decrypt_all_sol

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
            print("❌❌ Your implementation produced incorrect output for:", letter, f"(shift: {i})")
            print("Expected output:", expected_output)
            print("Output generated:", test_output)
            return 
    print("✔✔ Your implementation is correct!")

def encrypt_word_sol(word, shift):
    encrypted_word = ""
    for letter in word:
        letter = letter.lower()
        char_index  = ord(letter) - ord('a')
        shifted_letter = chr(ord('a') + ((char_index + shift) % 26))
        encrypted_word += shifted_letter
    return encrypted_word

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

        shift = randrange(250) 
       
        expected_output = encrypt_word_sol(sanitized_word, shift)
        
        test_output = test_func(sanitized_word, shift)

        if expected_output != test_output:
            print("❌ Your implementation produced incorrect output for word:", f"\"{sanitized_word}\"", f"(shift: {shift})")
            print("Expected output:", expected_output)
            print("Output generated:", test_output)
            return

    print("✔✔ Your implementation is correct!")

def encrypt_sentence_sol(sentence, shift):
    words = sentence.split(" ")
    encrypted_sentence = []
    for word in words:
        encrypted_sentence.append(encrypt_word_sol(word, shift))
    return encrypted_sentence

def test_encrypt_sentence(test_func):
    sentences = [
        "this is an example",
        "this is a very secret message",
        "a SeNTENCE tHat Has uppercase aND LOWERCASE letters",
        "some additional TEsTs",
        "this works TOOOOOoooo right it should if all the others works too",
        "Ethan Hunt is really annoying",
        "Yes we must find a way to solve that particular problem",
        "HaHaHa tHe iMf WILL haVe NO CLUE tHAt we MiX lETTErs for no ReaSoN",
    ]

    for sentence in sentences:
        for i in range(52):
            expected_output = encrypt_sentence_sol(sentence, i)
            test_output = test_func(sentence, i)

            if type(test_output) != type([]):
                print("❌❌ Your implementation produced incorrect output for:", sentence, f"(shift: {i})")
                print("Remember, your implementation should return a list of encrypted words..")
                return

            if expected_output != test_output:
                print("❌❌ Your implementation produced incorrect output for:", sentence, f"(shift: {i})")
                print("Expected output:", json.dumps(expected_output, indent=3))
                print("Output generated:", json.dumps(test_output, indent=3))
                return 
    print("✔✔ Your implementation is correct!")
                            
def test_decrypt_all(test_func, encrypted_messages):
    expected_output = decrypt_all_sol(encrypted_messages, True)
    test_output = test_func(encrypted_messages)

    if type(test_output) != type([]):
        print("❌❌ Your implementation did not correctly generate the correct type of output")
        print("Your code should generate a list of messages that have been decrypted")
        print("Your function returned output of the type:", type(test_output))
        return

    if len(expected_output) != len(test_output):
        print("❌❌ Your implementation did not correctly generate output for all the encrypted messages")
        print("Expected number of messages decrypted:", len(expected_output))
        print("Number of messages decrypted by your implementation:", len(test_output))
        return

    else:
        for i, message in enumerate(test_output):
            if message != expected_output[i]:
                print(f"❌❌ Your implementation produced incorrect output for encrypted_messages[{i}]:")
                if type(message) != type(expected_output[i]):
                   print("   Your code produced messages of the wrong data type:")
                   print("   Expected message data type:", type(expected_output[i]))
                   print("   Message data type generated:", type(message))
                   return  
                print("  Ciphertext:", encrypted_messages[i])
                print("  Incorrect plaintext:", message)
                return 
    
        print("✔✔ Your implementation is correct!")
        print("Here are the decrypted messages:")
        print(json.dumps(test_output, indent=3))
        print()
        print("🎉🎉🎉🎉🎉🎉🎉 You have successfully helped thwart the group's nefarious activities and have saved millions of lives! The I.M.F thanks you for you brilliant efforts 🎉🎉🎉🎉🎉🎉🎉🎉")

