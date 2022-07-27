text = str(input())
illegal = ['?', '!', '.', ',']
text = text.lower()
for character in text:
    if character in illegal:
        text = text.replace(character, "")
print(text)
