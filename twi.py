import requests
url = 'https://developer.twitter.com/en/docs/twitter-api'
response = requests.post(url)
print(response.json())