
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext


occurences = {}
with open('pap.txt') as book:
    for line in book:
        for word in cleanedup(line).split():
            if word in occurences:
                occurences[word] += 1
            else:
                occurences[word] = 1
while True:
    word = input('Enter word: ')
    if word in occurences:
        print(word, 'was used', occurences[word], 'times')
    else:
        print('Not found')
            
