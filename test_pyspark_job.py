from pyspark.sql import SparkSession
from pyspark_job import clean_data


def test_clean_data():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("test")
        .getOrCreate()
    )

    data = [
        (1, "Ahmed", 100),
        (2, "Mohamed", 200),
        (3, "Omar", 0),
        (4, "Ali", -50),
        (5, None, 300),
    ]

    df = spark.createDataFrame(
        data,
        ["id", "name", "amount"]
    )

    result = clean_data(df)

    rows = result.orderBy("id").collect()

    assert len(rows) == 2

    assert rows[0]["name"] == "Ahmed"
    assert rows[1]["name"] == "Mohamed"

    assert rows[0]["amount_with_tax"] == 120
    assert rows[1]["amount_with_tax"] == 240

    spark.stop()