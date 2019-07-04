from common import *

# TODO Add more extensive documentation with the steps and logic


def main():

    # We set up the subreddit instance we are going to use the generate_search() on

    subreddit = reddit_api_logic.reddit_config.subreddit("onepiece")

    # We generate the seach. Aguments are the "query" + subreddit, the latter already defined above

    results = reddit_api_logic.generate_search(
        "one piece chapter 948 spoilers", subreddit=subreddit
    )

    # We analyze the result and strip the ones that we don't care about
    # by calling the RedditPost.clear_results() method

    results = reddit_post.RedditPost.clear_results(*results)

    # The results are put in a new JSON format (i.e. dict)

    print(type(results))

    # data = reddit_post.RedditPost.toJSON(*results)

    # # We import the database of choice

    # json_db = db_operators.JsonDb(".\common\posts_db.json")
    
    # json_db.add_results(data)

    
    
    
    
main()
