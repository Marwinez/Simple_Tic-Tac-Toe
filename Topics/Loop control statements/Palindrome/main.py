word = [char for char in str(input())]
backwards = []
i = len(word) - 1
while i >= 0:
    backwards.append(word[i])
    i -= 1
if word == backwards:
    print("Palindrome")
else:
    print("Not palindrome")
