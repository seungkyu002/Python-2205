import json
with open('cctv (1).json', 'rt', encoding='UTF-8') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)
    kind = set()
    for data in dict_list:
        # print(data['窜加备盒'])
        kind.add(data['窜加备盒'])
    print(kind)