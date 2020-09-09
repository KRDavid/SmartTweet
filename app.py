import tweepy
import csv
import pandas as pd
####input your credentials here
api_key = 'wvmPoGr45XpkjlXnkc5XVqoTG'
api_secret = 'vuyFTIw16n3ZpItONp26qNVU1PAfJ9HvKAMy9uhRFWBkfCoNWY'
access_token = '1301583918056050688-GfRQOc1N6OroeuMAfEHQbLN96Y89CB'
access_token_secret = 'sS65Y8W0iA1fmODF0YODm2Q8ohLnYuiDYQcZM6sBQ2bPi'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('comments.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#PowerYourBreakthrough",count=100,lang="en").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])