def echo():
    return "Echo"


def del_before(strng, char):
    string = ''
    for i in strng:
        string += i
        if i == char:
            string = ''
    return string


def del_after(strng, char):
    string = ''
    for i in strng:
        if i == char:
            return string
        string += i

