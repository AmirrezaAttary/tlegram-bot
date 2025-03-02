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

get_location()
