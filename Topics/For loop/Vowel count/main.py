string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
answer = 0
for i in string:
    if i in vowels:
        answer = answer + 1
print(answer)
