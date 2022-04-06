def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz#'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def lengths(lines):
    lengths = []
    for line in lines:
        lengths.append(len(line))
    return lengths


count = 0
maxwordCount = 0
wordCount = []

with open('elon-musk.txt') as tweets:
    for tweet in tweets:
        count += 1
        words = tweet.split()
        wordCount.append(words)
        if len(words) > maxwordCount:
                maxwordCount = len(words)
                maxTweet = tweet

while True:
    
            
print('Number of tweets:', count)
print('Tweet with max number of words:', tweet)
