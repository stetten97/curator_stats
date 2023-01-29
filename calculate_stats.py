# python script to calculate statistics of metadata curation so far
import os
import yaml
from yaml.loader import SafeLoader
import argparse
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
    
    return parser.parse_args()

def load_config(config_path):
    """loading of config file"""
    with open(config_path, "r") as config:
        try:
            config_data = yaml.load(config, Loader=SafeLoader)
            return config_data
        except yaml.YAMLError as e:
            print(e)

def define_paths(study: str, config_data: dict):
    study_path = f"{config_data['base_dir']}{study}/"
    template_path = f"{study_path}{config_data['concat_dirs']['filled_templates']}"
    template_file = f"{template_path}{study}_filled_sample_template.tsv"

    return template_file

def parse_data(template, header_len: int):
    """data_import and information extraction from study subdirectories"""
    with open(template) as tsvfile:
        tsv_reader = csv.reader(tsvfile, delimiter="\t")
        for line in tsv_reader:
            if line[0] == "## Study code:":
                study_code = line[-1]
                print(study_code)
                study_year = study_code.split("_")[1]
                break
    return study_code, study_year

def calculate_stats():
    """function that calcutates statistics of interests"""
    pass

def main(args):
    """main function that iterates though all study subdirectories and calculates statistics"""
    config_data = load_config("config.yaml")

    # check if study option is set and eventually only process specified study
    if args.study is not None:
        ### all of this should be included inside a different function or the StudyImporter Class
        template_filename = define_paths(args.study, config_data)
        study_code, study_year = parse_data(template_filename, config_data['header_len'])
        print(study_code, study_year)
    
    else:
        for study in os.listdir(config_data["base_dir"]):
            template_filename = define_paths(study, config_data)
            if os.path.isfile(template_filename):
                study_code, study_year = parse_data(template_filename, config_data['header_len'])
                print(study_code, study_year)
            


if __name__ == "__main__":
    description = "Python script to calculate base statistics on Metadata Curation Job"
    args = parse_args(description)

    main(args)