import telebot
import os
from test import re_text_input, feth_caption  

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من یک ربات دانلود ویدئو از آپارات هستم.\n" 
                          "لطفاً لینک ویدئوی موردنظر را ارسال کنید تا آن را دانلود کرده و برای شما ارسال کنم.")

@bot.message_handler(func=lambda message: 'aparat.com/v/' in message.text)
def download_video(message):
    bot.reply_to(message, "در حال پردازش لینک و دانلود ویدئو... لطفاً کمی صبر کنید.")
    
    caption = feth_caption(message.text)

    re_text_input(message.text)
    
    video_path = 'downloaded_video.mp4'
    
    if os.path.exists(video_path):
        with open(video_path, 'rb') as video:
            bot.send_video(message.chat.id, video, reply_to_message_id=message.message_id, caption=caption)
        os.remove(video_path)  
    else:
        bot.reply_to(message, "متأسفم! مشکلی در دانلود ویدئو به وجود آمد.")

bot.infinity_polling()
