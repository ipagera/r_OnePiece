""" This module holds the our logic for using the reddit api and praw.
1. We initialize the Reddit and Subreddit instances
2. We generate searches with the generate_search() function. """


import json
import time

import praw

import reddit_post

# We set up our configuration for our Reddit instance and Sub reddit instance

reddit_config = praw.Reddit(
    client_id="TIxlhxgTa1KR7A",
    client_secret="USPi3dCn19u1gEuD86O3NZFi8Tc",
    username="redonepiece_proj11",
    password="redonepiece_proj11",
    user_agent="one_piece_project",
)

subreddit = reddit_config.subreddit("onepiece")


def generate_search(
    query, sort="relevance", limit=5, time_filter="month", subreddit=subreddit
):
    """ Takes a subreddit object and generates a search based on the
    arguments one has provided to the function (e.g. query itself, sort and etc.). Returns
    a list of RedditPost objects."""

    # We call the search() method on the subreddit instance
    # and store that in a variable to traverse later wtih the for loop

    search = subreddit.search(query, sort, limit, time_filter)

    # We create the empty results list and start a for loop to
    # traverse the search generator

    results = []

    for i in search:

        created_on = int(i.created)

        # Unix time epoch conversion function for i.created field

        created_on = time.strftime("%Y-%m-%d@%H:%M:%S", time.localtime(created_on))

        # Each time we go through the loop we initiate a RedditPost object

        reddit_post_object = reddit_post.RedditPost(
            i.id, str(i.author), created_on, i.title, i.selftext
        )

        # We append each and every object to our list of results

        results.append(reddit_post_object)

    return results

    # TODO Have a check if the list searches is empty. If it is empty do not build a conditional
    # that does not append the result of the list (which)


results = generate_search("one piece chapter 945 spoilers")

data = reddit_post.RedditPost.toJSON(*results)

data = json.dumps(data, indent=2,)

print(data)