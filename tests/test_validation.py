import json

def test_health_score():

    with open(
        "reports/validation/validation_report.json"
    ) as file:

        report = json.load(file)

    assert report["data_health_score"] > 95