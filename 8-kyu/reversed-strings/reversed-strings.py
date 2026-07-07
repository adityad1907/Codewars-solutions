def solution(string):
    rev = ""
    for letters in str(string[::-1]):
        for i in range(len(letters)):
            rev += letters[i]
    return rev