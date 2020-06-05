# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(word):
    first_letter = word[0]
    inbetween = word[1:3]
    fourth = word[3]
    rest = word[4:]
    first_letter = first_letter.upper()
    fourth = fourth.upper()
    final_word = first_letter + inbetween + fourth + rest
    print(final_word)

old_macdonald('macdonald')