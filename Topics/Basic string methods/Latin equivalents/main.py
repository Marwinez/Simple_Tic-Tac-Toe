name = input()


def normalize(new_name):
    cursed = ['é', 'ë', 'á', 'å', 'œ', 'æ']
    latin = ['e', 'e', 'a', 'a', 'oe', 'ae']
    for character in new_name:
        if character in cursed:
            index = cursed.index(character)
            new_name = new_name.replace(character, latin[index])

    return new_name


print(normalize(name))

