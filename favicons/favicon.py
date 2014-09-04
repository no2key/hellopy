import requests


url = 'http://www.google.com/s2/favicons?domain=google.com'

response = requests.get(url)

print(response.text)

