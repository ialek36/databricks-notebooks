import pyspark.sql.functions as F
from pyspark.sql import DataFrame


def sample_transform(input_df: DataFrame) -> DataFrame:
    res = input_df.select(F.mean('age')).alias('new_column').collect()
    return res
