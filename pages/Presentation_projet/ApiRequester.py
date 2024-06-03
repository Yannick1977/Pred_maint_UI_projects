import requests
from time import sleep

class apiRequester:
    def __init__(self, url, state):
        """
        Initializes an instance of the ApiRequester class.

        Args:
            url (str): The URL of the API.
            state (str): The state of the page.

        Attributes:
            url (str): The URL of the API.
            num_requests_attempts (int): The number of attempts made to send requests to the API.
            timeout (int): The timeout duration for API requests.
            state (str): The state of the API request.
        """
        self.url = url
        self.num_requests_attempts = 0
        self.timeout = 20
        self.state = state

    def get_request(self, num_max_requests):
        """Send a GET request to the API. This is use to check if the API is alive and 
            if not, try to re-connect to it.

        Args:
            num_max_requests (int): The maximum number of requests to send.

        Returns:
            tuple: A tuple containing a boolean value indicating if the request was successful,
                   and the response object if the request was successful, otherwise None.

        Raises:
            None

        """
        self.state.status_connexion = "Starting in progress...!"
        for _ in range(num_max_requests):
            try:
                response = requests.get(self.url, timeout=self.timeout)
                print(response.status_code)
                if response.status_code == 200:
                    self.state.status_connexion = "Connected, Reading response..."
                    return True, response
                else:
                    self.state.status_connexion = f"Not connected. code error: {response.status_code}  Attempt: {self.num_requests_attempts}"
                    self.num_requests_attempts += 1
                    sleep(10)  # Attendre 10 secondes
            except requests.exceptions.Timeout:
                self.state.status_connexion =f"Attempt: {self.num_requests_attempts}/{num_max_requests}"
                self.num_requests_attempts += 1
        return False, None