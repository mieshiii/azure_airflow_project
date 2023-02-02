import requests
#fetch creds
with open("reddit_secret.txt", "r") as read:
  creds_lines = read.read()


CLIENT_ID: str = creds_lines[0]

CLIENT_SECRET: str = creds_lines[1]

with open("reddit_account.txt", "r") as read:
  account_lines = read.read()
  
reddit_username: str = account_lines[0]
reddit_password: str = account_lines[1]

#get access token from reddit
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

#setup credentials
data: dict[str, str] = {
  'grant_type': 'password',
  'username': reddit_username,
  'password': reddit_password,
}

print(reddit_username)
headers = {'User-Agent': 'Test API v0.0.1'}
res = requests.post('', auth=auth, data=data,headers=headers)