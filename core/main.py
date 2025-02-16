import telebot
import os
import pprint
import json

API_TOKEN = os.environ.get('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "سلام! چطور می‌تونم کمکتون کنم؟")


@bot.message_handler(regexp="ali")
def handle_message(message):
	bot.reply_to(message,'alo gay')

# bot.message_handler(content_types=['document','audio'])
# def handler_docs_audio(message):
#     if message.content_type == 'document':
#         bot.reply_to(message,'its a document')
#     elif message.content_type == 'audio':
#         print('its a audio')

bot.infinity_polling()