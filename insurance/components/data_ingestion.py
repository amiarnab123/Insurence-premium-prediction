import pandas as pd
import numpy as np
import os,sys
from insurance.entity import config_entity
from insurance.exception import insuranceException
from insurance.logger import logging
from insurance.entity import artifact_entity
from insurance import utils
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self, data_ingestion_config: config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise insuranceException
        
    def Initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"Export collection data as pandas dataframe")
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name = self.data_ingestion_config.database_name,
                collection_name = self.data_ingestion_config.collection_name
            )
            logging.info(f"save data in feature store")

            # replacing nan value
            df.replace("na",np.NaN,inplace=True)

            # save data in feature store
            logging.info(f"create feature store folder if not avalaible")
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)

            # save data to the feature store folder
            logging.info(f"save df to feature store folder")
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=True)

            # splitting the data into train test split
            logging.info(f"splitting the datasets into train and test set")
            train_df,test_df = train_test_split(df,test_size=self.data_ingestion_config.test_size,random_state=42)

            # creating dataset directory
            logging.info(f"create dataset directory if not exists")
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True)

            # saving train and test data to the dataset folder
            logging.info("save train and test data to the dataset folder")
            train_df.to_csv(path_or_buf = self.data_ingestion_config.train_file_path,index = False,header = True)
            test_df.to_csv(path_or_buf = self.data_ingestion_config.test_file_path,index = False,header = True)

            # prepare artifact folder
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path = self.data_ingestion_config.feature_store_file_path,
                train_file_path = self.data_ingestion_config.train_file_path,
                test_file_path = self.data_ingestion_config.test_file_path
            )


        except Exception as e:
            raise insuranceException(error_message = e, error_detail = sys)
