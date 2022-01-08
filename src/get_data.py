# The script will implement reading param.yaml file and 
# get data from mentioned data source in yaml file configuration

import os
import yaml
import pandas as pd 
import argparse


#read parameters from config file(here params.yaml)
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


#get data using data source configuration available in config file
def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]['csv_source']
    df = pd.read_csv(data_path,sep=",",encoding="utf-8")
    return df


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)