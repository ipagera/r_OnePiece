import json

with open("common/posts_db.json",'r') as f:
    data =json.load(f)

    data['varna'] = 'varna'

    print(data['varna'])
