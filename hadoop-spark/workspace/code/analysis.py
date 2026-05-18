import sys
from pathlib import Path

import pyspark
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType
from pyspark.sql.functions import sum, col


######## Question 1 ###############
# Calculer les ventes par magasin
##################################

def sales_by_store(
    spark: SparkSession,
    filepath: str
) -> DataFrame:
    """
    Calculate total sales grouped by store.

    Args:
        spark (SparkSession):
            Active Spark session.

        filepath (str):
            Path to the input CSV dataset.

    Returns:
        DataFrame:
            Spark DataFrame containing total sales by store.
    """

    # Dataset schema
    schema = StructType([
        StructField("date", DateType(), True),
        StructField("temps", StringType(), True),
        StructField("magasin", StringType(), True),
        StructField("produit", StringType(), True),
        StructField("cout", DoubleType(), True),
        StructField("paiement", StringType(), True),
    ])

    # Read dataset
    spark_df = (
        spark.read
        .schema(schema)
        .option("sep", "\t")
        .option("header", False)
        .csv(filepath)
        .toDF(
            "date",
            "temps",
            "magasin",
            "produit",
            "cout",
            "paiement"
        )
    )

    # Aggregate sales by store
    sales = (
        spark_df
        .groupBy("magasin")
        .agg(sum("cout").alias("total_ventes"))
        .orderBy(col("total_ventes").desc())
    )

    return sales


####### Question 2 ##########################
# Calculer les ventes par categorie de produit
##############################################

def sales_by_product(spark: SparkSession, filepath: str ) -> pyspark.sql.DataFrame:
    """
    Calculate total sales by product category.

    Args:
        df (pd.DataFrame): Input dataset.
        filepath (str): Path to the input dataset.

    Returns:
        pd.DataFrame: Total sales grouped by product category.
    """
    # Define the schema for the dataset
    schema = StructType([
        StructField("date", DateType(), True),
        StructField("temps", StringType(), True),
        StructField("magasin", StringType(), True),
        StructField("produit", StringType(), True),
        StructField("cout", DoubleType(), True),
        StructField("paiement", StringType(), True),
])
    # Loads a csv file into a Spark DataFrame with the defined schema
    spark_df = (
        spark.read
        .schema(schema)   
        .option("sep", "\t")
        .option("header", False)   
        .csv(filepath)
        .toDF(
            "date",
            "temps",
            "magasin",
            "produit",
            "cout",
            "paiement"
        )
    )

    # Calculate total sales by product category
    ### your code here 
    sales =""
                         
                         

    return sales

if __name__ == "__main__":

    filepath = Path("datasets/purchases.txt").resolve()
    path = f"file://{filepath}"
    
    # Create a SparkSession
    spark = (
        SparkSession.builder
        .appName("SalesAnalysis")
        .getOrCreate()
    )

    print()
    sales_by_store_result = sales_by_store(spark, filepath=str(path))
    print("Calculer les ventes par magasin:\n")
    sales_by_store_result.show()

    spark.stop()
    sys.exit()

    