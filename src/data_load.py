
from utils_data import create_directory, load_data

source_path = "/Users/etmco/MiuulDS20_Course/datasets/churn.csv"
dataset_name = "churn.csv"
target_path = "data/raw"

# 1. Creates target path
create_directory(target_path)

# 2. Loading data to target path
df = load_data(target_path, dataset_name, source_path)



if __name__ == "__main__":
    # Check data if it is successfully loaded and show first 5 rows
    if df is not None:
        print("DataFrame Loaded!!!")
        print(df.head(20))
    else:
        print("DataFrame Not Loaded, Warning, Check Data!!!")