# Model **Inference**{: .color-primary}


<|layout|columns=1 1|columns[mobile]=1|gap=20px|class_name=card|

<var_typ1|
## **Variables numeriques**{: .color-primary}
<|part|render={connexion_asked}|
<|layout|columns=1 2|
<v1|
<|{list_features[1]}|>
|v1>
<v2|
<|{val_air_temp}|slider|min={min_val_air_temp}|max={max_val_air_temp}|on_change=on_change_val|change_delay=1000|width=500|>
|v2>
|>
<br/>
<|layout|columns=1 2|
<v1|
<|{list_features[2]}|>
|v1>
<v2|
<|{val_process_temp}|slider|min={min_val_process_temp}|max={max_val_process_temp}|on_change=on_change_val|change_delay=1000|width=500|>
|v2>
|>
<br/>
<|layout|columns=1 2|
<v1|
<|{list_features[3]}|>
|v1>
<v2|
<|{val_rotational_speed}|slider|min={min_val_rotational_speed}|max={max_val_rotational_speed}|on_change=on_change_val|change_delay=1000|width=500|>
|v2>
|>
<br/>
<|layout|columns=1 2|
<v1|
<|{list_features[4]}|>
|v1>
<v2|
<|{val_torque}|slider|min={min_val_torque}|max={max_val_torque}|on_change=on_change_val|change_delay=1000|width=500|>
|v2>
|>
<br/>
<|layout|columns=1 2|
<v1|
<|{list_features[5]}|>
|v1>
<v2|
<|{val_tool_wear}|slider|min={min_val_tool_wear}|max={max_val_tool_wear}|on_change=on_change_val|change_delay=1000|width=500|>
|v2>
|>

|>
|var_typ1>

<var_typ2|
## **Variables categorielles**{: .color-primary}
<|part|render={connexion_asked}|
<|layout|columns=1 1|
<v1|
<|{list_features[0]}|>
|v1>
<v2|
<|{type_selected}|selector|lov={lst_val_type}|dropdown=True|label=Select Type|on_change=on_change_val|>
|v2>
|>

|>
|var_typ2>

|>
<|Submit|button|on_action=submit_val|>
---
<|{output_selected}|toggle|lov={output_selector}|>

---
<|part|render={output_selected == 'Prediction'}|
## **Prediction**{: .color-primary}
<|chart|figure={prediction_graphique}|height=700px|>

|>
---
<|part|render={output_selected == 'Explain'}|
## **Explanation**{: .color-primary}
<|chart|figure={explain_graphique}|height=700px|>

|>
---

