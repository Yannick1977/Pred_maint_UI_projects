import pandas as pd
import requests
import json
from urllib.parse import quote
from datetime import datetime

from taipy.gui import Markdown


def on_change_val(state):
    print("Heure actuelle 1 =", datetime.now().strftime("%H:%M:%S:%f"))
    state.predict_done = False
    if build_request(state):
        
        print("Heure actuelle 2 =", datetime.now().strftime("%H:%M:%S:%f"))
        state.predict_done = True

def build_request(state)->bool:
    data = {}
    data["Type"] = state.type_selected
    data["Air_temperature"] = state.val_air_temp
    data["Process_temperature"] = state.val_process_temp
    data["Rotational_speed"]= state.val_rotational_speed
    data["Torque"] = state.val_torque
    data["Tool_wear"] = state.val_tool_wear

    url = state.BASE_URL+quote('predict')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers,data=json.dumps(data))

    # Vérifiez le statut de la réponse
    if response.status_code == 200:
        print('Requête 1 réussie.')
        # Sauvegardez le contenu de la réponse
        for i,rep in enumerate(response.json()):
            state.name_failure[i] = rep['name']
            state.proba_failure[i] = rep['proba']*100.0

        state.proba_failure = list(map(round, state.proba_failure))
        state.df['Label'] = state.name_failure
        state.df['Prob'] = state.proba_failure
        #print(state.name_failure)

        #print(state.proba_failure)
        return True
    else:
        print('Requête 1 échouée.')
        return False



var_typ1="Variables categorielles"
var_typ2="Variables numeriques"
var_label_pred = "Label"
var_proba_pred = "Probabilité"

list_features = ['Type',
 'Air temperature [K]',
 'Process temperature [K]',
 'Rotational speed [rpm]',
 'Torque [Nm]',
 'Tool wear [min]']

val_air_temp = 0
val_process_temp = 0
val_rotational_speed = 0
val_torque = 0
val_tool_wear = 0
val_difference_temp = 0
val_power = 0
type_selected = ""

#<|{df}|chart|x=Prob|y=Label|type=bar|orientation=h|title=Prediction|layout=layout|>
properties = {
    # Shared y values
    "y": "Label",
    # Bars for the female data set
    "x[1]": "Prob",
    "color[1]": "#5c91de",
    # Bars for the male data set
    #"x[2]": "Male",
    #"color[2]": "#c26391",
    # Both data sets are represented with an horizontal orientation
    "orientation": "h",
    #
    "layout": {
        # This makes left and right bars aligned on the same y value
        #"barmode": "overlay",
        # Set a relevant title for the x axis
        "xaxis": {"title": "Probabilité en %"},
        # Set a relevant title for the y axis
        "yaxis": {"title": "Fault type"},
        # Hide the legend
        "showlegend": True,
        "margin": {"l": 200},
    },
}

Model = Markdown("pages/Model/Model.md")