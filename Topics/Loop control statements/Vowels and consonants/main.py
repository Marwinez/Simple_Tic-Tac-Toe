import string

vowels = "aeiou"
for letter in input():
    if letter in vowels:
        print("vowel")
    elif letter in string.ascii_lowercase:
        print("consonant")
    else:
        break
