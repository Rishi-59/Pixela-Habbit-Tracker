import random

import requests
from datetime import datetime
import secrets

TOKEN = ""
USERNAME = "kunal59"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPHID}"

headers = {
    "X-USER-TOKEN" : TOKEN,
}

def create_user(USERNAME):
    Token = secrets.token_urlsafe(8)
    print("Token : " + Token)
    params = {
        "token": Token,
        "username" : USERNAME,
        "agreeTermsOfService" : "yes",
        "notMinor" : "yes"
    }

    response = requests.post(url=pixela_endpoint, json=params)
    print(response.text)
    return Token

def create_graph(name, type, unit, color):
    GraphId = f"graph{random.randint(1,1000)}"
    graph_config = {
        "id" : GraphId,
        "name" : name,
        "unit" : unit,
        "type" : type,
        "color" : color
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response)
    return GraphId

def create_pixel(USERNAME, GraphID , quantity):
    endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GraphID}"
    today = datetime.now()
    data = {
        "date" : today.strftime("%Y%m%d"),
        "quantity" : quantity
    }
    response = requests.post(endpoint, json=data, headers=headers)
    print(response.json())

    return response.json()

def update_pixel(USERNAME, GraphID , quantity, date):
    endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GraphID}/{date}"

    updated_data = {
        "quantity" : quantity
    }

    response = requests.put(endpoint, json=updated_data, headers=headers)
    print(response)

    return response.json()

def delete_pixel(USERNAME, GraphID , date):
    endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GraphID}/{date}"
    response = requests.delete(endpoint, headers=headers)
    print(response.json())
    return response.json()
