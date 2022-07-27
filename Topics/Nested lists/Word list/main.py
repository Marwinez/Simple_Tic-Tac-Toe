text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
char_num = int(input())
short_list = [word for word_group in text for word in word_group if len(word) <= char_num]
print(short_list)
