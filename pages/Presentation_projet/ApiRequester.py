import requests
from time import sleep

class apiRequester:
    def __init__(self, url, messsage=""):
        self.url = url
        self.num_requests_attempts = 0
        self.timeout = 20

    def get_request(self, num_max_requests)->bool:
        message = "Starting in progress..."
        for _ in range(num_max_requests):
            try:
                response = requests.get(self.url, timeout=self.timeout)
                print(response.status_code)
                if response.status_code == 200:
                    message = "Connected, Reading response..."
                    print(response.json())
                    return True, response
                else:
                    message = f"Not connected. code error: {response.status_code}  Attempt: {self.num_requests_attempts}"
                    self.num_requests_attempts += 1
                    sleep(10)  # Attendre 10 secondes
            except requests.exceptions.Timeout:
                message ="Attempt: {self.num_requests_attempts}"
                self.num_requests_attempts += 1
                #print("La requête a dépassé le délai d'attente.")
        return False, None