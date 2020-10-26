#%%
import pandas as pd

# %%
sourceData = "../data-pipeline/data/processed/drug_graph_1603703014.json"
drugGraph = pd.read_json(sourceData,orient="records")
# %%
journals = drugGraph[drugGraph["type"]=="journal"]
topJournal = journals.groupby("title")["drug"].nunique().sort_values(ascending=False)
topJournal

# %%
