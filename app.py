"""
    Flow:=>
1. Training and test data
    - Collect training and test data
    - Categorize the data 

2. Preprocessing 
    - Clean data
    - Lemmatize
    - Remove stop words
    - Format data
    - split into training and test data

3. Learning
    - Supervised Learning 
    - Usign the sentiment learning algorithm


4. Testing 

    - Measure accuracy
    - Test Algorithm
    - Persist Model

"""

import tweepy
def get_twitter_api(): 
    API_Key = "f9O2YBcIhTsZyq7R0hgXhV7ot"
    API_Secret_key = "ATeYV3yOFPW812UAaO7uCNl6X1Ofd5IheRqccsVnAAObRgnS4b"
    Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAFXbNQEAAAAARipHhiZMu%2F2LroR6JXKunjL77GM%3Ds2Cf3n0Qxcyu3mfKZgyDbWn6jZvLTUanq3bdnq9venP5J7shXb"
    ACCESS_TOKEN = "356619240-ddyfoN3T3mMBiM2tdABw6rMpPmc0WsRAICJfPuqq"
    ACCESS_TOKEN_SECRET = "n1rhpgeD4OA4S6lRteG1cZ3fX0tyvMh2u81tvS0v6hcdf"


    auth = tweepy.OAuthHandler(API_Key,API_Secret_key)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    return api

    """[We use pagination(dividing page) a lot in Twitter API development. 
    Iterating through timelines, user lists, direct messages, etc. 
    In order to perform pagination, we must supply a page/cursor parameter
     with each of our requests. 
     https://docs.tweepy.org/en/latest/cursor_tutorial.html]
    """


def collectData(api, twitterUser):
    favorite_count = list()
    retweet_data = list()
    for status in tweepy.Cursor(api.user_timeline, id = "twitter_user").items(100):
        #print( status.text)
        retweet_data.append(status.retweet_count)
        favorite_count.append(status.favorite_count)

    return favorite_count, retweet_data



def main():
    api = get_twitter_api()
    favorite_data, retweet_data =collectData(api,'@cnnbrk' )
    print(favorite_data[0:20],retweet_data[0:20])

if __name__ == "__main__":
    main()