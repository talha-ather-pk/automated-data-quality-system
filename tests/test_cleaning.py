import pandas as pd

def test_duplicates_removed():

    df = pd.read_csv(
        "data/cleaned/cleaned_data.csv"
    )

    assert df.duplicated().sum() == 0