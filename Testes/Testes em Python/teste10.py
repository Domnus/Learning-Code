import requests
response = requests.get("http://api.open-notify.org/astros.json%22")
print(response.status_code)
