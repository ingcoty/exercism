def is_isogram(string):
    print(string)
    string = string.lower()
    print(string)
    for letter in string:
        repeated = 0
        print(letter)
        for sample in string:
            if letter == sample and letter != " " and letter != "-":
                repeated += 1

        if repeated > 1:
            return False

    return True
