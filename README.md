# chestCancerClassificationDVC

# create repository "chestCancerClassificationDVC" with README.md, MIT licence, .gitignore(python)

# in cmd file location git clone
- git clone https://github.com/maheshpachpande/chestCancerClassificationDVC.git
- cd chestCancerClassificationDVC
- code . 

# create the template.py file
- python template.py

# create the vitual enviroment
- conda create -p chest python==3.8 -y

# activate the virtual enviroment
- conda activate C:\Users\pachp\Desktop\project_git\chestCancerClassificationDVC\chest

# deactivate the virtual enviroment
- conda deactivate

# set setup.py

# which lib is requires to execute the project add in requirements.txt
- pip install -r requirements.txt

# create the logging, exception

# construct utils.py

# reaseach
- 01_data_ingestion.ipynb
-02_prepare_base_model.ipynb

# WorkFlows in each research ipynb file
- Update config.yaml
- Update secrets.yaml [Optional] (use for userid or password)
- Update params.yaml  (define model related parameter)
- Update the entity    
- Update the configuration manager in src config
- Update the components (use for data-ingestion, model trainig, model evolution)
- Update the pipeline
- Update the main.py
- Update the dvc.yaml

# dagshub ui
- MLFLOW_TRACKING_URI=https://dagshub.com/pachpandemahesh300/chestCancerClassificationDVC.mlflow \
- MLFLOW_TRACKING_USERNAME=pachpandemahesh300 \
- MLFLOW_TRACKING_PASSWORD=9f73334e82cb0e1dc7693e6eed2b0827c86e8db9 \
- python script.py