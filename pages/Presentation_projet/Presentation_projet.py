
import pandas as pd
import requests

from taipy.gui import Markdown

resp=""
dataset = pd.read_csv("./data/predictive_maintenance.csv")

def is_alive(state):
    if not state.connexion_asked:
        url = 'https://test-pred-maint-projects.onrender.com/list_features'
        state.status_connexion = "Starting in progress..."
        response = requests.get(url)
        if response.status_code == 200:
            state.status_connexion = "Connected"
        else:
            state.status_connexion = f"Not connected. code error: {response.status_code}"
        state.connexion_asked = True

def req(state):
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
    print("on_init_Presentation_projet")
    dataset = pd.read_csv("./data/predictive_maintenance.csv")
    state.x_to_select = dataset.drop(columns=['Target', 'Failure Type']).columns.to_list()
    state.y_to_select = state.x_to_select
    state.x_selected = state.x_to_select[0]
    state.y_selected = state.y_to_select[1]

Presentation_projet = Markdown("pages/Presentation_projet/Presentation_projet.md")