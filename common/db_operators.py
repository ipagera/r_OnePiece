""" This module stores the logic behind the data storage of
each reddit post. They can be either stored in a JSON or 
Google Sheets. """

import json
import send_email
import re
from fuzzywuzzy import fuzz


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
                body1 = results[key]["body"]
                body2 = json_data[key]["body"]
                if (
                    JsonDb.check_for_update(body1, body2) < 100
                ):  # Cheks if there are any updates between the results and the database
                    JsonDb.new_entry_added(self,results)
                else:
                    print("Results already in DB!")

            else:
                JsonDb.new_entry_added(self,results)

    def new_entry_added(self, new_data):
        
        json_data = self.data

        for key in new_data.keys():
            json_data[key] = new_data[key]
            
        with open(self.file_name, "w") as f:
            json.dump(json_data, f)
            print("Added to DB!")

        print("Email is being sent now!")
        email_frame = Send_Emails.results_in_email(new_data)
        Send_Emails.email_sender(email_frame)

    @staticmethod
    def check_for_update(body1, body2):
        """ Uses fuzzy matching to check the matching ratio the
        body of new result vs body of result in database which matching
        post id."""
        ratio = fuzz.ratio(body1, body2)
        return ratio


class Send_Emails:
    @staticmethod
    def results_in_email(results):

        body_of_email = ""

        for key in results.keys():

            result = results[key]

            body_of_email += f"""
        <strong>ID: </strong>{result['id']}<br>
        <strong>User: </strong>{result['user']}<br>
        <strong>Created on: </strong>{result['created_on']}<br>
        <strong>{result['title']}</strong><br><br>
        {result['body']}<br><br>"""

        email_frame = f""" 
        <!DOCTYPE html>
        <html>
            <body>
                <p><b>Results from the Reddit Search</b></p><br>
                {body_of_email}
            </body>
        </html> """

        # print(email_frame)
        return email_frame

    @staticmethod
    def email_sender(email):
        """ Each time there is a new entry in the Json DB,
        this method is called which calls the email constructor. """

        send_email.send_email(email)

