from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.components.modelevaluation import ModelEvaluation


STAGE_NAME = 'Model Evaluation'

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.GetModelEvaluationConfig()
            model_evaluation  = ModelEvaluation(model_evaluation_config)
            model_evaluation.evaluation()
            model_evaluation.save_score()
        except Exception as e:
            raise e
if __name__ == "__main__":
    try: 
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj =  ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed")
    except Exception as e:
        raise e