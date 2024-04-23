import taipy as tp
from taipy.gui import Gui
from taipy.config import Config 
from pages.root import *


def on_change(state, var_name, var_value):
    """Handle variable changes in the GUI."""



def on_init(state):
    """Handle initialization of the GUI."""


# Define pages
pages = {
    "/": root,
    "Presentation projet": Presentation_projet,
    "Visualisation": visualisation, 
    "Model": Model,
}

if __name__ == '__main__':
    tp.Core().run()

    gui = Gui(pages=pages)
    gui.run(title="Churn classification", dark_mode=False, port=8494)