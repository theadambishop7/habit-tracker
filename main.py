import requests
from datetime import datetime
import os
import time

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
    "name": "Programming Progress",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

date = str(input("If not today, then please define which day you want to track time for (YYYYMMDD), "
                 "for TODAY leave blank? "))
if not date:
    today = TODAY
else:
    today = date

value_config = {
    "date": today,
    "quantity": input("How many hours did you work on Python today? ")
}

retry_limit = 5  # set a reasonable retry limit
retry_delay = 1  # set a delay between retries in seconds

success = False
attempts = 0

while not success and attempts < retry_limit:
    try:
        response = requests.post(pixela_value_endpoint, headers=pixela_header, json=value_config)
        response.raise_for_status()

        # If the response is successful, exit the loop
        success = True

    except requests.HTTPError as e:
        # Check if it's a 503 error
        if e.response.status_code == 503:
            print("Received a 503 error. Retrying...")
            attempts += 1
            time.sleep(retry_delay)  # Wait for the given delay before retrying
        else:
            # For any other exception, raise it immediately
            raise

    else:
        print(response.json())
