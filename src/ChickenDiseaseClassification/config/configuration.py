from ChickenDiseaseClassification.constants import *
from ChickenDiseaseClassification.utils.common import read_yaml,create_directories
from ChickenDiseaseClassification.entity.config_entity import DataIngestionConfig,BaseModelPrepConfig,CallBacksPrepConfig,ModelTrainingConfig
import os
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
    def GetCallBacksPrepConfig(self)->CallBacksPrepConfig:
        config = self.config.callbacks_prep
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([Path(model_ckpt_dir),Path(config.tensorboard_root_log_dir)])
        callback_prep_config = CallBacksPrepConfig(root_dir=Path(config.root_dir), tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir), checkpoint_model_filepath=Path(config.checkpoint_model_filepath))
        return callback_prep_config
    def GetModelTrainingConfig(self)->ModelTrainingConfig:
        model_training = self.config.model_training
        base_model_prep = self.config.base_model_prep
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chicken-fecal-images")
        create_directories([Path(model_training.root_dir)])
        model_traing_config = ModelTrainingConfig(root_dir=Path(model_training.root_dir), trained_model_path=Path(model_training.trained_model_path),updated_base_model_path=Path(base_model_prep.updated_base_model_path),training_data=Path(training_data), params_epochs=params.EPOCHS, params_batch_size=params.BATCH_SIZE, params_is_augmentation=params.AUGMENTATION, params_image_size=params.IMAGE_SIZE)
        return model_traing_config


    