import pandas as pd
import string
import json
import os
import re
import logging

log = logging.getLogger(__name__)


def extract_words(text):
    """
    Function to extract words from string

    Args:
        text: string to process

    Returns:
        set of words extracted from input string
    """
    # Use translation table to remove punctuation
    transTable = str.maketrans("", "", string.punctuation)
    words = text.lower().split()
    cleanWords = {w.translate(transTable).strip() for w in words}
    log.debug(f"Words : {cleanWords} extracted from string '{text}'")
    return cleanWords


def read_data(inputPath, fileType):
    """
    Function to read pubmed file and to add 'type' (=pubmed) and 'words' (from title) columns to data

    Args:
        inputPath: path to the file to read
        fileType: data file type either 'pubmed' or 'clinical_trials'

    Returns:
        dictionary of the pubmed data with additional 'type' and 'words' keys
        None if file does not exists or not csv/json format
    """
    log.info(f"Start the read of the {fileType} file {inputPath}")
    ext = os.path.splitext(inputPath)[-1]
    try:
        if ext == ".csv":
            datain = pd.read_csv(inputPath)
        elif ext == ".json" and fileType == "pubmed":
            with open(inputPath) as f:
                # Use regex to remove trailing comma on non regular json file
                datain = json.loads(re.sub(r".*},\n]", "}\n]", f.read()))
            datain = pd.DataFrame(datain)
        else:
            log.error("Not a correct file format")
            return None
        if fileType == "clinical_trials":
            datain.rename(columns={"scientific_title": "title"}, inplace=True)
        datain["type"] = fileType
        datain["words"] = datain["title"].apply(extract_words)
        log.info(
            f"{fileType} file {inputPath} successfully read ({datain.shape[0]} records)"
        )
        return datain
    except FileNotFoundError:
        log.error("File does not exists")
        return None
