from dateutil.parser import parse
import re
from setting.config import Config


class CheckAndCountError:

    def check_error(list_data):
        """
        :param list_data: list read from csv
        :return: same form:
        ************ In column 'No2' ************
        Data type in 'No2' column is: date
        In line 26! Error value: 345vbcx
        Have 1 error
        """
        for column in list_data.columns:
            print(f"************ In column '{column}' ************")
            count_email = 0
            count_date = 0
            count_number = 0
            column_not_null = 0
            # Part 1: count data type
            for index in range(0, list_data.shape[0], 1):
                if str(list_data.loc[index, column]) != "nan":
                    column_not_null += 1
                    # Check number
                    # if re.fullmatch(r'[0-9]*', str(list_data.loc[index, column])):
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
                        count_date += 1
                    except ValueError:
                        continue

            # Part 2: check data type
            if (count_email > count_number
                    and count_email > count_date
                    and count_email / column_not_null >= 0.9):
                data_type = "email"
            elif count_number > count_date and count_number / column_not_null >= 0.9:
                data_type = "number"
            elif count_date / column_not_null >= 0.9:
                data_type = "date"
            else:
                data_type = "unknown"
            print(f"Data type in '{column}' column is: " + data_type)

            # Part 3: count error
            count_error = 0
            for index in range(0, list_data.shape[0], 1):
                if data_type == "unknown":
                    break
                # Check mail error
                elif data_type == "email":
                    if str(list_data.loc[index, column]) != "nan":
                        if not re.fullmatch(Config.regex_mail, str(list_data.loc[index, column])):
                            count_error += 1
                            print(f"In line {index}! Error value: {list_data.loc[index, column]}")

                # Check date error
                elif data_type == "date":
                    if str(list_data.loc[index, column]) != "nan":
                        try:
                            parse(str(list_data.loc[index, column]))
                            result = True
                        except ValueError:
                            result = False
                        if not result:
                            count_error += 1
                            print(f"In line {index}! Error value: {list_data.loc[index, column]}")

                # Check number error
                elif data_type == "number":
                    if str(list_data.loc[index, column]) != "nan":
                        if not re.fullmatch(Config.regex_number_int, str(list_data.loc[index, column])):
                            count_error += 1
                            print(f"In line {index}! Error value: {list_data.loc[index, column]}")
            # consume
            if data_type != "unknown":
                print(f"Have {count_error} error")
