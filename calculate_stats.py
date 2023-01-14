# python script to calculate statistics of metadata curation so far
import os
import yaml
from yaml.loader import SafeLoader
import argparse

class Study():
    """Study object that holds basic information of interest for a specific study"""
    def __init__(self) -> None:
        self.study_code = study_code
        pass
    pass

class StudyImporter():
    """
    A potential Importer Object.
    
    Could be used to properly check for and read in data of interest for studies.
    """
    pass

def parse_args(description):
    parser = argparse.ArgumentParser(description=description)
    
    parser.add_argument("-s", "--study",
                        type=str, 
                        help="Option to run the script only on one specific study")
    
    return parser.parse_args()

def load_config(config_path):
    """loading of config file"""
    with open(config_path, "r") as config:
        try:
            config_data = yaml.load(config, Loader=SafeLoader)
            return config_data
        except yaml.YAMLError as e:
            print(e)

def import_data(file_path):
    """data_import and information extraction from study subdirectories"""
    with open(file_path, "r") as f:
        num_lines = sum(_ for _ in f)
    return num_lines

def calculate_stats():
    """function that calcutates statistics of interests"""
    pass

def main(args):
    """main function that iterates though all study subdirectories and calculates statistics"""
    config_data = load_config("config.yaml")
    print(config_data)
    pass
    # check if study option is set and eventually only process specified study
    if args.study is not None:
        ### all of this should be included inside a different function or the StudyImporter Class
        study_path = f"{config_data['base_dir']}{args.study}/"
        template_path = f"{study_path}{config_data['concat_dirs']['filled_templates']}"
        print(template_path)
    pass

if __name__ == "__main__":
    description = "Python script to calculate base statistics on Metadata Curation Job"
    args = parse_args(description)

    main(args)