from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification.components.dataingestion import DataIngestion
from ChickenDiseaseClassification import logger

STAGE_NAME = "Data Ingestion Stage"
class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        try: 
            config = ConfigurationManager()
            data_ingestion_config = config.getDataIngestionConfig()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e 

if __name__ == "__main__":
    try: 
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed")
    except Exception as e:
        raise e



