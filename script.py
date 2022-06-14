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
    # File processing for tweets before the George Floyd incident
    with open("before_georgefloyd.txt", encoding="utf-8") as f:
        tweets_before = f.readlines()

    # File processing for tweets after the George Floyd incident
    with open("after_georgefloyd.txt", encoding="utf-8") as f:
        tweets_after = f.readlines()

    # List of tags to be sought after
    tags = ['#blm', 'blm', '#blacklivesmatter', 'blacklivesmatter']

    # Calling of functions (before and after the incident)
    tweets_before_split = splitting_tweets(tweets_before)
    before_counter, before_counted = count_blm(tags, tweets_before_split)

    tweets_after_split = splitting_tweets(tweets_after)
    after_counter, after_counted = count_blm(tags, tweets_after_split)

    # Printing of results
    print("The mention for BLM in the week BEFORE the George Floyd incident is equal to: " + str(before_counter) +
          ", and the mentioned words and/or tags are (disregarding all uppercase, lowercase, and mixed variations): " +
          str(before_counted) + ".\n")

    print("The mention for BLM in the week of and after the George Floyd incident is equal to: " + str(after_counter) +
          ", and the mentioned words and/or tags are (disregarding all uppercase, lowercase, and mixed variations): " +
          str(after_counted) + ".")


if __name__ == "__main__":
    main()
