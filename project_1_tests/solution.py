import json
from random import randrange

messages = [
   "safe to talk question mark",
   "yes absolutely",
   "do not worry about it the imf will never break this encryption scheme",
   "so when will we meet today question mark",
   "the meeting is in the afternoon",
   "center plaza as usual",
   "yeah but in a different house this time",
   "last time we got too drunk and made a lot of noise so the police came snooping and we almost got caught",
   "what will we eat at the meeting",
   "we have the best snacks",
   "these snacks are pretty great though you have to admit that",
   "less eating and more plotting please",
   "this is a really evil plan is it not",
   "yes but the world needs to be changed",
   "yeah it is rotting and the people are the problem",
   "so once the fake bombs are in place we will tweet the location to mislead the police",
   "then at the party we will put false trackers in the pockets of everyone there",
   "the imf agents will definitely take that bait",
   "hunt will probably be on our trail though",
   "yeah that is going to be a huge problem",
   "no it is okay we have a plan for that",
   "hunt is incapable of deciding between saving one and many",
   "we will exploit this and put some exploding trackers in only some of their pockets",
   "they will be really really busy trying to save everyone",
   "so where is the real bomb question mark",
   "do you not know about our plan question mark",
   "no i was not here last time",
   "remember i was trying to lead away those pesky imf agents",
   "oh yeah great job on getting rid of them",
   "okay so since you do not know this is the part of the plan that is actually genius",
   "there is no one bomb",
   "the bomb is everywhere",
   "wait what how question mark",
   "we infiltrated the supply chains of some electric car factories",
   "we managed to put in some code that will overload the batteries and make them explode",
   "boom boom boom everywhere at once",
   "no way to stop it",
   "even better we can take control of the car remotely and drive it anywhere we want",
   "a hundred thousand portable bombs with minds of their own",
   "the expected amount of radiation fallout is huge",
   "this will really bring about the change we require to fix things",
   "that is really amazing",
   "why thank you glad you agree with this plan",
   "are we all set question mark",
   "absolutely",
   "tomorrow question mark",
   "tomorrow it is then",
   "okay these snacks will not be warm forever we should eat soon",
]

def load_dictionary():
    dictionary_filename = "dictionary.txt"
    dictionary_file = open(dictionary_filename, 'r')
    dictionary = set()
    for line in dictionary_file.readlines():
        line = line.strip()
        dictionary.add(line)
    return dictionary

def shift_letters_in_word(word, shift, break_code = True):
    word = word.lower()
    encoded_word = ""
    num_letters = 26
    start_letter_ascii = ord('a')
    # Shift each letter in the word by the specified number and store the result
    for letter in word:
        actual_letter_index = ord(letter) - start_letter_ascii
        shifted_letter_index = (actual_letter_index + shift) % num_letters
        shifted_letter_ascii = shifted_letter_index + start_letter_ascii
        shifted_letter = chr(shifted_letter_ascii)
        if not break_code and randrange(100) < 32:
            shifted_letter = shifted_letter.upper()
        encoded_word = encoded_word + shifted_letter
    return encoded_word

def make_code(plaintext, shift):
    words = plaintext.split(" ")
    changed_words = []
    for word in words:
        changed_word = shift_letters_in_word(word, shift, False)
        changed_words.append(changed_word)
    return " ".join(changed_words)

def generate_encrypted_messages():
    encrypted_sentences = []
    for sentence in sentences:
        shift = randrange(125)
        while ( shift % 26 ) == 0:
            shift = randrange(125)
        encrypted = make_code(sentence, shift)
        encrypted_sentences.append(encrypted)
    print(json.dumps(encrypted_sentences, indent=3))

def break_code(encoded_input):
    dictionary = load_dictionary()
    
    # Break input sentence into "words" (separated by spaces)
    words = encoded_input.split(" ")
    
    # Normalize all the letters in the word to the same (lower) case
    index = 0
    while index < len(words):
        words[index] = words[index].lower()
        index = index + 1
        
    possible_shift = 0
    num_letters = 26
    
    # Try all possible shifts
    while possible_shift < num_letters:
        changed_words = []
        
        # Go through all the words in the input
        for word in words:
            encoded_word = shift_letters_in_word(word, possible_shift)
            changed_words.append(encoded_word)
        
        # Check if every decoded word exists in the dictionary
        all_words_correct = True
        for changed_word in changed_words:
            all_words_correct = all_words_correct and (changed_word in dictionary)
        # If all the words exist, this is our shift!
        if all_words_correct:
            return " ".join(changed_words)
        
        possible_shift = possible_shift + 1
        
    return "Could not break code!"

def encrypt_all_sol(messages):
    encrypted_messages = []
    for message in messages:
        shift = randrange(125)
        while ( shift % 26 ) == 0:
            shift = randrange(125)
        encrypted_messages.append(make_code(message, shift))
    return encrypted_messages

def decrypt_all_sol(encrypted_messages):
    decrypted_messages = []
    for ciphertext in encrypted_messages:
        plaintext = break_code(ciphertext)
        decrypted_messages.append(plaintext)
    for i, plaintext in enumerate(decrypted_messages):
        if plaintext != messages[i]:
            print("Expected output:", messages[i])
            print("Output generated:", plaintext)
            return
    print("All messages have been decrypted correctly")
    print(json.dumps(decrypted_messages, indent=3))

def get_encrypted_messages():
    encrypted_messages = encrypt_all_sol(messages)
    print(json.dumps(encrypted_messages, indent=3))
    return encrypted_messages

if __name__ == "__main__":
    decrypt_all_sol(encrypt_all_sol(messages))
