# from setting.get_conf import Config
import pandas as pd
from script.aPhu.preprocess_data import PreProcessData
from script.aPhu.get_config import Config

def main():
    df = pd.read_csv('input/input.csv')
    columns = list(df.columns)
    process_obj = PreProcessData(df)
    for column in columns:
        process_obj.validate_email(column)
        process_obj.numeric_validate(column)
        process_obj.datetime_validate(column)


if __name__ == "__main__":
    # main()
    config = Config()
    config.get_init()
    print(config.common_err)

