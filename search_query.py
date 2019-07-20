import re
import json
from datetime import datetime
from common import *


json_db = db_operators.JsonDb("common/posts_db.json")

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

    @property
    def chapter_no(self):
        chapter_no = re.findall('\d{2,}',self.query_text)
        for result in chapter_no:
            return result

class QueryDatabase(db_operators.JsonDb):
    """ Class that initializes search query database. It
    helps create automatic queries and it inherits from
    db_operators.JsonDb """

    def __init__(self, filename):
        super().__init__(filename)
        
    @staticmethod
    def new_query(query_text):
        query = Query(query_text)
        return query

    def add_entry(self, query):
        """ Adds a new query to the Query Database """
        with open("common/query_db.json",'w') as f:
            pass

    @property
    def latest_chapter(self):
        """ Reads the database and returns the most the most recent 
        chapter number """

        # List of queries' creation dates for filtering purposes.
        # We need the most recent date.

        creation_dates = [] 
        for key in self.data:
            creation_dates.append(key)
        
        # Sorting the list

        creation_dates.sort(reverse = True)

        # We initialize the latest query as a Query object

        latest_query = Query(self.data[creation_dates[0]])

        return int(latest_query.chapter_no)


    def new_query(self):
        new_chapter_no = self.latest_chapter + 1
        new_query = f"one piece chapter {new_chapter_no} spoilers"

        return new_query

    

        
        
        

QUERY_DB = QueryDatabase('common/query_db.json')



test_query1 = Query('one piece chapter 948 spoilers')





# print(query_db.latest_chapter)
# print(query_db.new_query())


