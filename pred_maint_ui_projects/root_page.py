from taipy.gui import Icon, navigate
import taipy.gui.builder as tgb
from pages.compare_models.compare_models import *
from pages.data_visualization.data_visualization import *
from pages.databases.databases import *
from pages.model_manager.model_manager import *

# dialog
show_roc = False

# Common variables to several pages
algorithm_selector = ['Baseline', 'ML']
algorithm_selected = 'ML'

select_x = []
x_selected = None
select_y = []
y_selected = None

menu_lov = [
    ("Data Visualization", Icon('images/histogram_menu.svg', 'Data Visualization')),
    ("Model Manager", Icon('images/model.svg', 'Model Manager')),
    ("Compare Models", Icon('images/compare.svg', 'Compare Models')),
    ('Databases', Icon('images/Datanode.svg', 'Databases'))
]


def menu_fct(state, var_name, var_value):
    """Function that is called when there is a change in the menu control."""
    page = var_value['args'][0].replace(" ", "-")
    navigate(state, page)   

def close_dialog(state):
    state.show_roc = False


with tgb.Page() as roc_curve_page:
    tgb.chart("{roc_dataset}", x="False positive rate", y="True positive rate", label="True positive rate", height="500px", width="90%", type="scatter")


with tgb.Page() as root:
    tgb.toggle(theme=True)
    tgb.menu(label="Menu", lov=menu_lov, on_action=menu_fct)

    tgb.dialog(open="{show_roc}", page="ROC-Curve", title="ROC Curve", width="100%", on_action=close_dialog)