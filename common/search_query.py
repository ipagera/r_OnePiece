import re
import json
from datetime import datetime
from . import *


class Query:
    def __init__(self, query_text):
        self.query_text = query_text
        self.creation_date = (datetime.now()).timestamp()

    @property
    def chapter_no(self):
        chapter_no = re.findall("\d{2,}", self.query_text)
        for result in chapter_no:
            return result


class QueryDatabase(db_operators.JsonDb):
    """ Class that initializes search query database. It
    helps create automatic queries and it inherits from
    db_operators.JsonDb """

    def __init__(self, filename):
        super().__init__(filename)

    def add_entry(self, query):
        """ Adds a new query to the Query Database """

        # We instatiate the new query as an object of class Query

        new_query = Query(query)

        # current_data = the data in the QueryDatabase we are working with at the moment

        current_data = self.data

        # We add the new entry to the current data dictionary.
        # Key = creation_date (epoch time)
        # Value = query text i.e. the query itself

        current_data[new_query.creation_date] = new_query.query_text

        with open(self.file_name, "w") as f:
            json.dump(current_data, f)
            print("Query was successful. Added to Query Database!")

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

        creation_dates.sort(reverse=True)

        # We initialize the latest query as a Query object

        latest_query = Query(self.data[creation_dates[0]])

        return int(latest_query.chapter_no)

    def new_query(self):
        new_chapter_no = self.latest_chapter + 1
        new_query = f"one piece chapter {new_chapter_no} spoilers"

        return new_query

