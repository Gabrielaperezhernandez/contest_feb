alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""

# Open the file (ensure your secret message is saved as secret.txt)
with open("secret.txt") as f:
    for line in f:
        # 1. Count how many vowels are in the current line
        vowel_count = 0
        for char in line.lower():
            if char in vowel:
                vowel_count += 1

        # 2. Use that count to find the letter in the alphabet
        # Note: If a line has 0 vowels, it picks alphabet[0], which is a space.
        decoded_char = alphabet[vowel_count]

        # 3. Add that letter to our message
        message += decoded_char

print("The secret message is:")
print(message)

#TEACHER METHOD
alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""

# Open the file (ensure your secret message is saved as secret.txt)
with open("secret.txt") as f:
    for line in f:
        nr_vowels = 0
        for v in vowel:
            nr_vowels += line.count(v) #count the amount of time that particular vowel shows up
        letter = alphabet[nr_vowels]
        message += letter
print(message)