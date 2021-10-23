# file main.py
import pandas as pd
import argparse
from setting.config import Config
from script.Check_and_count_error import CheckAndCountError


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-in", "--input_directory", type=str, default=Config.DEFAULT_INPUT,
                        help="It is directory of csv file")
    opt = parser.parse_args()

    # read file csv
    list_data = pd.read_csv(opt.input_directory, encoding="utf-8")
    # check error
    CheckAndCountError.check_error(list_data)
