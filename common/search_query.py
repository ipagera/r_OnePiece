from datetime import datetime
from db_operators import JsonDb


json_db = JsonDb("common/posts_db.json")

posts_from_db = {}

for key, value in json_db.data.items():
    posts_from_db[key] = json_db.data[key]["created_on"]


# print(posts_from_db)


# TODO

""" 
1. New Database for search queries
2. 
"""

class Query:

    def __init__(self, query_text):
        self.query_text = query_text
        self.creation_date = (datetime.now()).timestamp()

class QueryDb(JsonDb):
    """ Class that initializes search query database. It
    helps create automatic queries and it inherits from
    db_operators.JsonDb """

    def __init__(self, filename):
        super().__init__(filename)
        


    def add_entry(self, data):
        pass





test_query1 = Query('one piece chapter 948 spoilers')


query_db = QueryDb('common/query_db.json')

