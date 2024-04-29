import taipy as tp
from taipy.gui import Gui
from taipy.config import Config 
from pages.root import *


def on_change(state, var_name, var_value):
    """Handle variable changes in the GUI."""
    if var_name in ['x_selected', 'y_selected']:
        on_change_Visualization(state)



def on_init(state):
    """Handle initialization of the GUI."""
    on_init_Presentation_projet(state)


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