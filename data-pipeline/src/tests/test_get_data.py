from load.get_data import read_data, extract_words


def test_read_data_pubmedcsv():
    res = read_data("../data/tests/pubmed.csv", "pubmed")
    assert res.shape == (2, 6)


def test_read_data_pubmedjson():
    res = read_data("../data/tests/pubmed.json", "pubmed")
    assert res.shape == (1, 6)


def test_read_data_clinicaltrialsjson():
    res = read_data("../data/tests/clinical_trials.csv", "clinical_trials")
    assert res.shape == (1, 6)


def test_read_data_filetype():
    res = read_data("../data/tests/pubmed.txt", "pubmed")
    assert not (res)


def test_read_data_filenotfound():
    res = read_data("../data/tests/pubmed2.csv", "pubmed")
    assert not (res)


def test_extract_words():
    words = extract_words(
        "A 44-year-old man with erythema of the face diphenhydramine, neck, and chest, weakness, and palpitations"
    )
    assert words == {
        "erythema",
        "with",
        "and",
        "chest",
        "of",
        "weakness",
        "neck",
        "diphenhydramine",
        "44yearold",
        "a",
        "palpitations",
        "man",
        "the",
        "face",
    }

