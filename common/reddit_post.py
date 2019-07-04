""" Module holds the class RedditPost which in conjunction with
module reddit_api_logic is used to initialize results the subreddit search into
objects which we later analyze and put in JSON data structure.  """

import json


class RedditPost:
    """ Reddit Post Object """

    no_of_posts = 0

    def __init__(self, id, user, created_on, title, body):
        self.id = id
        self.user = user
        self.created_on = created_on
        self.title = title
        self.body = body

    def __repr__(self):
        return "{} by {} on {}".format(self.title, self.user, self.created_on)

    @staticmethod
    def clear_results(*args):
        """ To analyze the body of the post and determine if it should join
        the json database.
         """
        validation_list = ["spoiler", "SPOILER", "Spoiler"]

        updated_results = []
        for item in validation_list:
            for arg in args:
                if item in arg.title:
                    updated_results.append(arg)

        if len(updated_results) == 0:
            print("No matching results")
        return updated_results

    @staticmethod
    def toJSON(*args):
        """ Parses one or several RedditPost objects
         onto a JSON style data structure dict. """

        json_dict = {}
        for arg in args:
            arg.__dict__["body"] = "body"  # TODO - Remove line for live version
            new_item = arg.__dict__
            json_dict[arg.id] = new_item

        return json_dict

    @staticmethod
    def results_in_email(updated_results):
        for result in updated_results:
            body_of_email += f""" 
        
        <p>id: {result.id}</p>
        <p>user: {result.user}</p>
        <p>created on: {result.created_on}</p><br>
        <p><b>{result.title}</b></p>
        <p>{result.body}</p><br> """

        email_frame = f""" 
        <!DOCTYPE html>
        <html>
            <body>
                <p><b>Results from the Reddit Search</b></p><br>
                {body_of_email}
            </body>
        </html> """

        return email_frame

