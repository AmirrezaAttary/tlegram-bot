from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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

def other_menu():
    markup = InlineKeyboardMarkup(row_width=2)
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
    return markup


def contact_button():
    markup = InlineKeyboardMarkup()
    Live_Support = InlineKeyboardButton('✍️پشتیبانی زنده',callback_data='support')
    markup.add(Live_Support)
    return markup

def referral_program_button():
    markup = InlineKeyboardMarkup()
    Share = InlineKeyboardButton('🔗به اشتراک بگذارید',callback_data='share')
    Referral_Details = InlineKeyboardButton('جزئیات ارجاع',callback_data='referral_details')
    markup.add(Share,Referral_Details)
    Cancel = InlineKeyboardButton('❌لغو',callback_data='cancel')
    markup.add(Cancel)
    return markup

def referral_program_button_inline():
    markup = InlineKeyboardMarkup()
    Share = InlineKeyboardButton('🔗به اشتراک بگذارید',callback_data='share')
    Referral_Details = InlineKeyboardButton('جزئیات ارجاع',callback_data='referral_details')
    markup.add(Share,Referral_Details)
    Go_Back = InlineKeyboardButton("برگشت",callback_data="back_other")
    markup.add(Go_Back)
    return markup


def choose_language_button():
    markup = InlineKeyboardMarkup()
    Engilsh = InlineKeyboardButton('🇺🇸English',callback_data='english')
    Turkish = InlineKeyboardButton('🇹🇷Turkish',callback_data='turkish')
    markup.add(Engilsh,Turkish)
    Cancel = InlineKeyboardButton('❌لغو',callback_data='cancel')
    markup.add(Cancel)
    return markup

def Get_Access_Key_button():
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
    return markup

def callback_other_button():
        markup = InlineKeyboardMarkup()
        Go_Back = InlineKeyboardButton("برگشت",callback_data="back_other")
        markup.add(Go_Back)
        return markup
    
def app_center_button():
    markup = InlineKeyboardMarkup()
    Android = InlineKeyboardButton('اندروید',url="https://play.google.com/store/apps/details?id=org.outline.android.client")
    Iphone = InlineKeyboardButton('آیفون/ios',url="https://apps.apple.com/us/app/outline-app/id1356177741")
    markup.add(Android,Iphone)
    Windows = InlineKeyboardButton('ویندوز',url="https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe")
    Mac_OS = InlineKeyboardButton('مک',url="https://apps.apple.com/us/app/outline-secure-internet-access/id1356178125?mt=12")
    markup.add(Windows,Mac_OS)
    Chrom_os = InlineKeyboardButton('کروم',url="https://play.google.com/store/apps/details?id=org.outline.android.client")
    Linux = InlineKeyboardButton('لینوکس',url="https://s3.amazonaws.com/outline-releases/client/linux/stable/Outline-Client.AppImage")
    markup.add(Chrom_os,Linux)
    Android_APK = InlineKeyboardButton('برنامه اندروید',url="https://s3.amazonaws.com/outline-releases/client/android/stable/Outline-Client.apk")
    markup.add(Android_APK)
    Go_Back = InlineKeyboardButton("برگشت",callback_data="back_other")
    markup.add(Go_Back)
    return markup