def average(num):
    total = 0
    for number in num:
        total += number
    return total/len(num)

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

while True:
    line = input('Enter a sentence: ')
    words = cleanedup(line).split()
    print('Average word length:', average(lengths(words)))

