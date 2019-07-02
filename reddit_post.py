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
    def toJSON(*args):
        """ Parses one or several RedditPost objects
         onto a JSON style data structure dict. """

        posts_json = {}
        for arg in args:
            posts_json[arg.id] = {
                "id": arg.id,
                "user": arg.user,
                "created_on": arg.created_on,
                "title": arg.title,
                "body": "arg.body",
            }

        return posts_json


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

