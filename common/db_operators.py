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
        with open(self.file_name, "r") as f:
            data = json.load(f)
        return data

    def add_results(self, results):
        """ Opens our RedditPosts JSON database and checks if
        the results (that's the dict) we have are there, if not it adds them. """

        # We add all reddit posts which are not in our DB. We
        # check if a post from results is in the DB based on ID
        # ID = key

        json_data = self.data

        for key in results.keys():
            if key in json_data.keys():
                print("Results already in DB!".format(key))
                JsonDb.new_entry()
            else:

                json_data[key] = results[key]

                # We overwrite the json db with the new data appended to the old

                with open(self.file_name, "w") as f:
                    json.dump(json_data, f)

    @staticmethod
    def new_entry():
        """ Each time there is a new entry in the Json DB,
        this method is called which calls the email constructor. """
        print("Send email!")

