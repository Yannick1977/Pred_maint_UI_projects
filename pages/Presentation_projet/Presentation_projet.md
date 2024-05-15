# *Fault Classification* - **Introduction**{: .color-primary}

<|container card|
Cette application a pour objectif d'utiliser un modele de Machine Learning.
Ce modele a été defini et entrainé sur un jeu de donnée disponible sur le site Kaggle.
Vous trouverez une description détaillée du dataset à [cette adresse](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification)

Ce jeu de donnée donne des valeurs de process pour un diagnostic de defaut.
Cette application permet de definir les valeurs du process et permet de predire si il y aura un defaut et d'en connaitre la cause.
<br/>
L'application est composé de la maniere suivante :  
&nbsp;&nbsp;&nbsp;&nbsp;- Back-end : Contient les API pour interroger le modele  
&nbsp;&nbsp;&nbsp;&nbsp;- Front-end : Interface graphique pour interagir avec les API  

<br/>
L'interface graphique est composé de la mniere suivante:  
&nbsp;&nbsp;&nbsp;&nbsp;- Description du projet ainsi que visualisation des API  
&nbsp;&nbsp;&nbsp;&nbsp;- Visualisation des données  
&nbsp;&nbsp;&nbsp;&nbsp;- Inference avec le modele   
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

