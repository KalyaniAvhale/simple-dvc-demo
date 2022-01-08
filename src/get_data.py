# get param
# process data
# return dataframe 
import os
import yaml
import pandas as pd 
import argparse


if __name__=="main":
    arg = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parsed_args()