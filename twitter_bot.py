import tweepy
import time

# Consumers API
CONSUMER_API_KEY = "wGda0HvwfUhSnJO2wnWcgby3Z"
CONSUMER_SECRET_KEY = "9pErtO02z4FO4Ua71kDRB3eTDAbA3seJtiANemgxOY7tfFxoCa"

# Access tokens
ACCESS_TOKEN = "1454373730868609025-e3bjsbQB5iyq8TDb69Flzi3zzn07Po"
ACCESS_SECRET_TOKEN = "tVRKiunvctWGCeeeQJrsyehXfMgpONuWKZNOXmg2wMA6a"

# Setting authentication for Twitter API
auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
user = api.me

# Keyword that is going to be searched
SEARCH_KEYWORD = 'namihyun'
# Maximum number of tweets that the API will return
NUMBER_OF_TWEETS = 20
# How many seconds the code will stop before retweeting and liking again
SLEEP_SECONDS = 10

while True:
    for tweet in tweepy.Cursor(api.search, SEARCH_KEYWORD).items(NUMBER_OF_TWEETS):
        try:
            # If the keyword is in the text of the twitt (excluding the username and other parts)
            # then retweets and likes it.
            if SEARCH_KEYWORD in tweet.text.lower():
                print('Done!')
                tweet.retweet()
                time.sleep(SLEEP_SECONDS)

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    
    # Stoping X seconds and trying again to avoid the restrictions getting twitts.
    # Which are 180 twitts per 15 mins.
    time.sleep(30)
