import requests

api_token = "e0968073-0a88-43dc-be68-150b91dcf8c5"
headers = {
    "Content-Type": "application/json",
    "X-OUTLINE-BOT-API-SECRET-TOKEN": api_token
}

def create_access_key():
    data = {
        "plan_id": 29,
        "region_slug": "iran",
        "country_slug": "at",
        "port_type": "tcp"
    }
    url = "https://api.getoutlinevpn.com/create-access-key"
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # بررسی وضعیت پاسخ
        response_data = response.json()
        
        if response_data.get("status"):
            print("کلید دسترسی با موفقیت ایجاد شد:", response_data)
        else:
            print("خطا در ایجاد کلید دسترسی:", response_data.get("message"))
    
    except requests.exceptions.HTTPError as http_err:
        print(f"خطای HTTP رخ داد: {http_err}")
    except Exception as err:
        print(f"خطای عمومی رخ داد: {err}")

# فراخوانی تابع
create_access_key()
