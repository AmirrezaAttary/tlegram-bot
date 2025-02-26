import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton
import random
import os

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# دکمه‌های اصلی
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton("📞 ارتباط مستقیم با ما")
    btn2 = KeyboardButton("📝 ثبت مشکل")
    markup.add(btn1, btn2)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "به ربات پشتیبانی خوش آمدید. لطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda message: message.text == "📞 ارتباط مستقیم با ما")
def contact_info(message):
    markup = InlineKeyboardMarkup()
    btn_tel = InlineKeyboardButton('09330570810',callback_data='tel')
    btn_phone = InlineKeyboardButton('0214442808',callback_data='phone')
    markup.add(btn_tel,btn_phone)
    bot.send_message(
        message.chat.id,
        "📌 برای ارتباط مستقیم با ما می‌توانید با شماره‌های پشتیبانی زیر تماس بگیرید:",reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "📝 ثبت مشکل")
def request_issue(message):
    bot.send_message(
        message.chat.id,
        "❗ لطفاً مشکل خود را وارد نمایید:"
    )
    bot.register_next_step_handler(message, save_issue)

def save_issue(message):
    ticket_id = random.randint(10000, 99999)
    bot.send_message(
        message.chat.id,
        f"✅ کارشناسان ما در اسرع وقت با شما تماس خواهند گرفت.\n"
        f"📌 شماره پیگیری تیکت: <b>{ticket_id}</b>",
        parse_mode="HTML"
    )

bot.infinity_polling()
