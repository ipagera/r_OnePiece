from common import *
from fuzzywuzzy import fuzz



# TODO Add more extensive documentation with the steps and logic


def main():

    # We set up the subreddit instance we are going to use the generate_search() on

    subreddit = reddit_api_logic.reddit_config.subreddit("onepiece")

    # We generate the seach. Aguments are the "query" + subreddit, the latter already defined above

    results = reddit_api_logic.generate_search(
        "one piece chapter 947 spoilers"
    )

    # We analyze the result and strip the ones that we don't care about
    # by calling the RedditPost.clear_results() method

    results = reddit_post.RedditPost.clear_results(*results)
    results = reddit_post.RedditPost.toJSON(*results)

    # print(results)

    json_db = db_operators.JsonDb('common/posts_db.json')
    
    json_db.add_results(results)
    



    

main()
    


    
    
    
