import telebot
import requests
import os
from telebot.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
import random
from button_man import (main_menu, other_menu, contact_button,
                        referral_program_button, choose_language_button,
                        Get_Access_Key_button, callback_other_button,
                        app_center_button, referral_program_button_inline)
from text_man import (start_text, get_menu_text, contact_text,
                      referral_program_text,choose_language_text,
                      get_access_key_text,other_operations_text,
                      what_outline_text,why_outline_text,
                      cancel_text,outline_secure_text,why_use_text,
                      how_to_outline_text,app_center_text,
                      price_list_text,quest_text,play_text,
                      about_text,system_status_text)

API_MANMARKET = os.environ.get('API_MANMARKET')
bot = telebot.TeleBot(API_MANMARKET)


# START
@bot.message_handler(commands=['start'])
def start_handler(message):
    '''
    When the start command comes into the bot
    '''
    bot.send_message(
            chat_id=message.chat.id,
            text=start_text,
            reply_markup=main_menu()         
        )

# GET MENU
@bot.message_handler(commands=["get_menu"])
def get_menu_handler(message):
    '''
    When the get_menu command comes in the bot
    '''
    bot.send_message(
        chat_id=message.chat.id,
        text=get_menu_text,
        reply_markup=main_menu()
    )

# CONTACT US
@bot.message_handler(commands=["contact_us"])
def contact_handler(message):
    '''
    When the contact_us command comes in the bot
    '''
    bot.send_message(
        chat_id=message.chat.id,
        text=contact_text(),
        parse_mode="Markdown",
        reply_markup=contact_button()
    )
    
# REFERRAL PROGRAM
@bot.message_handler(commands=['referral_program'])
def referral_program_handler(message):
    '''
    When the referral_program command comes in the bot
    '''
    bot.send_message(
        chat_id=message.chat.id,
        text=referral_program_text,
        parse_mode="Markdown",
        reply_markup=referral_program_button()
    )
    
# CHOOSE LANGUAGE
@bot.message_handler(commands=['choose_language'])
def choose_language_handler(message):
    '''
    When the choose_language command comes in the bot
    '''
    bot.send_message(
        chat_id=message.chat.id,
        text=choose_language_text,
        reply_markup=choose_language_button()
    )
    
# 🖋️دریافت کلید دسترسی
@bot.message_handler(regexp='🖋️دریافت کلید دسترسی$')
def Get_Access_Key_handler(message):
    '''
    When the text 🖋️دریافت کلید دسترسی is written in the bot
    '''
    bot.send_message(
        chat_id=message.chat.id,
        text=get_access_key_text,
        reply_markup=Get_Access_Key_button()
    )
    
# ❓سایر عملیات
@bot.message_handler(regexp="❓سایر عملیات$")
def other_operations_handler(message):
    '''
    When the text ❓سایر عملیات is written in the bot
    '''
    bot.send_message(
        chat_id=message.chat.id,
        text=other_operations_text,
        reply_markup=other_menu()
    )

# CALL BACK QUERY
'''
When callback query requests come in the bot
'''
@bot.callback_query_handler(func=lambda call:True)
def callback_other_handler(call):
    # QUERY WHAT OUTLINE
    if call.data == "what_outline":
        '''
        When callback data was equal to what_outline
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=what_outline_text,
            reply_markup=callback_other_button()
            )
    # QUERY WHY OUTLINE
    elif call.data == "why_outline":
        '''
        When callback data was equal to why_outline
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=why_outline_text,
            reply_markup=callback_other_button()
            )
    # QUERY OUTLINE SECURE
    elif call.data == "outline_secure":
        '''
        When callback data was equal to outline_secure
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=outline_secure_text,
            reply_markup=callback_other_button()
            )
        # QUERY OUTLINE SECURE
    # QUERY WHY USE
    elif call.data == "why_use":
        '''
        When callback data was equal to why_use
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=why_use_text,
            reply_markup=callback_other_button()
            )
    # QUERY HOW TO OUTLINE
    elif call.data == "how_to_outline":
        '''
        When callback data was equal to how_to_outline
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=how_to_outline_text,
            reply_markup=callback_other_button()
            )
    # QUERY APP CENTER
    elif call.data == "app_center":
        '''
        When callback data was equal to app_center
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=app_center_text,
            reply_markup=app_center_button()
            )
    # QUERY PRICE LIST
    elif call.data == "price_list":
        '''
        When callback data was equal to price_list
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=price_list_text,
            reply_markup=callback_other_button()
            )
    # QUERY REFR PEOGRAM
    elif call.data == "refr_program":
        '''
        When callback data was equal to refr_program
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=referral_program_text,
            parse_mode="Markdown",
            reply_markup=referral_program_button_inline()
            )
    # QUERY QUEST
    elif call.data == "quest":
        '''
        When callback data was equal to quest
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=quest_text,
            reply_markup=callback_other_button()
            )
    # QUERY PLAY
    elif call.data == "play":
        '''
        When callback data was equal to play
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=play_text,
            reply_markup=callback_other_button()
            )
    # QUERY ABOUT
    elif call.data == "about":
        '''
        When callback data was equal to about
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=about_text,
            reply_markup=callback_other_button()
            )
    # QUERY SYSTEM STATUS
    elif call.data == "system_status":
        '''
        When callback data was equal to system_status
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=system_status_text,
            reply_markup=callback_other_button()
            )
    # QUERY BACK OTHER
    elif call.data == "back_other":
        '''
        When callback data was equal to back_other
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=get_menu_text,
            reply_markup=other_menu()
            )
    # QUERY CANCEL
    elif call.data == "cancel":
        '''
        When callback data was equal to cancel
        '''
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=cancel_text,
            )



bot.infinity_polling()