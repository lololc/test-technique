from process.generate_graph import generate_drugs_graph
import pandas as pd


def test_generate_drugs_graph():
    record = pd.DataFrame(
        [
            {
                "id": "",
                "title": "Comparison of pressure BETAMETHASONE release, phonophoresis and dry needling in treatment of latent myofascial trigger point of upper trapezius ATROPINE muscle.",
                "date": "01/03/2020",
                "journal": "The journal of maternal-fetal & neonatal medicine",
                "type": "pubmed",
                "words": {
                    "and",
                    "atropine",
                    "betamethasone",
                    "comparison",
                    "dry",
                    "in",
                    "latent",
                    "muscle",
                    "myofascial",
                    "needling",
                    "of",
                    "phonophoresis",
                    "point",
                    "pressure",
                    "release",
                    "trapezius",
                    "treatment",
                    "trigger",
                    "upper",
                },
            }
        ]
    )
    filePath = generate_drugs_graph(
        record, drugFilePath="../data/tests/drugs.csv", outputPath="../data/tests/"
    )
    res = pd.read_json(filePath, orient="records", convert_dates=False).to_dict(
        orient="records"
    )
    assert res == [
        {
            "drug": "betamethasone",
            "title": "Comparison of pressure BETAMETHASONE release, phonophoresis and dry needling in treatment of latent myofascial trigger point of upper trapezius ATROPINE muscle.",
            "date": "01/03/2020",
            "type": "pubmed",
        },
        {
            "drug": "betamethasone",
            "title": "The journal of maternal-fetal & neonatal medicine",
            "date": "01/03/2020",
            "type": "journal",
        },
    ]

