# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gowthamdevops176.atlassian.net/rest/api/3/project"

API_TOKEN = ""

auth = HTTPBasicAuth("gowthamdevops176@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
# Convert json to dictionary using "json.loads"
output = json.loads(response.text)
name = output[0]["name"]
print(name)
