# python script to calculate statistics of metadata curation so far
import os
import yaml
from yaml.loader import SafeLoader
import argparse
import pandas as pd
import csv

class Study:
    """Study object that holds basic information of interest for a specific study"""
    def __init__(self, study_code, year, study_type, count) -> None:
        self.study_code = study_code
        self.study_year = study_year
        self.sample_count = sample_count

def parse_args(description):
    parser = argparse.ArgumentParser(description=description)
    
    parser.add_argument("-s", "--study",
                        type=str, 
                        help="Option to run the script only on one specific study")
    
    parser.add_argument("search_str",
                        type=str,
                        help="String that is used to search for in filenames")
    
    return parser.parse_args()

def load_config(config_path):
    """loading of config file"""
    with open(config_path, "r") as config:
        try:
            config_data = yaml.load(config, Loader=SafeLoader)
            return config_data
        except yaml.YAMLError as e:
            print(e)

def get_filepaths(base_dir, search_str):
    """
    Function to get all files with specific substring in name.
    Search base directory and all sub-directories.
    Return a list of absolute filepaths
    """
    filepaths = []
    for root, dirs, files in os.walk(base_dir):
        for file in [fname for fname in files if search_str in fname]:
            filepaths.append(os.path.join(root, file))
    
    if len(filepaths) > 1:
        return filepaths
    else:
        return filepaths[0]

def define_paths(study: str, config_data: dict):
    study_path = f"{config_data['base_dir']}{study}/"
    template_path = f"{study_path}{config_data['concat_dirs']['filled_templates']}"
    template_file = f"{template_path}{study}_filled_sample_template.tsv"

    return template_file

def parse_data(template, header_len: int):
    """data_import and information extraction from study subdirectories"""
    # with open(template) as tsvfile:
    #     tsv_reader = csv.reader(tsvfile, delimiter="\t")
    #     for line in tsv_reader:
    #         if line[0] == "## Study code:":
    #             study_code = line[-1]
    #             print(study_code)
    #             study_year = study_code.split("_")[1]
    #             break
    # return study_code, study_year
    template = pd.read_csv(template,
                           sep="\t",
                           skiprows=header_len)
    
    return len(template)

def calculate_stats():
    """function that calcutates statistics of interests"""
    pass

def main(args):
    """main function that iterates though all study subdirectories and calculates statistics"""
    config_data = load_config("config.yaml")

    # check if study option is set and eventually only process specified study
    if args.study is not None:
        ### all of this should be included inside a different function or the StudyImporter Class
        study_dir = f"{config_data['base_dir']}{args.study}"

        filepath = get_filepaths(study_dir, args.search_str)

        # get len of specific file
        parse_data(filepath, config_data['header_len'])
        # template_filename = define_paths(args.study, config_data)
        # study_code, study_year = parse_data(template_filename, config_data['header_len'])
        # print(study_code, study_year)
    
    else:
        base_dir = f"{config_data['base_dir']}"
        filepaths = get_filepaths(base_dir, args.search_str)
        
if __name__ == "__main__":
    description = "Python script to calculate base statistics on Metadata Curation Job"
    args = parse_args(description)

    main(args)