def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz#'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext


count = 0
maxwordCount = 0
concordance = {}

with open('elon-musk.txt') as tweets:
    for tweet in tweets:
        linenum = 1
        count += 1
        words = tweet.split()
        if len(words) > maxwordCount:
                maxwordCount = len(words)
                maxTweet = tweet
        for hashtag in cleanedup(tweet).split():
            if hashtag in concordance:
                concordance[hashtag].append(linenum)
            else:
                concordance[hashtag]=[linenum]
        linenum += 1
                
print('Number of tweets:', count)

print('Tweet with max number of words:', maxTweet)

while True:
    hashtag = input('Enter hashtag: ')
    if '#' in hashtag:
        if hashtag in concordance:
            print('Mentioned:', len(concordance[hashtag]), 'times.')
        else:
            print('Not mentioned.')
    else:
        print('Not mentioned.')
               


                

