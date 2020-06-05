# ANIMAL CRACKERS: Write a function takes a two-word string 
# and returns True if both words begin with same letter

def animalCrackers(text):
    word, word1 = text.split(' ')
    if word[0] == word1[0]:
        print('True')
    else:
        print('False')

animalCrackers('Crazy Kangaroo')
