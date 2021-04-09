import asyncpraw

# Yes there are safer ways to do this
# I just don't care
reddit = asyncpraw.Reddit(
    client_id="YXLgxDx5qtQD0Q",
    client_secret="SJEa9_F65OOs4s3b8eDQgoCs-ggAOg",
    user_agent="python:Moxie Bot:v0.1.0 by u/BubbyRoosh"
)

class Link:
    url: str
    title: str
    def __init__(self, url, title):
        self.url = url
        self.title = title

async def get_links(sub, num) -> list[Link]:
    urls = []
    subreddit = await reddit.subreddit(sub)
    async for submission in subreddit.hot(limit=num):
        url = submission.url
        if url.endswith(".jpg") or url.endswith(".png"):
            urls.append(Link(url, submission.title))
    return urls
