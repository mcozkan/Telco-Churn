##################################### LIBRARIES #######################################
import pandas as pd
import numpy as np
import os
import shutil

from sklearn.model_selection import train_test_split


##################################### DIRECTORY TRANSACTIONS #######################################

# Defines the source and target_paths

"""
source_path = "/Users/etmco/MiuulDS20_Course/datasets/churn.csv"
dataset_name = "churn.csv"
target_path = "data/raw"
# Full target path create
full_target_path = os.path.join(target_path, dataset_name)
"""

def create_directory(target_path):
    """
    :param target_path:
    Checks and creates directory if it doesn't exist
    """
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"'{target_path}' File Created!!!")
    else :
        print(f"'{target_path}' File Already Exists!!!")

def load_data(target_path, dataset_name, source_path):
    """
    Copies the source dataset and samples it accordingly
    :param target_path:
    :param dataset_name:
    :param source_path:
    :return:
    """
    full_target_path = os.path.join(target_path, dataset_name)
    if not os.path.exists(full_target_path):
        if os.path.exists(source_path):
            shutil.copyfile(source_path, full_target_path)
            print(f"File is copied to this path..: {full_target_path}")
        else:
            print(f"Source file did not found!!!: {source_path}")
    else:
        print("File is already exist!!!")

    df = pd.read_csv(full_target_path)
    return df


##################################### XXXXX XXXXX #######################################

#########################################################################################
if __name__ == "__main__":
    create_directory(target_path)
    df = load_data(target_path, dataset_name, source_path)
    # Check data if it is successfully loaded and show first 5 rows
    if df is not None:
        print("DataFrame Created!!!")
    else:
        print("DataFrame Not Created!!!")
