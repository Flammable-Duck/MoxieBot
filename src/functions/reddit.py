import asyncpraw
import random

# Yes there are safer ways to do this
# I just don't care
reddit = asyncpraw.Reddit(
    client_id="YXLgxDx5qtQD0Q",
    client_secret="SJEa9_F65OOs4s3b8eDQgoCs-ggAOg",
    user_agent="python:Moxie Bot:v0.1.0 by u/BubbyRoosh and u/wf6er6"
)

class Link:
    url: str
    title: str
    def __init__(self, url, title):
        self.url = url
        self.title = title

async def get_link(amount, cmd):
    urls = []
    async for submission in cmd(limit=amount):
        url = submission.url
        if url.endswith(".jpg") or url.endswith(".png"):
            urls.append(Link(url, submission.title))
    url = None
    if len(urls) > 0:
        url = urls[random.randint(0, len(urls))]
    return url

async def get_hot(sub, amount):
    "Returns a random 'hot' image in <sub>"
    subreddit = await reddit.subreddit(sub)
    return await get_link(amount, subreddit.hot)

async def get_top(sub, amount):
    "Returns a random 'top' image in <sub>"
    subreddit = await reddit.subreddit(sub)
    return await get_link(amount, subreddit.top)
