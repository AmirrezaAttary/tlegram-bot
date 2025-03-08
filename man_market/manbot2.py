import telebot
import sqlite3
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# دریافت توکن بات از متغیر محیطی
API_MANMARKET = os.environ.get('API_MANMARKET')
if not API_MANMARKET:
    raise ValueError("API_MANMARKET is not set. Please configure the environment variable.")

bot = telebot.TeleBot(API_MANMARKET)

# اتصال به دیتابیس و ایجاد جدول کاربران
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        language TEXT DEFAULT 'fa'
    )
""")
conn.commit()

def set_user_language(user_id, lang):
    cursor.execute("INSERT INTO users (user_id, language) VALUES (?, ?) ON CONFLICT(user_id) DO UPDATE SET language = ?", (user_id, lang, lang))
    conn.commit()

def get_user_language(user_id):
    cursor.execute("SELECT language FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 'fa'

# دیکشنری پیام‌ها بر اساس زبان
messages = {
    "welcome": {
        "fa": "به Outline VPN خوش آمدید!",
        "en": "Welcome to Outline VPN!",
        "tr": "Outline VPN'ye hoş geldiniz!"
    },
    "choose_language": {
        "fa": "لطفاً زبان مورد نظر خود را انتخاب کنید:",
        "en": "Please select your preferred language:",
        "tr": "Lütfen tercih ettiğiniz dili seçin:"
    }
}

def main_menu(language):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = {
        "fa": ["🖋️دریافت کلید دسترسی", "📋کلیدهای دسترسی به فهرست", "💎تعادل را بررسی کنید", "🌍 تغییر زبان"],
        "en": ["🖋️Get Access Key", "📋List Access Keys", "💎Check Balance", "🌍 Change Language"],
        "tr": ["🖋️Erişim Anahtarını Al", "📋Erişim Anahtarları Listesi", "💎Bakiye Kontrolü", "🌍 Dili Değiştir"]
    }
    markup.add(*buttons[language])
    return markup

@bot.message_handler(commands=['start'])
def start_handler(message):
    user_id = message.chat.id
    language = get_user_language(user_id)
    bot.send_message(chat_id=user_id, text=messages['welcome'][language], reply_markup=main_menu(language))

@bot.message_handler(regexp='🌍 تغییر زبان|🌍 Change Language|🌍 Dili Değiştir')
def change_language_handler(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(KeyboardButton("🇮🇷 فارسی"), KeyboardButton("🇬🇧 English"), KeyboardButton("🇹🇷 Türkçe"))
    bot.send_message(message.chat.id, messages["choose_language"][get_user_language(message.chat.id)], reply_markup=markup)

@bot.message_handler(regexp='🇮🇷 فارسی|🇬🇧 English|🇹🇷 Türkçe')
def set_language(message):
    lang_map = {"🇮🇷 فارسی": "fa", "🇬🇧 English": "en", "🇹🇷 Türkçe": "tr"}
    lang = lang_map[message.text]
    set_user_language(message.chat.id, lang)
    bot.send_message(message.chat.id, messages['welcome'][lang], reply_markup=main_menu(lang))

bot.infinity_polling()
