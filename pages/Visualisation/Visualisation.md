# Data **Visualisation**{: .color-primary}

Visualisation des données du dataset avec des histogrammes ou des nuages de points.<br/>

<|{graph_selected}|toggle|lov={graph_selector}|>

--------------------------------------------------------------------

<|part|render={graph_selected == 'Histogram'}|
### Histogram

Choisissez la variable pour la distribution en distinguant la presence de default.<br/>

<|{x_selected}|selector|lov={x_to_select}|dropdown=True|label=Select column|>

<|chart|figure={histogram}|height=700px|>
|>

<|part|render={graph_selected == 'Scatter'}|
### Scatter

Choisissez deux variables pour visualiser la distribution 2D en distinguant la presence de defaut.<br/>

<|layout|columns=1 2|
<|{x_selected}|selector|lov={x_to_select}|dropdown|label=Select x|>

<|{y_selected}|selector|lov={y_to_select}|dropdown|label=Select y|>
|>

<|chart|figure={scatter}|height=700px|>
|>