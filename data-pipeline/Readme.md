# Data Pipeline Project
Le data pipeline permet de créer un graphe de dépendances entre les principes actifs et leur apparition dans certaines publications. Les principes actifs pris en compte sont définis dans le fichier data/raw/drugs.csv et les publications sont disponibles dans 3 types de fichiers : data/raw/clinical_trials.csv, data/raw/pubmed.csv, data/raw/pubmed.json.  

## Eléments du pipeline
Le pipeline est composé de 2 étapes :
* Une première étape de chargement de données : src/load/get_data.py. Cette étape permet lire les fichiers de publication et de générer une liste de mots à partir du titre. Ce module permet de gérer les 3 types de fichiers "publication"
* Une deuxième étape qui permet de générer le graphe et enregister le résultat au format json : src/process/generate_graph.py. Ce module utilise la liste de mots générée lors de la première étape du workflow pour vérifier si un nom de principe actif est présent.

Remarque : ces 2 étapes peuvent facilement être utilisées au sein d'un DAG Airflow en tant que PythonOperator par example.

## Exécution
### En local dans un environnement conda ou virtualenv
* Créer un nouvel environnement
* Installer les dépendances : `pip install requirements.txt` ou `conda install --file requirements.txt`
* Se placer dans le répertoire src et lancer le main.py : `python main.py`
* Le fichier de résultats json est généré dans le répertoire data/processed/

### Docker
* Lancer le programme via la commande : `docker-compose up`
* Le fichier de résultats json est généré dans le répertoire data/processed/

### Tests
* Installer la libraire pytest
* Lancer les tests unitaires via la commande depuis le répertoire src : `python -m pytest tests/`