import requests
import datetime
import os 
from dotenv import load_dotenv

load_dotenv()


pixela_endpoint = "https://pixe.la/v1/users"

username = os.environ.get("USERNAME")
token  = os.environ.get("TOKEN")
graphid = os.environ.get("GRAPHID")

user_params ={
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint,json=user_params)

# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{username}/graphs"


graph_config = {
    "id": graphid,
    "name" : "Coding Tracker",
    "unit" : "days",
    "type" : "int",
    "color" : "shibafu",
}

# graph_response = requests.post(url=graph_endpoint,json=graph_config,headers={"X-USER-TOKEN": TOKEN})

# print(graph_response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphid}"


add_point_config = {
    "date": "20260903",
    "quantity": "1",
}

add_pixel_response = requests.post(url=add_pixel_endpoint,json=add_point_config,headers={"X-USER-TOKEN": token})

print(add_pixel_endpoint)

print(add_pixel_response.text)