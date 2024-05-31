
import pandas as pd
import requests
from urllib.parse import quote
import requests
from time import sleep

from taipy.gui import Markdown

resp=""
dataset = pd.read_csv("./data/predictive_maintenance.csv")
BASE_URL = 'https://test-pred-maint-projects.onrender.com/'

class apiRequester:
    def __init__(self, url, state):
        self.url = url
        self.num_requests_attempts = 0
        self.timeout = 20
        self.state = state

    def get_request(self, num_max_requests):
        self.state.status_connexion = "Starting in progress...!"
        print(self.state.status_connexion+"!")
        for _ in range(num_max_requests):
            try:
                response = requests.get(self.url, timeout=self.timeout)
                print(response.status_code)
                if response.status_code == 200:
                    self.state.status_connexion = "Connected, Reading response..."
                    print(self.state.status_connexion+"!")
                    print(response.json())
                    return True, response
                else:
                    self.state.status_connexion = f"Not connected. code error: {response.status_code}  Attempt: {self.num_requests_attempts}"
                    print(self.state.status_connexion+"!")
                    self.num_requests_attempts += 1
                    sleep(10)  # Attendre 10 secondes
            except requests.exceptions.Timeout:
                self.state.status_connexion =f"Attempt: {self.num_requests_attempts}/{num_max_requests}"
                print(self.state.status_connexion+"!")
                self.num_requests_attempts += 1
                #print("La requête a dépassé le délai d'attente.")
        return False, None

def is_alive(state):
    api_requester = apiRequester(BASE_URL, state)

    try:
        if not state.connexion_asked:
            url = BASE_URL+'list_features'
            print('url : ', url)
            state.status_connexion = "Starting in progress..."
            #response = requests.get(url)
            (state.connexion_asked, response) = api_requester.get_request(20)
            if state.connexion_asked:
                state.status_connexion = "Connected, Reading features details..."
            else:
                state.status_connexion = f"Not connected. code error: {response.status_code}"

            req_features_list(state)  
            req_features_details(state, state.resp)
            state.status_connexion = "Connected"
            state.connexion_asked = True
    except Exception as e:
        print("Une erreur s'est produite: ", e)
    

def req_features_list(state):
    url = 'https://test-pred-maint-projects.onrender.com/list_features'
    response = requests.get(url)
    if response.status_code == 200:
        state.resp = response.json()
    else:
        state.resp = f"Error {response.status_code}"
    
    
    state.x_to_select = dataset.drop(columns=['Target', 'Failure Type']).columns.to_list()
    state.y_to_select = state.x_to_select
    state.x_selected = state.x_to_select[0]
    state.y_selected = state.y_to_select[1]

    

def on_init_Presentation_projet(state):
    dataset = pd.read_csv("./data/predictive_maintenance.csv")
    state.x_to_select = dataset.drop(columns=['Target', 'Failure Type']).columns.to_list()
    state.y_to_select = state.x_to_select
    state.x_selected = state.x_to_select[0]
    state.y_selected = state.y_to_select[1]

def req_features_details(state, response_json):
    for feature in response_json:
        url2 = state.BASE_URL+quote(f'features/{feature}')
        response2 = requests.get(url2)
        #print(url2)
        #print(response2.json())
        if response2.json()['type']=='object':
            state.dict_list[feature] = state.feature_list(feature, response2.json()['list'])
        else:
            state.dict_numeric[feature] = state.feature_numeric(feature, response2.json()['min'], response2.json()['max'])
    
    #print(f'test : {state.dict_list[state.list_features[0]].values}')
    state.lst_val_type = eval(state.dict_list[state.list_features[0]].values.replace(" ", ","))
    state.type_selected = state.lst_val_type[0]
    state.min_val_air_temp = state.dict_numeric[state.list_features[1]].min
    state.max_val_air_temp = state.dict_numeric[state.list_features[1]].max
    state.min_val_process_temp = state.dict_numeric[state.list_features[2]].min
    state.max_val_process_temp = state.dict_numeric[state.list_features[2]].max
    state.min_val_rotational_speed = state.dict_numeric[state.list_features[3]].min
    state.max_val_rotational_speed = state.dict_numeric[state.list_features[3]].max
    state.min_val_torque = state.dict_numeric[state.list_features[4]].min
    state.max_val_torque = state.dict_numeric[state.list_features[4]].max
    state.min_val_tool_wear = state.dict_numeric[state.list_features[5]].min
    state.max_val_tool_wear = state.dict_numeric[state.list_features[5]].max
    #print(f'val : {state.min_val_air_temp} : {state.max_val_air_temp}')

Presentation_projet = Markdown("pages/Presentation_projet/Presentation_projet.md")