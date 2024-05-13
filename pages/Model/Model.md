# Model **Inference**{: .color-primary}


<|layout|columns=1 1|columns[mobile]=1|gap=20px|class_name=card|

<var_typ1|
## **Variables numeriques**{: .color-primary}
<|part|render={connexion_asked}|
### <|{list_features[1]}|>: 
<|{val_air_temp}|slider|min={min_val_air_temp}|max={max_val_air_temp}|on_change=on_change_val|change_delay=1000|width=500|>
<br/>
### <|{list_features[2]}|>:  
<|{val_process_temp}|slider|min={min_val_process_temp}|max={max_val_process_temp}|on_change=on_change_val|change_delay=1000|width=500|>
<br/>
### <|{list_features[3]}|>:
<|{val_rotational_speed}|slider|min={min_val_rotational_speed}|max={max_val_rotational_speed}|on_change=on_change_val|change_delay=1000|width=500|>
<br/>
### <|{list_features[4]}|>:
<|{val_torque}|slider|min={min_val_torque}|max={max_val_torque}|on_change=on_change_val|change_delay=1000|width=500|>
<br/>
### <|{list_features[5]}|>: 
<|{val_tool_wear}|slider|min={min_val_tool_wear}|max={max_val_tool_wear}|on_change=on_change_val|change_delay=1000|width=500|>
|>
|var_typ1>

<var_typ2|
## **Variables categorielles**{: .color-primary}
<|part|render={connexion_asked}|
<|{list_features[0]}|>: 
<|{type_selected}|selector|lov={lst_val_type}|dropdown=True|label=Select Type|on_change=on_change_val|>
|>
|var_typ2>

|>
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
---
<|part|render={False}|
## **Prediction**{: .color-primary}

<|{df}|chart|type=bar|properties=properties|>

|>
-----
