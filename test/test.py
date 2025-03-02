import requests

api_token = "e0968073-0a88-43dc-be68-150b91dcf8c5"
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

data = {
    'region_slug' : 'iran'
}
regions_url = "https://api.getoutlinevpn.com/get-locations"
regions_response = requests.get(regions_url, headers=headers,json=data)
regions_data = regions_response.json()
print(regions_data)


