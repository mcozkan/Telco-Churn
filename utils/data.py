##################################### LIBRARIES #######################################
import pandas as pd
import numpy as np
import os
import shutil


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

def load_data(target_path, source_path):
    """
    Copies the source dataset and samples it accordingly
    :param target_path:
    :param dataset_name:
    :param source_path:
    :return:
    """
    #concats the path and new file name
    new_file_name = "telco_churn.csv"
    final_target_path = os.path.join(target_path, new_file_name)

    if not os.path.exists(final_target_path):
        if os.path.exists(source_path):
            shutil.copyfile(source_path, final_target_path)
            print(f"File is copied to this path and renamed to..: {final_target_path}")
        else:
            print(f"Source file did not found!!!: {source_path}")
            return None #Don't try to read the file and return None...
    else:
        print(f"File is already exist!!! {source_path}")

    try:
        df = pd.read_csv(final_target_path)
        return df
    except Exception as e:
        print(f"Error While Reading the CSV: {e}")
        return None



##################################### Data Profiling #######################################

def data_profile(dataframe):
    print(f"Data Columns..:\n  {dataframe.columns.to_list()}")
    print(f"{'#'*100}")
    print(f"Dataframe row count..:\n {dataframe.shape[0]}")
    print(f"{'#' * 100}")
    print(f"Dataframe column count..:\n  {dataframe.shape[1]}")
    print(f"{'#' * 100}")
    print(f"Dataframe describe..:\n  {dataframe.describe()}")
    print(f"{'#' * 100}")
    print(f"Dataframe info..:\n  {dataframe.info}")
    print(f"{'#' * 100}")

    analysis_df = pd.DataFrame({
        'Null Count' : dataframe.isnull().sum(),
        'Null Ratio' : (dataframe.isnull().sum()/len(dataframe) * 100).round(4),
        'Unique Counts' : dataframe.nunique(),
        'Dtypes' : dataframe.dtypes
    })
    print("Null & Unique Value Analysis:")
    print(analysis_df)

    print(f"\n{'=' * 30} DATA PROFILING END {'=' * 30}\n")



#########################################################################################
if __name__ == "__main__":
    source_path = "/Users/etmco/MiuulDS20_Course/datasets/churn.csv"
    dataset_name = "churn.csv"
    target_path = "data/raw"
    create_directory(target_path)
    df = load_data(target_path, source_path)
    # Check data if it is successfully loaded and show first 5 rows
    if df is not None:
        print("DataFrame Created!!!")
    else:
        print("DataFrame Not Created!!!")

    if df is not None:
        print("Dataframe Loaded Successfully!!!")
        data_profile(df)
    else:
        print("CRITICAL ERROR!!! :\n Dataframe Not Created!!! \n PROFILING SKIPPED!!! ")
