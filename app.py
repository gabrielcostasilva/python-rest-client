import requests
import json
import time

list = [
    "a",
    "b",
    "f"
]
for item in list:
    try:
        response = requests.get(
            f"https://super-secret-api.com.br/v1/info/{item}/secure-key"
        )

        if response.status_code == 200:
            print(json.dumps(response.json()))
            print(", ")

        time.sleep(10)

    except Exception as e:
        print(e)
