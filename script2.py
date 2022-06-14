def splitting_tweets(tweets):
    """Takes a list of lines of tweets and returns a list of words from it"""
    tweets_split = []

    # Splits the lines of text into words converts to lowercase
    for tweet in tweets:
        words = tweet.split()
        for word in words:
            tweets_split.append(word.lower())

    return tweets_split


def count_blm(tags, tweets_split):
    """Takes a list of tags and a list of words of split tweets and returns
    a count of mentions of the specific tags as well as the tags mentioned"""
    counter = 0
    counted = []

    # Checks whether the word is equal to the tag, and counts if True
    for word in tweets_split:
        for tag in tags:
            if word == tag:
                counter += 1
                counted.append(word)

    return counter, set(counted)


def main():
    # File processing for tweets of a particular day (number-of-day.txt)
    with open("31.txt", encoding="utf-8") as f:
        tweets = f.readlines()

    # List of tags to be sought after
    tags = ['#blm', 'blm', '#blacklivesmatter', 'blacklivesmatter']

    # Calling of functions
    tweets_split = splitting_tweets(tweets)
    counter, counted = count_blm(tags, tweets_split)

    # Printing of results
    print("The count of the tag is: " + str(counter))


if __name__ == "__main__":
    main()
