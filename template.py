# for creating folder structure 
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "chestCancerClassifierDVC"

list_of_files = [
    ".github/workflows/.gitkeep",  # empty folder can upload in git repo
    f"src/{project_name}/__init__.py", # constructor file for helping to create local package
    f"src/{project_name}/components/__init__.py",  # data ingestion, transformation, validation, model trainer
    f"src/{project_name}/utils/__init__.py",  # for common function
    f"src/{project_name}/config/__init__.py", # creating configuration
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",  # before implementing modular coding 
    "templates/index.html"  # for user ui creation


]



for filepath in list_of_files:
    filepath = Path(filepath)  # for auto reconises os and path
    filedir, filename = os.path.split(filepath)  # extracing separate file and folder


    if filedir !="":  # for creation folder
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # for checking file is Empty or Not
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")