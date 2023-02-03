import requests
#fetch api creds
with open("reddit_secret.txt", "r") as creds:
  creds_lines = creds.readlines()


CLIENT_ID: str = creds_lines[0]

CLIENT_SECRET: str = creds_lines[1]

#fetch reddit account creds
with open("reddit_account.txt", "r") as account:
  account_lines = account.readlines()
  
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

headers = {'User-Agent': 'Test API v0.0.1'}
res = requests.post('', auth=auth, data=data,headers=headers)