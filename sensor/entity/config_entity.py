import os,sys
from sensor.exception import SensorException
from sensor.logger import logging
from datatime import datetime 

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME + "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(), "atrifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")

        except Exception as e:
            
            
            class DataIngestionConfig:

    def __init__(self, training_pipeline_Config:TrainingPipelineConfig):
        self.database_name = "aps
        self.collection_name = "sensor"
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir, "feature_store")
        self.train_file_path = os.path.join(self.data_ingestion_dir, "dataset" ,TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset", TEST_FILE_NAME)
        self.test_size = 



    def to_dict() ->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e, sys)

         
        
class DataValidationConfig:


class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...
