import re


def count_words(sentence):
    result = re.findall(r'[a-zA-Z0-9\'?]+', sentence)
    words = []
    for element in result:
        words.append((element.lower()).strip("'"))

    base = set(words)
    count = 0
    obj = {}
    for item in base:
        for each_word in words:
            if item == each_word:
                count += 1
        obj[item] = count
        count = 0

    return(obj)
