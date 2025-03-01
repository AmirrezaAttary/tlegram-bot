import time
import feedparser
import telebot
import os

# تنظیمات ربات
TOKEN = os.environ.get('API_TOKEN')
CHANNEL_ID = "@amirreza_test_bot_1"
RSS_URL = "https://thealibigdeli.ir/blog/feed/rss"  

bot = telebot.TeleBot(TOKEN)
latest_post_link = None  

def get_latest_post():
    global latest_post_link
    feed = feedparser.parse(RSS_URL)
    if not feed.entries:
        return None
    
    latest_entry = feed.entries[0]
    if latest_entry.link == latest_post_link:
        return None  
    
    latest_post_link = latest_entry.link  
    return f"📢 {latest_entry.title}\n{latest_entry.link}"

def send_latest_post():
    post = get_latest_post()
    if post:
        bot.send_message(CHANNEL_ID, post)

if __name__ == "__main__":
    while True:
        send_latest_post()
        time.sleep(600)  
