# Data-pipeline
## Code
Voir le code et le Readme dans le répertoire data-pipline

## Traitement Ad-hoc
Voir le code dans le répertoire top-journal.  
Pour une étude Ad-hoc, le code a été écrit en mode "Cellule jupyter intéractive" dans vscode.

## Scaling
Pour pouvoir gérer de grandes volumétries de données dans le data-pipeline (très gros fichiers ou grand nombre de fichiers), 2 solutions peuvent être mise en place (en fonction de l'infrastructure déjà en place, des compétences internes...) :  
1- Un traitement distribué sur un cluster kubernetes
2- Un traitement distribué sur un cluster Spark  

Pour mettre en place la première solution, il faut prendre en compte les éléments suivants :
* Si certains fichiers sont trop volumineux pour tenir en mémoire, faire un split du fichier en plusieurs parties
* Utiliser un mécanisme de pub/sub (publication/souscription) pour publier la liste des fichiers à traiter
* Déployer un grand nombre de containers pour exécuter les traitements, chaque container récupérant les fichiers à traiter (tour à tour) dans la souscription pub/sub (il faut donc modifier légèrement le code pour lire de manière continue dans la souscription).
* Chaque fichier d'entrée traité génére un fichier json de sortie. La structure de donnée des fichiers de sortie a été définie pour permettre de concaténer directement ces derniers pour avoir le résultat global

Pour mettre en place la solution Spark, il faut :
* Modifier légèrement les codes de load et process pour l'adapter à pyspark (travail simple car spark possède une structure Dataframe proche de celle de pandas)
* Lancer le traitement sur l'ensemble des fichiers source
* Le système va générer un résultat partitionné (donc plusieurs fichiers json). Comme dans le cas précédent, la structure de donnée permet la concaténation pour un résultat global

# SQL
## Chiffre d'affaire 2019
Requête SQL : 
```
SELECT
  date,
  SUM(prod_price*prod_qty) AS vente
FROM
  transaction
WHERE
  date BETWEEN "2019-01-01"
  AND "2019-12-31"
GROUP BY
  date
```

## Ventes meubles et deco par client en 2019
```
WITH
  ventesbyprodtype AS (
  SELECT
    tr.client_id,
    pn.product_type,
    SUM(prod_price*prod_qty) AS vente
  FROM
    transaction tr
  INNER JOIN
    product_nomenclature pn
  ON
    tr.prod_id = pn.product_id
  WHERE
    tr.date BETWEEN "2019-01-01"
    AND "2019-12-31"
    AND pn.product_type IN ("MEUBLE",
      "DECO")
  GROUP BY
    tr.client_id,
    pn.product_type)
SELECT
  client_id,
  ANY_VALUE(
  IF
    (product_type="MEUBLE",
      vente,
      NULL)) AS vente_meuble,
  ANY_VALUE(
  IF
    (product_type="DECO",
      vente,
      NULL)) AS vente_deco
FROM
  ventesbyprodtype
GROUP BY
  client_id
```

