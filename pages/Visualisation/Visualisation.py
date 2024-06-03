
import pandas as pd
import plotly.express as px

from taipy.gui import Markdown

scatter = None
histogram = None
graph_selector = ['Histogram', 'Scatter']
graph_selected = graph_selector[0]

def create_scatter(dataset, x_selected, y_selected):
    """
    Create a scatter plot with marginal histograms and violin plots.

    Args:
        dataset (pandas.DataFrame): The dataset containing the data to be plotted.
        x_selected (str): The column name of the x-axis variable.
        y_selected (str): The column name of the y-axis variable.

    Returns:
        plotly.graph_objects.Figure: The scatter plot with marginal histograms and violin plots.
    """
    dataset['Target'] = dataset['Target'].astype(int)
    dataset['Target'] = dataset['Target'].map({0: 'No Fault', 1: 'Fault'})
    return px.scatter(dataset, x=x_selected, y=y_selected, color="Target", marginal_x="histogram", marginal_y="violin", hover_data=dataset.columns, title="2D Distribution of Fault")

def create_histogram(dataset, x_selected):
    """
    Create a histogram plot for the given dataset.

    Parameters:
    - dataset (pandas.DataFrame): The dataset containing the data to be plotted.
    - x_selected (str): The column name of the dataset to be plotted on the x-axis.

    Returns:
    - plotly.graph_objects.Figure: The histogram plot.

    """
    dataset['Target'] = dataset['Target'].astype(int)
    dataset['Target'] = dataset['Target'].map({0: 'No Fault', 1: 'Fault'})
    return px.histogram(dataset, x=x_selected, color="Target", marginal="box", hover_data=dataset.columns, title="Fault distribution", barmode="overlay")

def on_change_Visualization(state):
    """
    Update the scatter plot and histogram based on the selected dataset and x-y variables.

    Parameters:
    state (object): The state object containing the dataset and selected variables.

    Returns:
    None
    """
    state.scatter = create_scatter(state.dataset.copy(), state.x_selected, state.y_selected)
    state.histogram = create_histogram(state.dataset.copy(), state.x_selected)
   

Visualisation = Markdown("pages/Visualisation/Visualisation.md")
