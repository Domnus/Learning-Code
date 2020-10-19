def paper_doll(string):
    new_string = ''

    for i in string:
        new_string += (i * 3)

    return new_string

print(paper_doll('Mississippi'))
