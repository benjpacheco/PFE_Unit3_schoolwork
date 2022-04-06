def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

maxlength = 0
with open('pap.txt') as book:
    for line in book:
        for word in cleanedup(line).split():
            length = len(word)
            if length > maxlength:
                 maxlength = length
                 maxword = word
print(maxword)
                
     
