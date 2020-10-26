from load.get_data import read_data
from process.generate_graph import generate_drugs_graph
import pandas as pd
import logging.config

if __name__ == "__main__":

    logging.config.fileConfig("../conf/logging.conf", disable_existing_loggers=False)

    # Load and prepare data from 3 types of files
    pubmedcsv = read_data("../data/raw/pubmed.csv", "pubmed")
    pubmedjson = read_data("../data/raw/pubmed.json", "pubmed")
    clinicaltrials = read_data("../data/raw/clinical_trials.csv", "clinical_trials")

    # Generate graph data as json file
    gengraphPath = generate_drugs_graph(
        pd.concat([pubmedcsv, pubmedjson, clinicaltrials])
    )
