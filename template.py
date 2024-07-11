import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:') 

project_name="textSummerizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/traials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    #split files and folders
    fildir,filename=os.path.split(filepath)

    #check if file exists
    if fildir != "":
        os.makedirs(fildir, exist_ok=True)
        logging.info(f"Created directory: {fildir}")

    if (not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Create empty file: {filepath}")

    else:
        logging.info(f"File {filename} already exists.")