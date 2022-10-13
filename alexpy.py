def echo():
    return "Echo"


def del_before(strng, char):
    """
        Returns a string with everything before a specified character deleted

        Usage: del_after(string, char)

        E.g: del_after("C:/users/username/Desktop/file.txt","file.txt") ==> "file.txt"
    """
    string = ''
    for i in strng:
        string += i
        if i == char:
            string = ''
    return string


def del_after(string, char):
    """
    Returns a string with everything after a specified character deleted

    Usage: del_after(string, char)

    E.g: del_after("username@email.com","@") ==> "username"
    """
    strng = ''
    for i in string:
        if i == char:
            return strng
        strng += i


def find_letter(x, y):
    """
    Returns a list of all the indexes where the character was found

    Usage: find_letter(string, character)

    E.g: find_letter("mississippi", "i") ==> [1, 4, 7, 10]
    """
    return [idx for idx, value in enumerate(x) if value == y]


