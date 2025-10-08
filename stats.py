def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    lowers = text.lower()
    character = {
            }
    
    for i in lowers:
        character[i] = character.get(i, 0) + 1

    return character

def list_of_dicts(dict):
    list = []
    for ch in dict:
        num = dict[ch]
        pair = {"char": ch, "num": num}
        list.append(pair)
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(items):
    return items["num"]
