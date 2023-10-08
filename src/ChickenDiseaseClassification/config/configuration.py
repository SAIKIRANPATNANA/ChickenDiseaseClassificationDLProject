from ChickenDiseaseClassification.constants import *
from ChickenDiseaseClassification.utils.common import read_yaml,create_directories
from ChickenDiseaseClassification.entity.config_entity import DataIngestionConfig
from ChickenDiseaseClassification.entity.config_entity import BaseModelPrepConfig

class ConfigurationManager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])
    def getDataIngestionConfig(self)->DataIngestionConfig:
        config  = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(root_dir = config.root_dir, source_url = config.source_url, local_data_file = config.local_data_file, unzip_dir = config.unzip_dir)
        return data_ingestion_config
    def GetBaseModelPrepConfig(self)->BaseModelPrepConfig:
        config = self.config.base_model_prep
        params = self.params
        create_directories([config.root_dir])
        base_model_prep_config = BaseModelPrepConfig(
        root_dir = config.root_dir,
        base_model_path = config.base_model_path,
        updated_base_model_path=config.updated_base_model_path,
        params_image_size = params.IMAGE_SIZE,
        params_learning_rate = params.LEARNING_RATE,
        params_include_top = params.INCLUDE_TOP,
        params_weights = params.WEIGHTS,
        params_classes = params.CLASSES
        )
        return base_model_prep_config
