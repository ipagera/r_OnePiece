#! python3

from common import *
from fuzzywuzzy import fuzz


# TODO Add more extensive documentation with the steps and logic


def main():

    # We set up the subreddit instance we are going to use the generate_search() on

    subreddit = reddit_api_logic.reddit_config.subreddit("onepiece")

    # We generate the seach. Aguments are the "query" + subreddit, the latter already defined above

    query_database = search_query.QueryDatabase("common/query_db.json")

    automatic_query = query_database.new_query()

    results = reddit_api_logic.generate_search(automatic_query)

    # We analyze the result and strip the ones that we don't care about
    # by calling the RedditPost.clear_results() method

    results = reddit_post.RedditPost.clear_results(*results)

    if results == False:
        print("Try again later.")
        exit()
    else:

        # We add the new query to the Query Database

        query_database.add_entry(automatic_query)

        # We put the results to a JSON data structure

        results = reddit_post.RedditPost.toJSON(*results)
        # print(results)

        # Results are added to the Posts Database, email is sent to the user

        json_db = db_operators.JsonDb("common/posts_db.json")

        json_db.add_results(results)


if __name__ == "__main__":
    main()
