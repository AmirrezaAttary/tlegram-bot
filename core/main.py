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
