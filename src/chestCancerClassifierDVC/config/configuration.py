from chestCancerClassifierDVC.constants import *
import os
from chestCancerClassifierDVC.entity.config_entity import (DataIngestionConfig,
                                                           PrepareBaseModelConfig,
                                                           TrainingConfig)
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
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "chestCancerData")
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config