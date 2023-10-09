from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.components.callbacksprep import CallBacksPrep
from ChickenDiseaseClassification.components.modeltraining import ModelTraining

STAGE_NAME = 'Model Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            callbacks_prep_config = config.GetCallBacksPrepConfig()
            callbacks_prep = CallBacksPrep(config=callbacks_prep_config)
            callbacks_list = callbacks_prep.get_tb_ckpt_callbacks()
            model_training_config = config.GetModelTrainingConfig()
            model_training = ModelTraining(config=model_training_config)
            model_training.get_base_model()
            model_training.train_valid_generator()
            model_training.train(callbacks_list=callbacks_list)
        except Exception as e:
            raise e