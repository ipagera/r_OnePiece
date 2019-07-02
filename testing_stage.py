import praw

reddit = praw.Reddit(
    client_id="TIxlhxgTa1KR7A",
    client_secret="USPi3dCn19u1gEuD86O3NZFi8Tc",
    username="redonepiece_proj11",
    password="redonepiece_proj11",
    user_agent="one_piece_project",
)

subreddit = reddit.subreddit("onepiece")

hot_python = subreddit.hot(limit=1)

query = subreddit.search(
    "One Piece Chapter 949 Spoilers", sort="relevance", limit=5, time_filter="month"
)


for i in query:
    print(i in query == True)

