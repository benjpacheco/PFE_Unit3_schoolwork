dictionary = {}

while True:
    english = input('Enter English word: ')
    if english in dictionary:
        print(english, '=', dictionary[english])
    else:
        trans = input('Enter translation: ')
        dictionary[english] = trans
    print()
