import pandas as pd
import time
import logging

pd.options.mode.chained_assignment = None
log = logging.getLogger(__name__)


def generate_drugs_graph(
    records, drugFilePath="../data/raw/drugs.csv", outputPath="../data/processed/"
):
    """
    Function to create drugs graph in json format

    Args:
        records: dataframe of source data (pubmed or clinical trials)
        drugfilePath: path to the reference drug file
        outputPath : output folder to save json file

    Returns:
        json file representing drugs dependencies
    """
    log.info(f"Start generation the drugs dependencies graph")
    drugs = pd.read_csv(drugFilePath)
    log.debug(f"{drugs.shape[0]} drugs to evaluate from file {drugFilePath}")
    graph = pd.DataFrame()
    for drug in drugs["drug"].str.lower():
        log.debug(f"Working on drug {drug}")
        filtered = records[records["words"].apply(lambda x: drug in x)]
        if filtered.shape[0] > 0:
            filtered["drug"] = drug
            # Add records relative to pubmed or clinical_trials
            article = filtered[["drug", "title", "date", "type"]]
            graph = pd.concat([graph, article])
            # Add records relative to journal
            journal = filtered[["drug", "journal", "date"]]
            journal.rename(columns={"journal": "title"}, inplace=True)
            journal["type"] = "journal"
            graph = pd.concat([graph, journal])
            log.debug(
                f"{article.shape[0]+journal.shape[0]} relations added to graph for drug {drug}"
            )
        else:
            log.debug(f"No relation added to graph for drug {drug}")
    # Generate unique output file name based on time
    outputFileName = outputPath + "drug_graph_" + str(int(time.time())) + ".json"
    try:
        graph.to_json(outputFileName, orient="records")
        log.info(f"File {outputFileName} successfully generated")
    except Exception as e:
        log.error(f"Error writing file {outputFileName} :: {e}")
        return None
    return outputFileName
