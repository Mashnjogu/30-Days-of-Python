import requests

url = "https://android-developers.googleblog.com/2022/11/leading-health-and-fitness-apps-roll-out-health-connect-integrations.html"

response = requests.get(url) #opening a network and fetching data
print(response)
print(response.status_code)
print(response.headers)
print(response.text)

