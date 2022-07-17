import json

dict_list = [
    {'menu_no':1,'menu_name':'김밥','price':2500},
    {'menu_no':2,'menu_name':'라면','price':3000},
    {'menu_no':3,'menu_name':'제육덮밥','price':8500},
    {'menu_no':4,'menu_name':'떡볶이','price':3500}
]

json_str = json.dumps(dict_list)
print(json_str)
with open('menu.json','wt',encoding='UTF-8') as file:
    file.write(json_str)
print('json 파일이 생성되었습니다.')

# mune.json을 열어서 모든 내용을 출력
with open('menu.json','rt',encoding='UTF-8') as file:
    json_reader = file.read()
    read_list = json.loads(json_reader)
    print(read_list)