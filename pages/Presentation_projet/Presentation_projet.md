# *Fault Classification* - **Introduction**{: .color-primary}

<|container card|
Cette application permet de definir les valeurs du process et permet de predire si il y aura un defaut et d'en connaitre la cause
<br/>
Cette interface va interrogée un site distant via des API. L'application serveur a été entraine sur des données issue du site Kaggle.
<br/>
Vous trouverez une description du dataset à [cette adresse](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification)

|>
----
<|container card|
Le site distant étant un site serverless, celui peut mettre quelques minutes à demarrer

<|APIs is alive ?|button|on_action=is_alive|>
  **Status:** <|{status_connexion}|>
|>

----
## Dataset **Visualisation**{: .color-primary} : 
<Training|part|render={connexion_asked}|
<|{dataset}|table|>
|Training>
----
## Affichage des **Entrypoints**{: .color-primary} :
<|part|page=https://test-pred-maint-projects.onrender.com/docs|height=500px|render={connexion_asked}|>
----
<|request|button|on_action=req|>
<|{resp}|input|multiline|label=Resulting response|class_name=fullwidth|>

