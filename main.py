import taipy as tp
from taipy.gui import Gui
from taipy.config import Config 
from pages.root import *

from pages.root import feature_numeric, feature_list


def on_change(state, var_name, var_value):
    """Handle variable changes in the GUI."""
    if var_name in ['x_selected', 'y_selected']:
        on_change_Visualization(state)
    elif var_name == 'ID_request':
        on_change_Model(state)


def on_init(state):
    """Handle initialization of the GUI."""
    on_init_Presentation_projet(state)
    on_init_Model(state)

# Define pages
pages = {
    "/": root,
    "Presentation_projet": Presentation_projet,
    "Visualisation": Visualisation, 
    "Model": Model,
}

if __name__ == '__main__':
    tp.Core().run()

    gui = Gui(pages=pages)
    gui.run(title="Maintenance projects", dark_mode=True, port=8494)