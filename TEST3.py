import requests

api_token = "e0968073-0a88-43dc-be68-150b91dcf8c5"
headers = {
    "Content-Type": "application/json",
    "X-OUTLINE-BOT-API-SECRET-TOKEN": api_token
}

# مرحله 1: دریافت region_slug
regions_url = "https://api.getoutlinevpn.com/get-regions"
regions_response = requests.get(regions_url, headers=headers)
if regions_response.status_code == 200:
    regions_data = regions_response.json()
    print(regions_data)
    # انتخاب اولین region_slug موجود
    region_slug = regions_data['regions_of_residence'][0]['region_slug']
    print(f"Region Slug: {region_slug}")
else:
    print(f"خطا در دریافت regions: {regions_response.status_code}")
    print(regions_response.text)
    exit()

# مرحله 2: دریافت مکان‌ها با استفاده از region_slug
locations_url = "https://api.getoutlinevpn.com/get-locations"
payload = {"region_slug": region_slug}
locations_response = requests.post(locations_url, headers=headers, json=payload)
if locations_response.status_code == 200:
    locations_data = locations_response.json()
    print("Locations:")
    for location in locations_data['outline_locations']:
        print(f"- {location['country_name']} ({location['country_slug']})")
else:
    print(f"خطا در دریافت locations: {locations_response.status_code}")
    print(locations_response.text)
