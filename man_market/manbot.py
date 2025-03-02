import telebot
import requests
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import random

API_MANMARKET = os.environ.get('API_MANMARKET')
bot = telebot.TeleBot(API_MANMARKET)

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Access_Keys = KeyboardButton("🖋️دریافت کلید دسترسی")
    List_Access_Keys = KeyboardButton("📋کلیدهای دسترسی به فهرست")
    markup.add(Access_Keys, List_Access_Keys)
    Chek_Balance = KeyboardButton("💎تعادل را بررسی کنید")
    Payment = KeyboardButton("💳پرداخت")
    markup.add(Chek_Balance,Payment)
    Other_Operations = KeyboardButton("❓سایر عملیات")
    markup.add(Other_Operations)
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

@bot.message_handler(commands=["contact_us"])
def contact_handler(message):
    markup = InlineKeyboardMarkup()
    Live_Support = InlineKeyboardButton('✍️پشتیبانی زنده',callback_data='support')
    markup.add(Live_Support)
    ticket_id = random.randint(10000, 99999)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'اگر به مشکلی برخوردید یا سؤال یا نگرانی دارید، ما همیشه خوشحالیم که به شما کمک کنیم. در هر زمان با ما تماس بگیرید. \n\n کد پشتیبانی شما: `{ticket_id}`',
        parse_mode="Markdown",
        reply_markup=markup
    )
    

@bot.message_handler(commands=['referral_program'])
def referral_program_handler(message):
    markup = InlineKeyboardMarkup()
    Share = InlineKeyboardButton('🔗به اشتراک بگذارید',callback_data='share')
    Referral_Details = InlineKeyboardButton('جزئیات ارجاع',callback_data='referral_details')
    markup.add(Share,Referral_Details)
    Cancel = InlineKeyboardButton('❌لغو',callback_data='cancel')
    markup.add(Cancel)
    bot.send_message(
        chat_id=message.chat.id,
        text='❖ برنامه ارجاع\nکاربران را دعوت کنید و به دلار آمریکا پاداش بگیرید.\n\nبا دعوت از کاربران می توانید جوایز زیر را کسب کنید:\n• 10% کارمزد تمام سپرده های آنها.\n\nبرای دعوت از کاربران از لینک های زیر استفاده کنید\n`https://t.me/Outline_Man_Bot?start`',
        parse_mode="Markdown",
        reply_markup=markup
    )
    
    
@bot.message_handler(commands=['choose_language'])
def choose_language_handler(message):
    markup = InlineKeyboardMarkup()
    Engilsh = InlineKeyboardButton('🇺🇸English',callback_data='english')
    Turkish = InlineKeyboardButton('🇹🇷Turkish',callback_data='turkish')
    markup.add(Engilsh,Turkish)
    Cancel = InlineKeyboardButton('❌لغو',callback_data='cancel')
    markup.add(Cancel)
    bot.send_message(
        chat_id=message.chat.id,
        text='زبان خود را انتخاب کنید',
        reply_markup=markup
    )
    
@bot.message_handler(regexp='🖋️دریافت کلید دسترسی$')
def Get_Access_Key_handler(message):
    markup = InlineKeyboardMarkup()
    Russia = InlineKeyboardButton('🇷🇺روسیه',callback_data='russia')
    Iran = InlineKeyboardButton("🇮🇷ایران",callback_data='iran')
    Ukraine = InlineKeyboardButton('🇺🇦اکراین',callback_data='ukraine')
    China = InlineKeyboardButton('🇨🇳چین',callback_data='china')
    Other_Count = InlineKeyboardButton('🌎کشور های دیگر',callback_data='other_count')
    Cancel = InlineKeyboardButton('❌لغو',callback_data='cancel')
    all_count = [Russia,Iran,Ukraine,China,Other_Count,Cancel]
    for countri in all_count:
        markup.add(countri) 
    bot.send_message(
        chat_id=message.chat.id,
        text='انتخاب کشور محل اقامت:',
        reply_markup=markup
    )
    
@bot.message_handler(regexp="❓سایر عملیات$")
def other_operations_handler(message):
    markup = InlineKeyboardMarkup()
    What_Outline = InlineKeyboardButton('outline VPN چیست❓',callback_data='what_outline')
    Why_Outline = InlineKeyboardButton('❔چرا outline VPN',callback_data='why_outline')
    Outline_Secure = InlineKeyboardButton('❓طرح کلی امن است',callback_data="outline_secure")
    Why_Use = InlineKeyboardButton('❔چرا از VPN استفاده کنید',callback_data="why_use")
    How_To_Outline = InlineKeyboardButton('🛠️نحوه استفاده از Outline VPN',callback_data="how_to_outline")
    App_Center = InlineKeyboardButton('💠مرکز درخواست',callback_data="app_center")
    Trouble = InlineKeyboardButton('🔧عیب یابی',callback_data="trouble")
    all_operator = [
        What_Outline,
        Why_Outline,
        Outline_Secure,
        Why_Use,
        How_To_Outline,
        App_Center,
        Trouble,
    ]
    for operator in all_operator:
        markup.add(operator)
        
    
    Price_List = InlineKeyboardButton('💵لیست قیمت',callback_data="price_list")
    Refr_Program = InlineKeyboardButton('🤝برنامه ارجاع',callback_data="refr_program")
    markup.add(Price_List,Refr_Program)
    Quest = InlineKeyboardButton('🏆تلاش برای عصر',callback_data="quest")
    Play = InlineKeyboardButton('🎮بازی کنید و کسب درآمد کنید',callback_data="play")
    markup.add(Quest,Play)
    About = InlineKeyboardButton("❕در مورد ما",callback_data="about")
    System_Status = InlineKeyboardButton('👁️وضعیت سیستم',callback_data="system_status")
    markup.add(About,System_Status)
    
    
    
    bot.send_message(
        chat_id=message.chat.id,
        text="عملیاتی را که می خواهید انجام دهید انتخاب کنید:",
        reply_markup=markup
    )
    
    
bot.infinity_polling()
