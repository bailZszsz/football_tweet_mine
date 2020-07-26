import csv
import pandas as pd

##create new csv file
def write_to_csv():
    emoji_data = pd.read_csv('emoji_sentiment_data.csv')

    df_new = emoji_data.loc[:,['emoji_code', 'Occurrences', 'Negative', 'Positive']]
    #['Unicode codepoint', 'Occurrences', 'Negative', 'Positive']
    df_new.to_csv("new_sentiment_data.csv", index=False)

    #1,2,4,6

def sentimentCalculator():
    # function to find the sentiment of each emoji based on :
    # total occurrence (of emoji) / no. of positive (or negative) uses.
    senti_df = pd.read_csv('new_sentiment_data.csv')

    senti_df['positive_pc'] = senti_df.Positive/senti_df.Occurrences
    senti_df['negative_pc'] = senti_df.Negative/senti_df.Occurrences
    sentimentScore = (-1*senti_df.negative_pc) + (1*senti_df.positive_pc)

    senti_df['sentimentScore'] = sentimentScore
    cols=['positive_pc','negative_pc','sentimentScore']
    senti_df[cols] = senti_df[cols].round(3)
    
    #df.round(3)
    
    print([senti_df['sentimentScore']]) 
    #print(df)
    senti_df.to_csv("new_sentiment_data.csv", index=False)
    #return senti_df

def analyse_emoji():

    df = pd.read_csv('tweet_file.csv')
    senti_df = pd.read_csv('new_sentiment_data.csv')
    #new_df = pd.DataFrame(df.emoji_code.values.tolist()).add_prefix('emoji_')
    #print(df['emoji_code'][1])


        

#sentimentCalculator()
#emoji_translation()


analyse_emoji()