import requests

# توکن API خود را در اینجا قرار دهید
API_SECRET_TOKEN = 'توکن_API_شما'

# آدرس API
OUTLINE_API_URL = 'https://api.getoutlinevpn.com/get-port-type'

# region_slug مورد نظر خود را در اینجا قرار دهید
region_slug = 'your_region_slug'

# هدرهای درخواست
headers = {
    'Content-Type': 'application/json',
    'X-OUTLINE-BOT-API-SECRET-TOKEN': API_SECRET_TOKEN,
}

# داده‌های درخواست
data = {
    'region_slug': region_slug
}

try:
    # ارسال درخواست POST
    response = requests.post(OUTLINE_API_URL, headers=headers, json=data)

    # بررسی وضعیت پاسخ
    if response.status_code == 200:
        result = response.json()
        if result.get('status'):
            port_types = result.get('port_type', [])
            print('Available port types:')
            for port in port_types:
                print(f"- {port.get('port_type')}")
        else:
            print('Error in response:', result)
    else:
        print(f'HTTP Error: {response.status_code}')
except requests.exceptions.RequestException as e:
    print('Request failed:', e)
