import tweepy 
import pandas as pd
import json
import numpy as np
import emoji
import csv
import regex
#from tweepy import OAuthHandler 
from authorise_app import consumer_key, consumer_secret, access_token, access_secret
import matplotlib.pyplot as plt
from textblob import TextBlob


import re



#class that interacted with twitter directly.
class TwitterClient():

    def __init__(self, twitter_user=None):
            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_secret)
            self.twitter_client = tweepy.API(self.auth, wait_on_rate_limit=True)

            self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_tweets(self,start_ID, end_ID):
        tweets = []
        #start_date = datetime.datetime()

        for tweet in tweepy.Cursor(self.twitter_client.user_timeline, 
                                    id=self.twitter_user, 
                                    since_id=start_ID, max_id=end_ID, tweet_mode="extended").items():
            
            if(tweet.favorite_count > 7000):
                tweets.append(tweet)
        
        return tweets

    ## After researchng I discovered that currently, you can only extrat replies to tweets that are less
        ## than a week old. This meant I had to change the focus of my project.
    '''def find_replies_to_tweets(self, tweets):
        replies = []
        #for tweet in tweets:
        for tweet_replies in tweepy.Cursor(self.twitter_client.search, q='to:{}'.format(self.twitter_user), 
        since_id=1158134107257397248, result_type='popular').items(5):
            for tweet in tweets:
                if hasattr(tweet_replies, 'in_reply_to_status_id'):
                    if(tweet_replies.in_reply_to_status_id_str == tweet.id_str):
                        replies.append(tweet_replies.full_text)


        return replies'''


class TweetAnalyser():

   

    def createDataFrame(self, tweets):
        ##this fucntion creats the dataframe

        df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['tweets'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['created_at'] = np.array([tweet.created_at for tweet in tweets])
        df['emoji_code'] = np.array([tweet_analyser.check_emoji(tweet) for tweet in df['tweets']])
        df['tweet_sentiment'] = np.array([tweet_analyser.analyse_sentiment(tweet) for tweet in df['tweets']])
        return df
    
    def clean_tweet(self, tweet):
        ##fucntion to clean tweet before undergoing sentiment anaylsis 
        # removes all characters but plain text.
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyse_sentiment(self, tweet):
        # Textblob has a sentiment polarity function that I used. 
        # The results were rather inaccurate (see csv file)
        # Potential Idea - Create my own sentiment analysis feature trained on football tweets only?
        analysis = TextBlob(self.clean_tweet(tweet))
        return analysis.sentiment.polarity
        
        
    def check_emoji(self, tweet):
        # function to convert emoji symbol/char into its unicode
        
        # translate and check emoji here
        emoji_list = []
        data = regex.findall(r'\X', tweet)
        senti_df = pd.read_csv('new_sentiment_data.csv')
        for word in data:
            if any(char in emoji.UNICODE_EMOJI for char in word):
                #translate word to unicdoe code
                ##append unicode code to list
                try:
                    uni_code = f'U+{ord(word):X}' 
                    emoji_list.append(uni_code)

                except TypeError:
                    pass

        return emoji_list


#def emoji_translation(self, tweets):
    pass
    '''##create new df of the sentiment row and score
    senti_df = pd.read_csv('new_sentiment_data')
    senti_value = senti_df['sentimentScore']
    emoji_code = senti_df['Unicode_codepoint']
    
    #import tweet csv data
    tweet_file = pd.read_csv('tweet_file.csv')
    ##find a way to iterate through each element in each emoji block per tweet
    #emoji_tweet = tweet_file['emoji']

    ##translate the unicode using f-string
    for tweet in tweets:
        emoji_list = tweet_analyser.check_emoji(tweet)
    



    ##check if that fstring matches emoji_code
    ##if yes, store each translation AND the AVERGAE sentiment score (senti_value) 
        #as their own columns in tweet_csv file
    #find the average of the word sentiment and emoji-sentiment
        #average = final_Sentiment column in tweet_file.

    #print(senti_row)'''




    
    


if __name__ == '__main__': 
  
    twitter_client = TwitterClient('Arsenal')
    tweet_analyser = TweetAnalyser()

    api = twitter_client.get_twitter_client_api()

    tweets = twitter_client.get_user_tweets(1212442388981002240, 1236413003127566337)
    
    df = tweet_analyser.createDataFrame(tweets)

    #df.to_csv('tweet_file.csv')
    #new_df = pd.DataFrame(df.emoji_code.values.tolist()).add_prefix('emoji_')
    #print(new_df)

    '''emoji_col = df['emoji_code'].apply(pd.Series)
    emoji_col = emoji_col.rename(columns = lambda x : 'emoji_' + str(x))
    pd.concat([df[:], emoji_col[:]], axis=1)

    print(df)'''





    


    #print(dir(tweets[0]))

    #print(type(tweet_data))
    #print(tweet_data[4])
