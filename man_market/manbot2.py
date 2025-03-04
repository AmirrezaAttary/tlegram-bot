import telebot
import requests
import os
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_MANMARKET = os.environ.get('API_MANMARKET')
if not API_MANMARKET:
    raise ValueError("API_MANMARKET is not set. Please configure the environment variable.")

bot = telebot.TeleBot(API_MANMARKET)

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("🖋️دریافت کلید دسترسی"), 
        KeyboardButton("📋کلیدهای دسترسی به فهرست"),
        KeyboardButton("💎تعادل را بررسی کنید"),
        KeyboardButton("💳پرداخت"),
        KeyboardButton("❓سایر عملیات")
    )
    return markup

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='به Outline VPN خوش آمدید.\n می توانید کلید دسترسی Outline VPN خود را از منوی Get Access Key ایجاد کرده و شروع به استفاده از آن کنید.',
        reply_markup=main_menu()
    )

@bot.message_handler(commands=["get_menu"])
def get_menu_handler(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='عملیاتی را که می خواهید انجام دهید انتخاب کنید:',
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    responses = {
        "what_outline": "❖ Outline VPN چیست؟ \nOutline به هر کسی امکان می‌دهد با اجرای VPN خود با خیال راحت‌تر به اینترنت رایگان و باز دسترسی داشته باشد...",
        "why_outline": "❖ چرا Outline VPN؟ \nOutline یک VPN امن و قابل اعتماد است که به شما کمک می‌کند بدون نگرانی از سانسور به اینترنت متصل شوید.",
        "outline_secure": "❖ آیا Outline VPN امن است؟ \nبله! Outline از رمزنگاری قوی استفاده می‌کند تا اطلاعات شما را محافظت کند.",
        "why_use": "❖ چرا باید از VPN استفاده کنید؟ \nVPN به شما کمک می‌کند بدون نگرانی از ردیابی یا سانسور، آزادانه از اینترنت استفاده کنید."
    }
    if call.data in responses:
        markup = InlineKeyboardMarkup().add(InlineKeyboardButton("برگشت", callback_data="other"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=responses[call.data],
            reply_markup=markup
        )
    elif call.data == "other":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="عملیاتی را که می‌خواهید انجام دهید انتخاب کنید:",
            reply_markup=other_operations_markup()
        )

def other_operations_markup():
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        ("outline VPN چیست❓", "what_outline"),
        ("❔چرا outline VPN", "why_outline"),
        ("❓طرح کلی امن است", "outline_secure"),
        ("❔چرا از VPN استفاده کنید", "why_use"),
        ("🛠️نحوه استفاده از Outline VPN", "how_to_outline"),
        ("💠مرکز درخواست", "app_center"),
        ("🔧عیب یابی", "trouble"),
        ("💵لیست قیمت", "price_list"),
        ("🤝برنامه ارجاع", "refr_program"),
        ("🏆تلاش برای عصر", "quest"),
        ("🎮بازی کنید و کسب درآمد کنید", "play"),
        ("❕در مورد ما", "about"),
        ("👁️وضعیت سیستم", "system_status"),
    ]
    for text, callback in buttons:
        markup.add(InlineKeyboardButton(text, callback_data=callback))
    return markup

@bot.message_handler(regexp='🖋️دریافت کلید دسترسی$')
def get_access_key_handler(message):
    markup = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton('🇷🇺روسیه', callback_data='russia'),
        InlineKeyboardButton("🇮🇷ایران", callback_data='iran'),
        InlineKeyboardButton('🇺🇦اکراین', callback_data='ukraine'),
        InlineKeyboardButton('🇨🇳چین', callback_data='china'),
        InlineKeyboardButton('🌎کشور های دیگر', callback_data='other_count'),
        InlineKeyboardButton('❌لغو', callback_data='cancel')
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='انتخاب کشور محل اقامت:',
        reply_markup=markup
    )

bot.infinity_polling()
