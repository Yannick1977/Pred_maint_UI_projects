import pandas as pd
import requests
import json
from urllib.parse import quote
from datetime import datetime
import plotly.express as px
from taipy.gui import notify

from taipy.gui import Markdown

b_submit = 1
str_submit = "Submit"

def submit_val(state):
    """Submit values for prediction and explanation.

    Args:
        state: The state object containing the values to be submitted.

    Returns:
        bool: True if the submission is successful, False otherwise.
    """
    state.b_submit = 2
    state.str_submit = "Processing..."

    if build_request_predict(state) & build_request_explain(state):
        state.ID_request += 1

    state.str_submit = "Submit"
    state.b_submit = 1

def on_init_Model(state):
    """Initialize the Model page.

    Args:
        state: The state object to be initialized.
    """
    state.str_submit = "Submit"
    state.b_submit = 1

def on_change_val(state):
    """Not used."""
    pass

def build_request_predict(state) -> bool:
    """Build the request for prediction.

    Args:
        state: The state object containing the data for prediction.

    Returns:
        bool: True if the request is successful, False otherwise.
    """
    data = {}
    data["Type"] = state.type_selected
    data["Air_temperature"] = state.val_air_temp
    data["Process_temperature"] = state.val_process_temp
    data["Rotational_speed"]= state.val_rotational_speed
    data["Torque"] = state.val_torque
    data["Tool_wear"] = state.val_tool_wear

    url = state.BASE_URL + quote('predict')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response status
    if response.status_code == 200:
        # Save the response content
        for i, rep in enumerate(response.json()):
            state.name_failure[i] = rep['name']
            state.proba_failure[i] = rep['proba'] * 100.0

        state.proba_failure = list(map(round, state.proba_failure))
        state.df['Label'] = state.name_failure
        state.df['Prob'] = state.proba_failure

        return True
    else:
        return False

def build_request_explain(state) -> bool:
    """Build the request for explanation.

    Args:
        state: The state object containing the data for explanation.

    Returns:
        bool: True if the request is successful, False otherwise.
    """
    data = {}
    data["Type"] = state.type_selected
    data["Air_temperature"] = state.val_air_temp
    data["Process_temperature"] = state.val_process_temp
    data["Rotational_speed"]= state.val_rotational_speed
    data["Torque"] = state.val_torque
    data["Tool_wear"] = state.val_tool_wear

    url = state.BASE_URL + quote('explain')
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response status
    if response.status_code == 200:
        # Save the response content
        state.df_explain = pd.DataFrame(response.json())
        return True
    else:
        return False

var_typ1 = "Categorical variables"
var_typ2 = "Numerical variables"
var_label_pred = "Label"
var_proba_pred = "Probability"

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

properties = {
    "y": "Label",
    "x[1]": "Prob",
    "color[1]": "#5c91de",
    "orientation": "h",
    "layout": {
        "xaxis": {"title": "Probability (%)"},
        "yaxis": {"title": "Fault type"},
        "showlegend": True,
        "margin": {"l": 200},
    },
}

prediction_graphique = None
explain_graphique = None
output_selector = ['Prediction', 'Explain']
output_selected = output_selector[0]

def create_prediction_graphique(state):
    """Create the prediction graph.

    Args:
        state: The state object containing the data for the graph.

    Returns:
        plotly.graph_objects.Figure: The prediction graph.
    """
    graph = px.bar(state.df, x="Prob", y="Label", text_auto=True)
    graph.update_layout(autosize=True, margin=dict(l=250))
    return graph

def create_explain_graphique(state):
    """Create the explanation graph.

    Args:
        state: The state object containing the data for the graph.

    Returns:
        plotly.graph_objects.Figure: The explanation graph.
    """
    graph = px.bar(state.df_explain, x="weight", y="item", text_auto=True)
    graph.update_layout(autosize=True, margin=dict(l=250))
    return graph

def on_change_Model(state):
    """Handle variable changes in the Model page.

    Args:
        state: The state object containing the updated variables.
    """
    state.prediction_graphique = create_prediction_graphique(state)
    state.explain_graphique = create_explain_graphique(state)
    notify("Prediction completed", "Predictions and explanations have been successfully calculated")
    output_selected = None

Model = Markdown("pages/Model/Model.md")