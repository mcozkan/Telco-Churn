import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *

source_path = "/Users/etmco/MiuulDS20_Course/datasets/churn.csv"
dataset_name = "churn.csv"
target_path = "data/raw"

# 1. Creates target path
create_directory(target_path)

# 2. Loading data to target path
df = load_data(target_path, dataset_name, source_path)

print(df.head(20))