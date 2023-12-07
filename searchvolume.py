from http.client import HTTPSConnection
from client import RestClient
import json


username = "vedantpangudwalw@gmail.com"
password = "2c937c8141a7a8f1"

client = RestClient(username, password)
post_data = dict()
post_data[len(post_data)] = dict(
    keywords=["phone", "iphone", "samsung"],
    date_from="2021-10-29",
    seacrh_partners=True,
)
response = client.post("/v3/keywords_data/google_ads/search_volume/live", post_data)
if response["status_code"] == 20000:
    print(response)
    with open("searchvolume_response.json", "w") as json_file:
        json.dump(response, json_file)
else:
    print(
        "error. Code: %d Message: %s"
        % (response["status_code"], response["status_message"])
    )
