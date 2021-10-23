# file main.py
import pandas as pd
import argparse
from dateutil.parser import parse
import re
from setting.config import Config


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-in", "--input_directory", type=str, default=Config.DEFAULT_INPUT,
                        help="It is directory of csv file")
    opt = parser.parse_args()

    # read file csv
    list_data = pd.read_csv(opt.input_directory, encoding="utf-8")

    for column in list_data.columns:
        print(f"************ In column {column} ************")
        count_email = 0
        count_date = 0
        count_number = 0
        column_not_null = 0
        data_type = ""
        for index in range(0, list_data.shape[0], 1):
            if str(list_data.loc[index, column]) != "nan":
                column_not_null += 1
                # Check number
                if re.fullmatch(Config.regex_number_int, str(list_data.loc[index, column])):
                    count_number += 1
                    continue
                # Check mail
                if re.fullmatch(Config.regex_mail, str(list_data.loc[index, column])):
                    count_email += 1
                    continue
                # Check date
                try:
                    parse(str(list_data.loc[index, column]))
                    result = True
                except ValueError:
                    result = False
                if result:
                    count_date += 1
                    continue

        if (count_email > count_number
                and count_email > count_date
                and count_email/list_data.shape[0] >= 0.9):
            data_type = "email"
        elif count_number > count_date and count_number/column_not_null >= 0.9:
            data_type = "number"
        elif count_date/column_not_null >= 0.9:
            data_type = "date"
        else:
            data_type = "unknow"
        print(f"Data type in {column} is: " + data_type)

        # Part 2 count error
        count_error = 0
        for index in range(0, list_data.shape[0], 1):
            # Check mail error
            if data_type == "email":
                if str(list_data.loc[index, column]) != "nan":
                    if not re.fullmatch(Config.regex_mail, str(list_data.loc[index, column])):
                        count_error += 1
                        print(f"Error mail format in line {index}! Error value: {list_data.loc[index, column]}")

            # Check date error
            if data_type == "date":
                if str(list_data.loc[index, column]) != "nan":
                    try:
                        parse(str(list_data.loc[index, column]))
                        result = True
                    except ValueError:
                        result = False
                    if not result:
                        count_error += 1
                        print(f"Error date in line {index}! Error value: {list_data.loc[index, column]}")

            # Check number error
            if data_type == "number":
                if str(list_data.loc[index, column]) != "nan":
                    if not re.fullmatch(Config.regex_number_int, str(list_data.loc[index, column])):
                        count_error += 1
                        print(f"Error number format in line {index}! Error value: {list_data.loc[index, column]}")
        # consume
        print(f"Error in column {column} is: {count_error}")