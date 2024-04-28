
import pandas as pd
import requests

from taipy.gui import Markdown

text="essai"
resp=""
status_connexion = "!!"
connexion_asked = False

def is_alive(state):
    if not state.connexion_asked:
        url = 'https://test-pred-maint-projects.onrender.com/list_features'
        state.status_connexion = "In progress..."
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

Presentation_projet = Markdown("pages/Presentation_projet/Presentation_projet.md")