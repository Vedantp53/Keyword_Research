from http.client import HTTPSConnection
from client import RestClient
import json


username = "vedantpangudwalw@gmail.com"
password = "2c937c8141a7a8f1"

client = RestClient(username, password)

response = client.get("/v3/keywords_data/google_ads/languages")
if response["status_code"] == 20000:
    print(response)
    with open("language_response.json", "w") as json_file:
        json.dump(response, json_file)
else:
    print(
        "error. Code: %d Message: %s"
        % (response["status_code"], response["status_message"])
    )
