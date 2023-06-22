import requests

cfToken = input("Enter your Cloudflare bearer token: ")

url = 'https://api.cloudflare.com/client/v4/zones'
headers = {'Authorization': f'Bearer {cfToken}'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("success")
    cfResponse = response.json()
    for item in cfResponse['result']:
        print(" " + item['name']) 
else:
    print(f"Error: {response.status_code}")

domainList = input("Copy the domains you want to update and put them in the file domainList.txt. When you have copied the domains to the file and saved type 'Y': ")

reqPath = input("Paste the request path of the desired  API call from https://developers.cloudflare.com/api eg (https://api.cloudflare.com/client/v4/zones/{zone_identifier}/settings/http2): ") 
reqMethod = input("what is the request type? (eg post, patch, delete):")

print("Add the request body to the reqBody.txt file")

with open("reqBody.txt", "r") as file:
    reqBody = file.read()

with open("domainList.txt", "r") as f:
    domainList = [line.strip() for line in f]

for domain in domainList:
    for item in cfResponse['result']:
        if item['name'] == domain:
            zoneId = item['id']
            newPath = reqPath.replace("{zone_identifier}", zoneId)

            url = f"{newPath}"
            headers = {'Authorization': f'Bearer {cfToken}'}

            if reqMethod == "POST":
                response = requests.post(url, headers=headers, data=reqBody)
            elif reqMethod == "PATCH":
                response = requests.patch(url, headers=headers, data=reqBody)
            elif reqMethod == "DELETE":
                response = requests.delete(url, headers=headers, data=reqBody)

            if response.status_code == 200:
                print("success")
            else:
                print(f"Error: {response.status_code}")

print("API calls complete")
