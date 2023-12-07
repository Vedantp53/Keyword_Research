from http.client import HTTPSConnection
from client import RestClient
import json


username = "vedantpangudwalw@gmail.com"
password = "2c937c8141a7a8f1"

client = RestClient(username, password)

post_data = dict()

response = client.get("/v3/keywords_data/google_ads/locations")
if response["status_code"] == 20000:
    print(response)
    # do something with result
    with open("getcounties_response.json", "w") as json_file:
        json.dump(response, json_file)
else:
    print(
        "error. Code: %d Message: %s"
        % (response["status_code"], response["status_message"])
    )
