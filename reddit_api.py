import praw
import json
import time

# We set up our configuration for Reddit

reddit_config = praw.Reddit(
    client_id="TIxlhxgTa1KR7A",
    client_secret="USPi3dCn19u1gEuD86O3NZFi8Tc",
    username="redonepiece_proj11",
    password="redonepiece_proj11",
    user_agent="one_piece_project",
)

# We create a subreddit object

subreddit = reddit_config.subreddit("onepiece")

 
def search_subreddit(query, sort= 'relevance', limit= 5, time_filter= 'month',subreddit=subreddit):
    """ Takes a subreddit object and generates a search based on the
    arguments one has provided to the function (e.g. query itself, sort and etc.). """

    search = subreddit.search(query, sort, limit, time_filter)


    # for i in search:
    #     print(i._fetch_info())
    #     # if i == "bxdj12":
    #     # print("ID: ", i.id)
    #     # print("Submission: ", i)
    #     # print("User: ", i.author)
    #     # print("Posted: ", i.author)
    #     # print("Subreddit: ", i.subreddit)
    #     # print("Title: ", i.title)
    

    for i in search:
        print(i.title)
        created_time = int(i.created)

    created_time = time.strftime('%Y-%m-%d@%H:%M:%S', time.localtime(created_time))
    print(created_time)
        

    # Unix time epoch conversion function for i.created field
    
    
        

search_subreddit('one piece chapter 947 spoilers')


class RedditPost:
    """ Creates a reddit post object with the attributes:
    - Submission id
    - User
    - Date / timestamp
    - Sub-Reddit
    - Title
    - Body """
    pass


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

