import requests

api_token = "c9a43188-24d9-4ed4-b14a-b40a1e79f35e"
headers = {
    "Content-Type": "application/json",
    "X-OUTLINE-BOT-API-SECRET-TOKEN": api_token
}
def get_regin():
    regions_url = "https://api.getoutlinevpn.com/get-regions"
    regions_response = requests.get(regions_url, headers=headers)
    regions_data = regions_response.json()["regions_of_residence"]
    for i in regions_data:
        print(i["region_slug"])
        print(i["region_name"])
        print("************************")

def get_port():
    data = {
        'region_slug' : 'iran'
    }
    regions_url = "https://api.getoutlinevpn.com/get-port-type"
    regions_response = requests.get(regions_url, headers=headers,json=data)
    regions_data = regions_response.json()['port_type']
    for port in regions_data:
        print(port["port_type"])


def get_location():
    data = {
        'region_slug' : 'iran'
    }
    regions_url = "https://api.getoutlinevpn.com/get-locations"
    regions_response = requests.get(regions_url, headers=headers,json=data)
    regions_data = regions_response.json()['outline_locations']
    for location in regions_data:
        print("*************************************************")
        print(location["country_name"] , "--",location["country_slug"])

def get_plan():
    data = {
        'region_slug' : 'iran'
    }
    regions_url = "https://api.getoutlinevpn.com/get-plan-list"
    regions_response = requests.get(regions_url, headers=headers,json=data)
    regions_data = regions_response.json()['outline_plans']
    for plan in regions_data:
        print(plan["plan_id"],"--",plan["period"],'--',plan['period_unit'],"--",plan["bandwidth"],"--",plan["price"],"--",plan["currency"])
        
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
        
# create_access_key()


def list_access_keys():
    regions_url = "https://api.getoutlinevpn.com/list-access-keys"
    regions_response = requests.get(regions_url, headers=headers)
    regions_data = regions_response.json()
    print(regions_data)


def get_access_key():
    data = {
        "access_key_name":"8295d7ede8"
    }
    regions_url = "https://api.getoutlinevpn.com/get-access-key"
    regions_response = requests.get(regions_url, headers=headers,json=data)
    regions_data = regions_response.json()
    print(regions_data)
# get_access_key()