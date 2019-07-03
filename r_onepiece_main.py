from common import *

# TODO Add more extensive documentation with the steps and logic

# We set up the subreddit instance we are going to use the generate_search() on 
subreddit = reddit_api_logic.reddit_config.subreddit('onepiece')


results = reddit_api_logic.generate_search("one piece chapter 945 spoilers",subreddit=subreddit)

results = reddit_post.RedditPost.clear_resutls(*results)

data = reddit_post.RedditPost.toJSON(*results)

print(data)