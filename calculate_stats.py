# python script to calculate statistics of metadata curation so far
import os
import yaml
from yaml.loader import SafeLoader

class Study():
    """Study object that holds basic information of interest for a specific study in the target directory"""
    def __init__(self) -> None:
        self.study_code = study_code
        pass

    pass

def load_config(config_path):
    """loading of config file"""
    with open(config_path, "r") as config:
        try:
            config_data = yaml.load(config, Loader=SafeLoader)
        except yaml.YAMLError as e:
            print(e)


def get_data(file_path):
    """data_import and information extraction from study subdirectories"""
    with open(file_path, "r") as f:
        num_lines = sum(_ for _ in f)
    return num_lines

def calculate_stats():
    """function that calcutates statistics of interests"""
    pass

def main():
    """main function that iterates though all study subdirectories and calculates statistics"""
    config_data = load_config("config.yaml")

    pass

if __name__ == "__main__":
    main()
