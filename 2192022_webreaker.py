import threading
import requests
import time

def cujdik():
    response = requests.get("//lubovolne url//")
    while response.status_code == 200:
        response = requests.get("//lubovolne url//")
        print(response)
    print(response)

while True:
    time.sleep(0.3)
    threading.Thread(target=cujdik).start()
