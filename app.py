from insurance.entity import artifact_entity,config_entity
from insurance.components.data_ingestion import DataIngestion
import pandas as pd


class DataValidation:


    def __init__(self,
                    data_validation_config:config_entity.DataValidationConfig,
                    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            #logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.validation_error=dict()
        except Exception as e:
            print(e)
            #raise insuranceException(e, sys)
        

    def data_read(self):
        train_df = pd.read_csv(filepath_or_buffer=self.data_ingestion_artifact.train_file_path)
        print(train_df.columns)
training_pipeline_config = config_entity.TrainingPipelineConfig()
data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
data_ingestion_artifact = data_ingestion.Initiate_data_ingestion()

data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config) 
data_validation = DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)

data_validation.data_read()