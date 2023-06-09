import requests
from datetime import datetime
import os

USERNAME = "theadambishop"
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph001"
TODAY = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixela_value_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"

pixela_header = {"X-USER-TOKEN": TOKEN}

graph_config = {
    "id": "graph001",
    "name": "Python Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

value_config = {
    "date": TODAY,
    "quantity": input("How many hours did you work on Python today? ")
}

response = requests.post(pixela_value_endpoint, headers=pixela_header, json=value_config)
response.raise_for_status()

print(response.json())
