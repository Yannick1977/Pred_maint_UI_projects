from taipy.gui import Icon, navigate
import taipy.gui.builder as tgb
from pages.Presentation_projet.Presentation_projet import *
from pages.Visualisation.Visualisation import *
from pages.Model.Model import *

# dialog
show_roc = False

#https://github.com/google/material-design-icons/upload/master/png

# Common variables to several pages
BASE_URL = 'https://test-pred-maint-projects.onrender.com/'
dict_numeric = {}
dict_list = {}

x_to_select = []
x_selected = None
y_to_select = []
y_selected = None

min_val_air_temp = 0.0
max_val_air_temp = 99.0
min_val_process_temp = 0
max_val_process_temp = 99
min_val_rotational_speed = 0
max_val_rotational_speed = 99
min_val_torque = 0
max_val_torque = 99
min_val_tool_wear = 0
max_val_tool_wear = 99

lst_val_type = []

status_connexion = "unknown"
connexion_asked = False
predict_done = False
name_failure = ["", "", "", "", ""]
proba_failure = [0.0, 0.0, 0.0, 0.0, 0.0]
df= pd.DataFrame(columns=["Label", "Prob"])


class feature_numeric:
    def __init__(self, name:str, min, max):
        self.name = name
        self.min = min
        self.max = max

class feature_list:
    def __init__(self, name:str, values:list):
        self.name = name
        self.values = values

menu_lov = [
    ("Presentation projet", Icon('images/description.png', 'Presentation projet')),
    ("Visualisation", Icon('images/line-graph.png', 'Visualisation')),
    ("Model", Icon('images/deep-learning.png', 'Model'))
]


def menu_fct(state, var_name, var_value):
    """Function that is called when there is a change in the menu control."""
    page = var_value['args'][0].replace(" ", "_")
    navigate(state, page)   

def close_dialog(state):
    state.show_roc = False


with tgb.Page() as roc_curve_page:
    tgb.chart("{roc_dataset}", x="False positive rate", y="True positive rate", label="True positive rate", height="500px", width="90%", type="scatter")


with tgb.Page() as root:
    tgb.toggle(theme=True)
    tgb.menu(label="Menu", lov=menu_lov, on_action=menu_fct)

    tgb.dialog(open="{show_roc}", page="ROC-Curve", title="ROC Curve", width="100%", on_action=close_dialog)