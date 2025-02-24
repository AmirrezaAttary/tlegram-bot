# import telebot
# import os
# import pprint
# import logging
# import json

# logger = telebot.logger
# telebot.logger.setLevel(logging.INFO)

# API_TOKEN = os.environ.get('API_TOKEN')

# bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	pprint.pprint(message.__dict__,width=4)
#     # bot.reply_to(message, "سلام! چطور می‌تونم کمکتون کنم؟")


# @bot.message_handler(regexp="ali")
# def handle_message(message):
# 	bot.reply_to(message,'alo gay')

# # Handles all sent documents and audio files
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     if message.content_type == 'document':
#         print('its a document')
#     elif message.content_type == 'audio':
#         print('its a audio')

# bot.infinity_polling()

# import telebot
# from telebot import types
# import os

# API_TOKEN = os.environ.get('API_TOKEN')
# bot = telebot.TeleBot(API_TOKEN)

# # ایجاد یک کیبورد پاسخ با دو گزینه: "دستور اول" و "دستور دوم"
# keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,input_field_placeholder='وارد کن',one_time_keyboard=True,)
# button1 = types.KeyboardButton("دستور اول")
# button2 = types.KeyboardButton("دستور دوم")
# keyboard.add(button1, button2)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "سلام! یکی از دستورات زیر را انتخاب کنید:", reply_markup=keyboard)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text, reply_markup=keyboard)

# # شروع گوش دادن به درخواست‌ها
# bot.infinity_polling()



import telebot
from telebot import types
import os

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# تعریف دکمه‌های کیبورد درون خطی
def create_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="گزینه یک", callback_data="option1")
    button2 = types.InlineKeyboardButton(text="گزینه دو", callback_data="option2")
    button3 = types.InlineKeyboardButton(text="گزینه سه", callback_data="option3")
    keyboard.add(button1, button2, button3)
    return keyboard

# دستور استارت
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! لطفاً یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=create_inline_keyboard())

# پاسخ به انتخاب‌های کاربر با استفاده از callback_query_handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "option1":
        bot.answer_callback_query(call.id, "شما گزینه یک را انتخاب کردید.")
        # ارسال دوباره کیبورد با گزینه‌های جدید
        new_keyboard = types.InlineKeyboardMarkup()
        button4 = types.InlineKeyboardButton(text="گزینه چهار", callback_data="option4")
        button5 = types.InlineKeyboardButton(text="گزینه پنج", callback_data="option5")
        new_keyboard.add(button4, button5)
        bot.send_message(call.message.chat.id, "حالا یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=new_keyboard)
    elif call.data == "option2":
        bot.answer_callback_query(call.id, "شما گزینه دو را انتخاب کردید.")
    elif call.data == "option3":
        bot.answer_callback_query(call.id, "شما گزینه سه را انتخاب کردید.")
    elif call.data == "option4":
        bot.answer_callback_query(call.id, "شما گزینه چهار را انتخاب کردید.")
    elif call.data == "option5":
        bot.answer_callback_query(call.id, "شما گزینه پنج را انتخاب کردید.")

# شروع گوش دادن به درخواست‌ها
bot.infinity_polling()