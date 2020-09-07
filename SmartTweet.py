# import des librairies
import requests
import pandas as pd
import json

bearertoken = 'AAAAAAAAAAAAAAAAAAAAAOuOHQEAAAAAdCYvOyCRPFuDaYlZisar99fsn54%3D1fYrjnxRipezCSHCme16XF2AySm2tdTliwEH0hcRb016C01KvN'
produit = 'ps5'
hashtag = '%23'+produit


url = f"https://api.twitter.com/2/tweets/search/recent?max_results=100&query={hashtag}"

payload = {}
headers = {
  'Authorization': f'Bearer {bearertoken}',
}

response = requests.request("GET", url, headers=headers, data = payload).json()
df = pd.json_normalize(response['data']).set_index('id')

for i in range(50) :
    if response['meta']['result_count'] == 100 :
        next_token = response['meta']['next_token']
        url = f"https://api.twitter.com/2/tweets/search/recent?max_results=100&next_token={next_token}&query={hashtag}"
        response = requests.request("GET", url, headers=headers, data = payload).json()
        nextdf = pd.json_normalize(response['data']).set_index('id')
        df = pd.concat([df,nextdf])
    else :
        break

print (df.head())
print (df.shape)






