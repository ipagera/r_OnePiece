
class RedditPost:
    """ Reddit Post Object """

    no_of_posts = 0

    def __init__(self, id, user, created_on, title, body):
        self.id = id
        self.user = user
        self.created_on = created_on
        self.title = title
        self.body = body

    




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

