import praw

reddit = praw.Reddit(
    client_id="xmZYPFS6XU-oyA",
    client_secret="SlTDyGWqQK1OrdYQvb1ryWJxGyo",
    username="ipagera",
    password="Ignigeralt123",
    user_agent="one_piece_project",
)

subreddit = reddit.subreddit("onepiece")

hot_python = subreddit.hot(limit=1)

search = subreddit.search(
    "One Piece Chapter 946 Spoilers", sort="relevance", limit=5, time_filter="month"
)


for i in search:
    # print(dir(i))
    # if i == "bxdj12":
    print('Title: ', i.title)
    print('Subreddit: ', i.subreddit)
    print('Submission: ', i)
    # print('Body: ', i.selftext)

#TODO

class SubRedditMain:
    # TODO Think of a new name for class and how it's going to be used
    # in relation to the other classes. 

    """ Main Class of module. Interacts with classes SearchQuery and RedditPost.
    Has a method called search_subreddit which takes an object of SearchQuery and
    performs a search and puts the submissions found in objects of RedditPost. 
    
    
    class variables:
        - Reddit Instance
    
    Object attributes:
        - Subreddit info """


    @staticmethod
    def search_subreddit(query):
        """ Takes query (SearchQuery object) and performs a search of a subreddit
        and puts the results into objects. 
        Find a way to use the hot() and other filters? Maybe in the SearchQuery object? """
    pass

    @staticmethod
    def check_with_db():
        """ Checks post with JSON / Google Sheet DB """
        pass

class SearchQuery:

    pass

class RedditPost:

    pass




