import requests
import datetime
import os 
from dotenv import load_dotenv

load_dotenv()


pixela_endpoint = "https://pixe.la/v1/users"

username = os.environ.get("USERNAME")
token  = os.environ.get("TOKEN")
graphid = os.environ.get("GRAPHID")



## CReate account requirments 
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
    "date": datetime.datetime.now().strftime("%Y%m%d"),
    "quantity": "1",
}

# add_pixel_response = requests.post(url=add_pixel_endpoint,json=add_point_config,headers={"X-USER-TOKEN": token})

print(add_pixel_endpoint)





def menu():
    print("What would you like to do")
    print("1. Add today! Good Job")
    print("2. Delete a day accident \n Fuck you jackass ")
    print("3. Exit menu ") 
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_pixel_response = requests.post(url=add_pixel_endpoint,json=add_point_config,headers={"X-USER-TOKEN": token})
    elif choice ==2:
        deletedate = input("Enter a day you want to delte in yyyyMMdd format.: ")
        delete_pixel_response = requests.delete(url=f"{add_pixel_endpoint}/{deletedate}",headers={"X-USER-TOKEN": token})
    else:
        print("Good bye")




menu()
