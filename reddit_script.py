import requests
#fetch creds
with open("reddit_secret.txt", 'r') as read:
  lines = read.read()


CLIENT_ID: str = lines[0]

CLIENT_SECRET: str = lines[1]

print(CLIENT_SECRET)

#get access token from reddit
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

#setup credentials
data: dict[str, str] = {
  'grant_type': 'password',
  'username': '',
  'password': '',
}

headers = {'User-Agent': 'Test API v0.0.1'}
res = requests.post('', auth=auth, data=data,headers=headers)