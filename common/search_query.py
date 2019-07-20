from db_operators import JsonDb

json_db = JsonDb("common/posts_db.json")

posts_from_db = {}

for key, value in json_db.data.items():
    posts_from_db[key] = json_db.data[key]["created_on"]


print(posts_from_db)


# TODO

""" 
1. New Database for search queries
2. 
"""