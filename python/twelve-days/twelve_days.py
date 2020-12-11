def verse(id):
    verses = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]

    order_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
                  'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

    paragraph = "On the {0} day of Christmas my true love gave to me: ".format(
        order_list[id-1])

    list_verses = ''
    for num in range(id-1, -1, -1):
        list_verses += verses[num]
    paragraph += list_verses

    return(paragraph)


def recite(start_verse, end_verse):
    if start_verse == end_verse:
        return([verse(start_verse)])
    else:
        colection = []
        for i in range(start_verse, end_verse+1, 1):
            colection.append(verse(i))
        return(colection)
