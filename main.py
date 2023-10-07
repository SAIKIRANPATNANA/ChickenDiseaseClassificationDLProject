from ChickenDiseaseClassification import logger
# logger.info("Welcome to my custom log")
from ChickenDiseaseClassification.pipeline.stage_01_dataingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"
try: 
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<< \n\n =====X=====")
except Exception as e:
    logger.exception(e)
    raise e
    


