#! python3

from common import *
from fuzzywuzzy import fuzz


SUBREDDIT = reddit_api_logic.reddit_config.subreddit("onepiece")
QUERY_DATABASE = search_query.QueryDatabase("common/query_db.json")
POSTS_DATABASE = db_operators.JsonDb("common/posts_db.json")


def main(
    SUBREDDIT=SUBREDDIT, QUERY_DATABASE=QUERY_DATABASE, POSTS_DATABASE=POSTS_DATABASE
):
    """ The main controler of this series of scripts. """

    # First we assume that we are in the start of the next week and make a search with the new query
    # i.e. looking for the new chapter spoilers.

    results = first_search()

    # If there are no results from the first search, we make the second search and reassign the results to that output

    if results == False:
        results = second_search()

    # We put the results to a JSON data structure

    results = reddit_post.RedditPost.toJSON(*results)
    # print(results)

    # Results are added to the Posts Database, email is sent to the user

    json_db = db_operators.JsonDb("common/posts_db.json")

    json_db.add_results(results)


def first_search(subreddit=SUBREDDIT, query_db=QUERY_DATABASE, posts_db=POSTS_DATABASE):
    """ Assumes this is the start of the new week and makes a search with the
    new query:
    1. Opens the query_db and checks the most recent query and modifies it (adds 1 to the chapter number)
    to create the new query.
    2. Makes a search.
    3. If there are no results - returns False
    4. Else - returns the results. 
     """

    query = query_db.new_query()

    results = reddit_api_logic.generate_search(query)

    results = reddit_post.RedditPost.clear_results(*results)
    
    

    if results == False:
        return False
    else:
        # If there are results - add entry to the query database

        query_db.add_entry(query)

        print(results)

        return results


def second_search(
    subreddit=SUBREDDIT, query_db=QUERY_DATABASE, posts_db=POSTS_DATABASE
):
    """ This search is performed when the first search fails because:
    1. It's found already the results for the current week.
    2. The results for the current week have not been generated yet.
    
    *** IT HELPS TO GET UPDATES FROM THE SPOILER POST """

    query = query_db.old_query()

    print('The new chapter spoilers have not been released yet.', 
    '\nTrying to see if there are updates on the old ones')

    results = reddit_api_logic.generate_search(query)

    results = reddit_post.RedditPost.clear_results(*results)

    return results


if __name__ == "__main__":
    main()
