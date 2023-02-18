import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://amiarnab:amiarnab100@cluster0.fugun.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "F:\ML project end to end\Insurence-premium-prediction\insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns: {df.shape}")

    df.reset_index(drop = True,inplace = True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)