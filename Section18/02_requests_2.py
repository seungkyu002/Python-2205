import requests

url = 'https://search.naver.com/search.naver'
param = {'query' : '장마'}
response = requests.get(url,param)
print(response.text)