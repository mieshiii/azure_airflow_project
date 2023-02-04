import requests
#fetch api creds
with open("reddit_secret.txt", "r") as creds:
  creds_lines = creds.readlines()


CLIENT_ID: str = creds_lines[0].rstrip()

CLIENT_SECRET: str = creds_lines[1].rstrip()

#fetch reddit account creds
with open("reddit_account.txt", "r") as account:
  account_lines: list[str] = account.readlines()
  
reddit_username: str = account_lines[0].rstrip()
reddit_password: str = account_lines[1].rstrip()

#get access token from reddit
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

#setup credentials
data: dict[str, str] = {
   'grant_type': 'password',
   'username': reddit_username,
   'password': reddit_password,
 }

headers = {'User-Agent':  reddit_username + '_Reddit_API/v0.0.1'}
#token request
res = requests.post('https://www.reddit.com/api/v1/access_token', 
                    auth=auth, 
                    data=data, 
                    headers=headers)

#token
reddit_token = res.json()['access_token']

#append token to headers
headers['Authorization'] = f'bearer {reddit_token}'

#get most popular post from a subreddit
reddit = requests.get('https://oauth.reddit.com/r/wallstreetbets/hot', headers=headers).json()

print(reddit)