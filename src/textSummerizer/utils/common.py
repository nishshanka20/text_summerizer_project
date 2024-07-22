# python functions frequently used in the project
import os
from box.exceptions import BoxValueError
import yaml
from textSummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """read yaml file and returns
    Args:
        path_to_yaml (str):path like input
        
    Raises:
        ValueError: if yaml ile is empty
        e:empty file
    Returns:
        ConfigBox: returns the yaml file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create list of directories
    
    Args:
        path_to_directories (list): list of path of create_directories
        ignore_log(bool,optinal): ignore if multiple dirs is to be created;default is false.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory:{path}")


@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB
    Args:
        path (str):path of file
        
    Returns:
        str: size of file in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"
    