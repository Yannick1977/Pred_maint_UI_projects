
import pandas as pd
import plotly.express as px

from taipy.gui import Markdown

scatter = None
histogram = None
graph_selector = ['Histogram', 'Scatter']
graph_selected = graph_selector[0]

def create_scatter(dataset, x_selected, y_selected):
    dataset['Target'] = dataset['Target'].astype(int)
    dataset['Target'] = dataset['Target'].map({0: 'No Fault', 1: 'Fault'})
    return px.scatter(dataset, x=x_selected, y=y_selected, color="Target", marginal_x="histogram", marginal_y="violin", hover_data=dataset.columns, title="2D Distribution of Fault")

def create_histogram(dataset, x_selected):
    dataset['Target'] = dataset['Target'].astype(int)
    dataset['Target'] = dataset['Target'].map({0: 'No Fault', 1: 'Fault'})
    return px.histogram(dataset, x=x_selected, color="Target", marginal="box", hover_data=dataset.columns, title="Fault distribution", barmode="overlay")


def on_change_Visualization(state):
    state.scatter = create_scatter(state.dataset.copy(), state.x_selected, state.y_selected)
    state.histogram = create_histogram(state.dataset.copy(), state.x_selected)
   

Visualisation = Markdown("pages/Visualisation/Visualisation.md")
