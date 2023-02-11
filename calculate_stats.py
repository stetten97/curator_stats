# python script to calculate statistics of metadata curation so far
import os
from os.path import dirname, realpath
import sys
import yaml
from yaml.loader import SafeLoader
import argparse
import pandas as pd

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

def parse_data(template, header_len: int):
    """data_import and information extraction from study subdirectories"""
    template = pd.read_csv(template,
                           sep="\t",
                           skiprows=header_len)
    
    return len(template)

def main(args):
    """main function that iterates though all study subdirectories and calculates statistics"""
    yaml_path = realpath(__file__).rsplit("/", 1)[0] + "/config.yaml"
    config_data = load_config(yaml_path)

    # check if study option is set and eventually only process specified study
    if args.study is not None:
        ### all of this should be included inside a different function or the StudyImporter Class
        study_dir = f"{config_data['base_dir']}{args.study}"

        filepath = get_filepaths(study_dir, args.search_str)

        # get len of specific file
        source = args.study
        row_count = parse_data(filepath, config_data['header_len'])
    
    else:
        base_dir = f"{config_data['base_dir']}"
        filepaths = get_filepaths(base_dir, args.search_str)

        source = config_data['base_dir']
        row_count = int()
        for path in filepaths:
            row_count += parse_data(path, config_data['header_len'])
    

    stats = f"""
    Total number of rows in {source}: {row_count}
    """

    return stats
        
if __name__ == "__main__":
    description = "Python script to calculate base statistics on Metadata Curation Job"
    args = parse_args(description)

    stats = main(args)
    print(stats)