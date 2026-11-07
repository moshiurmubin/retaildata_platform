from pyspark.sql import SparkSession


def test_silver_customer_transformation_regression():
    spark = SparkSession.builder.getOrCreate()
    df = spark.table("retaildata_platform.silver.customers")

    expected_columns = [
        "customer_id", "first_name", "last_name", "tax_id", "country",
        "city", "postcode", "units_purchased", "loyalty_segment", "last_update_ts",
    ]
    for column in expected_columns:
        assert column in df.columns, f"Regression detected: missing column '{column}'"

    schema = {f.name: f.dataType.simpleString() for f in df.schema.fields}
    # Silver config casts these to "long", which Spark reports as "bigint"
    assert schema["customer_id"] == "bigint"
    assert schema["first_name"] == "string"
    assert schema["last_name"] == "string"
    assert schema["units_purchased"] == "bigint"
    assert schema["last_update_ts"] == "timestamp"

    assert df.count() > 0, "Regression detected: Silver customers table is empty"