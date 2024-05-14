import pandas as pd
import requests
import json
from urllib.parse import quote
from datetime import datetime
import plotly.express as px

from taipy.gui import Markdown


def on_change_val(state):
    
    if build_request_predict(state) & build_request_explain(state):
        state.ID_request += 1

def build_request_predict(state)->bool:
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
        # Sauvegardez le contenu de la réponse
        for i,rep in enumerate(response.json()):
            state.name_failure[i] = rep['name']
            state.proba_failure[i] = rep['proba']*100.0

        state.proba_failure = list(map(round, state.proba_failure))
        state.df['Label'] = state.name_failure
        state.df['Prob'] = state.proba_failure
        
        return True
    else:
        return False

def build_request_explain(state)->bool:
    data = {}
    data["Type"] = state.type_selected
    data["Air_temperature"] = state.val_air_temp
    data["Process_temperature"] = state.val_process_temp
    data["Rotational_speed"]= state.val_rotational_speed
    data["Torque"] = state.val_torque
    data["Tool_wear"] = state.val_tool_wear

    url = state.BASE_URL+quote('explain')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers,data=json.dumps(data))

    # Vérifiez le statut de la réponse
    if response.status_code == 200:
        # Sauvegardez le contenu de la réponse
        state.df_explain = pd.DataFrame(response.json())
        return True
    else:
        return False

var_typ1="Variables categorielles"
var_typ2="Variables numeriques"
var_label_pred = "Label"
var_proba_pred = "Probabilité"

df_explain = None

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

prediction_graphique = None
explain_graphique = None
output_selector = ['Prediction', 'Explain']
output_selected = output_selector[0]

def create_prediction_graphique(state):
    graph = px.bar(state.df, x="Prob", y="Label", text_auto=True)
    graph.update_layout(autosize=False, margin=dict(l=250, r=50, b=100, t=100, pad=10))
    return graph

def create_explain_graphique(state):
    graph = px.bar(state.df_explain, x="weight", y="item", text_auto=True)
    graph.update_layout(autosize=False, margin=dict(l=250, r=50, b=100, t=100, pad=10))
    return graph

def on_change_Model(state):
    state.prediction_graphique = create_prediction_graphique(state)
    state.explain_graphique = create_explain_graphique(state)


Model = Markdown("pages/Model/Model.md")