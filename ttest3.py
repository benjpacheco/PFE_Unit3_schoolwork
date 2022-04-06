count = 0
maxwordCount = 0
wordCount = {}
maxTweet = " "
with open('elon-musk.txt') as tweets:
    linenum = 1
    for tweet in tweets:
        for word in tweet.split()
            if word in wordCount:
                wordCount[word].append(linenum)
        count += 1
        words = tweet.split()
        wordCount.append(words)
        if len(words) > maxwordCount:
                maxwordCount = len(words)
                maxTweet = tweet
            
print('Number of tweets:', count)
print('Tweet with max number of words:', tweet)
