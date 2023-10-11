from ChickenDiseaseClassification import logger
# logger.info("Welcome to my custom log")
from ChickenDiseaseClassification.pipeline.stage_01_dataingestion import DataIngestionPipeline
from ChickenDiseaseClassification.pipeline.stage_02_basemodelprep import BaseModelPrepPipeline
from ChickenDiseaseClassification.pipeline.stage_03_modeltraining import ModelTrainingPipeline
from ChickenDiseaseClassification.pipeline.stage_04_modelevaluation import ModelEvaluationPipeline
STAGE_NAME = "Data Ingestion Stage"
try: 
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n =====X=====")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Base Model Prep Stage"
try: 
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    base_model_prep = BaseModelPrepPipeline()
    base_model_prep.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n =====X=====")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Model Training"
try: 
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n =====X=====")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Model Evaluation"
try: 
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_evaluator = ModelEvaluationPipeline()
    model_evaluator.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n =====X=====")
except Exception as e:
    logger.exception(e)
    raise e


