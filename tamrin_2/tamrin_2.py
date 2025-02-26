import telebot
import requests
import os

# توکن ربات تلگرام خود را وارد کنید
TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# تابعی برای ارسال پیام توضیحات اولیه
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
                  "سلام! من یک ربات هستم که می‌توانم ویدئوهای آپارات را دانلود کرده و در اینجا برای شما ارسال کنم.\n"
                  "برای استفاده از من، لطفاً لینک ویدئو آپارات را ارسال کنید.")

# تابعی برای دانلود ویدئو از آپارات (این مثال فقط یک لینک فرضی است)
def download_video(url):
    # در اینجا باید روش مناسبی برای استخراج لینک دانلود ویدئو از آپارات بنویسید
    # برای سادگی، فرض می‌کنیم لینک مستقیم برای دانلود ویدئو موجود است
    response = requests.get(url)
    
    # ذخیره ویدئو در فایل
    video_path = 'downloaded_video.mp4'
    with open(video_path, 'wb') as f:
        f.write(response.content)
    
    return video_path

# تابعی برای دریافت لینک ویدئو و ارسال آن به کاربر
@bot.message_handler(func=lambda message: True)
def handle_video_link(message):
    video_url = message.text  # لینک ویدئویی که کاربر ارسال کرده است
    
    # دانلود ویدئو
    video_path = download_video(video_url)
    
    # ارسال ویدئو به کاربر به صورت reply
    with open(video_path, 'rb') as video_file:
        bot.reply_to(message, "نام ویدئو: downloaded_video.mp4", reply_to_message_id=message.message_id)
        bot.send_video(message.chat.id, video_file, reply_to_message_id=message.message_id)
    
    # حذف فایل ویدئو بعد از ارسال
    os.remove(video_path)

# شروع ربات
bot.polling()
