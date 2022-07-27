word = input()
answer = ""
first = True
for letter in word:
    if first:
        letter = letter.lower()
        answer = answer + letter
        first = False
    else:
        if letter.isupper():
            letter = letter.lower()
            answer = answer + "_" + letter
        else:
            answer = answer + letter
print(answer)
