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
    def clear_resutls(*args):
        """ To analyze the body of the post and determine if it should join
        the json database.
         """
        validation_list = ['spoiler','SPOILER','Spoiler']

        updated_results = []
        for item in validation_list:
            for arg in args:
                if item in arg.title:
                    updated_results.append(arg)
        
        return updated_results
    

    @staticmethod
    def toJSON(*args):
        """ Parses one or several RedditPost objects
         onto a JSON style data structure dict. """

        json_dict = {}
        for arg in args:
            new_item = json.dumps(arg.__dict__) 
            json_dict[arg.id] = new_item
        
        return json_dict

    



# @staticmethod
# def search_subreddit(query):
#     """ Takes query (SearchQuery object) and performs a search of a subreddit
#     and puts the results into objects.
#     Find a way to use the hot() and other filters? Maybe in the SearchQuery object? """
#     pass

# @staticmethod
# def check_with_db():
#     """ Checks post with JSON / Google Sheet DB """
#     pass

