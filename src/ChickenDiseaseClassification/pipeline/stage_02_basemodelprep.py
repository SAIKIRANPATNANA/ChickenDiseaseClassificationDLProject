from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.components.basemodelprep import BaseModelPrep

STAGE_NAME = "Base Model Prep Stage"
class BaseModelPrepPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            base_model_prep_config = config.GetBaseModelPrepConfig()
            base_model_prep = BaseModelPrep(config=base_model_prep_config)
            base_model_prep.get_base_model()
            base_model_prep.update_base_model()
        except Exception as e:
            raise e
if __name__ == "__main__":
    try: 
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj =  BaseModelPrepPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed")
    except Exception as e:
        raise e