import requests

url = 'https://www.naver.com'
#요청받은내용 = 요청
reponose = requests.get(url)
print('응답코드 : {}'.format(reponose.status_code))
print(reponose.text)