import os
import sys
import pandas as pd

project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, project_root)


from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
from google.cloud import storage
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)


class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]   #Here, it means that config.yaml file will be read till "data_ingestion" keyword
        self.bucket_name = self.config["bucket_name"]
        self.bucket_file_names = self.config["bucket_file_names"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestion started with {self.bucket_name} and {self.bucket_file_names}")

    def download_csv_From_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.bucket_file_names:
                file_path = os.path.join(RAW_DIR, file_name)

                if file_name=="animelist.csv":
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    data = pd.read_csv(file_path,nrows=5000000)
                    data.to_csv(file_path,index=False)
                    logger.info("Large file detected Only downloading 5M rows")
                else:
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    logger.info("Downloading Smaller Files ie anime and anime_with synopsis")
        

                logger.info("Datasets ingestion completed")

        except Exception as e:
            logger.error("Error while downloading data from GCP")
            raise CustomException("Data ingestion failed", e)
        
    def run(self):
        try:
            logger.info("Running the data ingestion")
            self.download_csv_From_gcp()
            # self.split_data()
            logger.info("Data Ingestion completed")
        except Exception as ce:
            logger.error(f"CustomException : {str(ce)}")
            
        finally:
            logger.info("Data Ingestion completed")

if __name__ == "__main__":
    config = read_yaml(CONFIG_PATH)
    data_ingestion = DataIngestion(config)
    data_ingestion.run()






