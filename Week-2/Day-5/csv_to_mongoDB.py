import pandas as pd
from pymongo import MongoClient

def csv_to_mongodb(csv_file):
    try:
        # Read CSV data using Pandas
        df = pd.read_csv(csv_file)
        print("CSV file loaded. Number of records:", len(df))
    except Exception as e:
        print(f"Failed to load CSV file: {e}")
        return

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["training_db"]
    collection = db["csv_data"]

    # Convert DataFrame rows to dictionary records and insert them
    records = df.to_dict(orient="records")
    try:
        result = collection.insert_many(records)
        print("Inserted document ids:", result.inserted_ids)
    except Exception as e:
        print(f"Error inserting documents: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    csv_to_mongodb("sample_data.csv")
