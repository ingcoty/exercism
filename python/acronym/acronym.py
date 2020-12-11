import re

def abbreviate(words):
    acronym = ''
    separated = re.findall('[a-zA-Z\'?]+', words)
    for word in separated:
        acronym += word[0].upper()
    return(acronym)
