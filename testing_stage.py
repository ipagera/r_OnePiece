import praw

reddit = praw.Reddit(client_id = 'xmZYPFS6XU-oyA',
                    client_secret = 'SlTDyGWqQK1OrdYQvb1ryWJxGyo',
                    username = 'ipagera',
                    password = 'Ignigeralt123',
                    user_agent = 'one_piece_project')

subreddit = reddit.subreddit('onepiece')

hot_python = subreddit.hot(limit=1)

search = subreddit.search("One Piece Chapter 947 Spoilers",sort="relevance",limit=5,time_filter='month')



# for i in search:
#     # print(dir(i))
#     print('Title: ', i.title)
#     print('Subreddit: ', i.subreddit)

subred_attr = [dir(i) for i in search]

print(subred_attr)
