import requests
import random
import os

USERNAME = "theadambishop"
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph001"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixela_value_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"

pixela_header = {"X-USER-TOKEN": TOKEN}

potential_hours = [1.5, 1, 1.5, 2, 2.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 3, 3, 3, 3.5, 4]

for n in range(1, 31):
    if n < 9:
        day = "0" + str(n + 1)
    else:
        day = str(n + 1)
    date = f"202304{day}"

    value_config = {
        "date": date,
        "quantity": str(random.choice(potential_hours))
    }

    try:
        response = requests.post(pixela_value_endpoint, headers=pixela_header, json=value_config)
    except:
        print(f"Failed on day {n + 1}")
    else:
        print(response.json())

