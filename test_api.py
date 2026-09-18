import requests
import json

with open("sample_request.json", "r") as file:
    customer = json.load(file)

    response = requests.post(
    "http://127.0.0.1:5000/predict",
    json=customer
    )

    print("Status code:", response.status_code)
    print("Response:")
    print(response.json())