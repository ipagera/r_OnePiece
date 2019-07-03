""" This module stores the logic behind the data storage of
each reddit post. They can be either stored in a JSON or 
Google Sheets. """

import json

class JsonDb:
    """ Class of Json Database objects. """

    def __init__(self, file_name):
        self.file_name = file_name

    
    @property
    def data(self):
        """ Holds the data of the JsonDb object """
        with open(self.file_name,'r') as f:
            data = json.load(f)
        return data


    def add_results(self,results):
        """ Opens our RedditPosts JSON database and checks if
        the results (that's the dict) we have are there, if not it adds them. """

        # We add all reddit posts which are not in our DB. We
        # check if a post from results is in the DB based on ID
        # ID = key 

        for key in results.keys():
            if key in self.data.keys():
                print("{} already in DB!".format(key))
            else:
                self.data[key] = results[key]
                print("Added to DB!")
        # We overwrite the json db with the new data appended to the old

        with open('posts_db.json','w') as f:
            json.dump(self.data,f)
        print('New entry added to database!')

