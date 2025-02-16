from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

# توکن‌های API
TELEGRAM_BOT_TOKEN = '7622125771:AAHQjUyLIXg3qWIVxzbTcwf4cNqCuiOu37A'
OUTLINE_API_TOKEN = 'b4a35de7-68cb-42df-9cfb-f2d6143f0676'
OUTLINE_API_URL = 'https://api.getoutlinevpn.com/'

# تابع برای ایجاد کلید دسترسی جدید
async def create_access_key():
    headers = {
        'Content-Type': 'application/json',
        'X-OUTLINE-BOT-API-SECRET-TOKEN': OUTLINE_API_TOKEN
    }
    response = requests.post(f'{OUTLINE_API_URL}create-access-key', headers=headers)
    if response.status_code == 200:
        return response.json().get('access_key')
    else:
        return None

# فرمان /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('سلام! به ربات مدیریت Outline VPN خوش آمدید.')

# فرمان /newkey
async def new_key(update: Update, context: CallbackContext) -> None:
    access_key = await create_access_key()
    if access_key:
        await update.message.reply_text(f'کلید دسترسی جدید شما:\n{access_key}')
    else:
        await update.message.reply_text('خطا در ایجاد کلید دسترسی.')

def main():
    # ایجاد اپلیکیشن
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # افزودن هندلرهای فرمان‌ها
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('newkey', new_key))

    # اجرای ربات
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == '__main__':
    main()
