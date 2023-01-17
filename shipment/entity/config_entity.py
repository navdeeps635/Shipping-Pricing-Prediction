import os,sys
from datetime import datetime
from shipment.exception import ShipmentException
from shipment.logger import logging


file_name = 'shipment.csv'
train_file_name = 'train.csv'
test_file_name = 'test.csv'
input_transformer_object_file_name = "input_transformer.pkl"
target_transformer_object_file_name = "target_transformer.pkl"
model_file_name = "model.pkl"


#create a training pipeline route to store information of subsequent steps in it.
class TrainingPipelineConfig:
    
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}")
        
        except Exception as e:
            raise ShipmentException(e,sys)
    
class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        
        try:
            self.database_name = "project"
            self.collection_name = "shipment"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",file_name)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"Dataset",train_file_name)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"Dataset",test_file_name)
            self.test_size = 0.2

        except Exception as e:
            raise ShipmentException(e,sys)


class DataValidationConfig:
    
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        
        try:
            self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
            self.report_file_path = os.path.join(self.data_validation_dir,"report.yaml")
            self.missing_threshold = 0.7
            self.base_file_path = os.path.join("SCMS_Delivery_History.csv")
            
        except Exception as e:
            raise ShipmentException(e,sys)

class DataTransformationConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        
        try:
            self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_transformation")
            self.tranformed_train_path = os.path.join(self.data_transformation_dir,"transformed_npfiles",train_file_name.replace(".csv",".npz"))
            self.tranformed_test_path = os.path.join(self.data_transformation_dir,"transformed_npfiles",test_file_name.replace(".csv",".npz"))
            self.input_transformer_object_path = os.path.join(self.data_transformation_dir,"input_transformer",input_transformer_object_file_name)
            self.target_transformer_object_path = os.path.join(self.data_transformation_dir,"target_transformer",target_transformer_object_file_name)
            
        except Exception as e:
            raise ShipmentException(e,sys)

class ModelTrainerConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        
        try:
            self.model_trainer_dir = os.path.join(training_pipeline_config.artifact_dir,"model_trainer")
            self.model_path = os.path.join(self.model_trainer_dir,"model",model_file_name)
            self.expected_score = 0.8
            self.overfitting_threshold = 0.1

        except Exception as e:
            raise ShipmentException(e,sys)

class ModelEvaluationConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.change_threshold = 0.01

        except Exception as e:
            raise ShipmentException(e, sys)

class ModelPusherConfig:...