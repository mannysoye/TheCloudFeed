import tweepy
import praw
import os
from random import choice
from dotenv import load_dotenv 
from requests import get
from io import BytesIO
from PIL import Image
import schedule
import time

# load environment variables from .env file
load_dotenv()

# set up reddit client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

# set up twitter client
auth = tweepy.OAuthHandler(
    os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET")
)
auth.set_access_token(
    os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)
api = tweepy.API(auth)

# list of subreddits to randomly select from
subreddit_list = [
    "aww",
    "pics",
    "gifs",
    "funny",
    "videos",
    "memes",
]

# function to post an image to twitter
def post_image(image_path, title, subreddit):
    api.update_with_media(image_path, f"{title} from r/{subreddit}")

# function to run the bot
def run_bot():
    # pick a random subreddit from the list
    subreddit = choice(subreddit_list)

    # get the top 3 posts from the subreddit
    for post in reddit.subreddit(subreddit).hot(limit=3):
        if post.is_self:
            continue
        if post.url.endswith(".jpg") or post.url.endswith(".png"):
            # open the image and post it to twitter
            img = Image.open(BytesIO(get(post.url).content))
            img_path = f"temp/{post.id}.jpg"
            img.save(img_path)
            post_image(img_path, post.title, subreddit)

# run the bot every day at 1 am, 10 am, 10 pm, 1 pm
# using the heroku scheduler add-on

def schedule_bot():
    schedule.every().day.at("1:00").do(run_bot)
    schedule.every().day.at("10:00").do(run_bot)
    schedule.every().day.at("22:00").do(run_bot)
    schedule.every().day.at("13:00").do(run_bot)
    while True:
        schedule.run_pending()
        time.sleep(60) # wait one minute

if __name__ == "__main__":
    schedule_bot()


