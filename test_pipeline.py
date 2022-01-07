import pytest
from pyspark.sql import SparkSession

from mytransform import sample_transform

@pytest.fixture(scope="session")
def spark_session():
    spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
    return spark

@pytest.mark.usefixtures("spark_session")
def test_sample_transform(spark_session):
    test_df = spark_session.createDataFrame(
        [
            ('hobbit', 'Samwise', 5),
            ('hobbit', 'Billbo', 50),
            ('hobbit', 'Billbo', 20),
            ('wizard', 'Gandalf', 1000)
        ],
        ['creature', 'name', 'age']
    )
    res = sample_transform(test_df)
    assert len(res) == 1
    assert res[0][0] == 268.75
