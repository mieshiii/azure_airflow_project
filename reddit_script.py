import requests
import pandas as pd
from datetime import date

#for local use
#path = r'C:/Users/mieshiii/Desktop/dev/azure_airflow_project'

def azure_airflow_etl():
  #fetch api creds
  with open("reddit_secret.txt", "r") as creds:
    creds_lines = creds.readlines()

  #fetch reddit account creds
  with open("reddit_account.txt", "r") as account:
    account_lines: list[str] = account.readlines()

  #api creds
  CLIENT_ID: str = creds_lines[0].rstrip()
  CLIENT_SECRET: str = creds_lines[1].rstrip()

  #reddit creds
  REDDIT_USERNAME: str = account_lines[0].rstrip()
  REDDIT_PASSWORD: str = account_lines[1].rstrip()

  #get access token from reddit
  auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

  #setup credentials
  data: dict[str, str] = {
    'grant_type': 'password',
    'username': REDDIT_USERNAME,
    'password': REDDIT_PASSWORD,
  }

  headers = {'User-Agent':  REDDIT_USERNAME + '_Reddit_API/v0.0.1'}
  #token request
  res = requests.post('https://www.reddit.com/api/v1/access_token', 
                      auth=auth, 
                      data=data, 
                      headers=headers)

  #token
  reddit_token = res.json()['access_token']

  #append token to headers
  headers['Authorization'] = f'bearer {reddit_token}'

  #get most hot posts from a subreddit
  reddit = requests.get('https://oauth.reddit.com/r/wallstreetbets/hot', 
                        headers=headers, 
                        params={'limit': '100'}).json()

  reddit_data = pd.DataFrame()

  #build data frame
  for post in reddit['data']['children']:
    reddit_data = reddit_data.append({
      'subreddit': post['data']['subreddit'],
      'unique_id': post['data']['name'],
      'title': post['data']['title'],
      'selftext': post['data']['selftext'],
      'upvote_ratio': post['data']['upvote_ratio'],
      'upvote': post['data']['ups'],
      'downvote': post['data']['downs'],
      'score': post['data']['score'],
      'num_comments': post['data']['num_comments'],
    }, ignore_index=True)

  #write to csv
  df = pd.DataFrame(reddit_data)
  file_name: str = f"wsb_{date.today()}.csv"
  df.to_csv(file_name)