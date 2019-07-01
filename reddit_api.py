import json
import time

import praw

import reddit_post

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


def generate_search(
    query, sort="relevance", limit=5, time_filter="month", subreddit=subreddit
):
    """ Takes a subreddit object and generates a search based on the
    arguments one has provided to the function (e.g. query itself, sort and etc.). Returns
    a list of searches."""

    search = subreddit.search(query, sort, limit, time_filter)

    searches = []
    for i in search:

        created_on = int(i.created)

        # Unix time epoch conversion function for i.created field

        created_on = time.strftime("%Y-%m-%d@%H:%M:%S", time.localtime(created_on))

        reddit_post_object = reddit_post.RedditPost(
            i.id, i.author, created_on, i.title, i.selftext
        )

        searches.append(reddit_post_object)

    return searches


searches = generate_search("one piece chapter 947 spoilers")
for i in searches:
    print(i.title, i.created_on)

