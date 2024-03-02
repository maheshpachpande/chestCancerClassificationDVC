from chestCancerClassifierDVC.constants import *
from chestCancerClassifierDVC.entity.config_entity import (DataIngestionConfig)
from chestCancerClassifierDVC.utils.common_utils import read_yaml, create_directories

# configuration
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,  # redirect the path from constant.yaml
        params_filepath = PARAMS_FILE_PATH):

        # read yaml through path and store it
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # create artifacts root
        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # config value store here
        config = self.config.data_ingestion

        # create the root dir
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            # initialize configuration
            root_dir=config.root_dir,# where to store
            source_URL=config.source_URL, # url of google drive 
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config