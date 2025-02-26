import telebot
from PIL import Image
import io
import os

API_TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


def compress_image(image_file):
    img = Image.open(image_file)
    output = io.BytesIO()
    img.save(output, format="JPEG", quality=40)  
    output.seek(0)  
    return output

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    
    compressed_image = compress_image(io.BytesIO(downloaded_file))
    
    
    bot.send_photo(message.chat.id, compressed_image)


@bot.inline_handler(lambda query: True)  
def query_help(inline_query):
    results = []
    results.append(telebot.types.InlineQueryResultArticle(
        id='1', 
        title="راهنمای ربات", 
        input_message_content=telebot.types.InputTextMessageContent("این ربات عکس‌های شما را فشرده می‌کند.")
        )
    )
    results.append(telebot.types.InlineQueryResultArticle(
        id='2', 
        title="وبسایت ربات", 
        input_message_content=telebot.types.InputTextMessageContent("وبسایت"),
        url="https://bloghamrah.ir"
        )
    )
    results.append(telebot.types.InlineQueryResultArticle(
        id='3',
        title="جوین شدن به ربات",
        input_message_content=telebot.types.InputTextMessageContent("ارسال عکس برای فشرده‌سازی."),
        url="https://t.me/amirreza_test_2_bot"
        )
    )
    
    
    bot.answer_inline_query(inline_query.id,results)





bot.infinity_polling()
