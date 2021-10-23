"""Load configuration from .ini file."""
import configparser
import sys

sys.path.append("../script/aPhu")


class Config:
    config = configparser.ConfigParser()
    config.read("setting\\config.ini")

    def __init__(self):
        self.seprate_line = ""
        self.not_inputed = ""
        self.common_err = ""
        self.value_err = ""
        self.input_csv = ""
        self.stock_csv = ""
        self.output_csv = ""
        self.sql_drop = ""
        self.sql_create = ""
        self.sql_insert = ""


    def get_init(self):
        # Get values from our .ini file
        Config.config.get("RANGE", "NOT_INPUTED")
        Config.config.get("DATA_FILE_NAME", "INPUT_CSV")
        Config.config.get("OUTPUT_FILE_NAME", "OUTPUT_CSV")
        Config.config.get("DATA_FILE_NAME", "STOCK_CSV")
        Config.config.get("STRING", "SEPERATE_LINE")
        Config.config.get("ERROR", "COMMON_ERR")
        Config.config.get("ERROR", "VALUE_ERR")
        self.not_inputed = int(Config.config["RANGE"]["NOT_INPUTED"])
        self.input_csv = Config.config["DATA_FILE_NAME"]["INPUT_CSV"]
        self.output_csv = Config.config["OUTPUT_FILE_NAME"]["OUTPUT_CSV"]
        self.stock_csv = Config.config["DATA_FILE_NAME"]["STOCK_CSV"]
        self.seprate_line = Config.config["STRING"]["SEPERATE_LINE"]
        self.common_err = Config.config["ERROR"]["COMMON_ERR"]
        self.value_err = Config.config["ERROR"]["VALUE_ERR"]

    def get_sql_ini(self):
        Config.config.get("SQL", "SQL_DROP")
        Config.config.get("SQL", "SQL_CREATE")
        Config.config.get("SQL", "SQL_INSERT")
        # not_inputed = config["RANGE"]["NOT_INPUTED"]
        self.sql_drop = Config.config["SQL"]["SQL_DROP"]
        self.sql_create = Config.config["SQL"]["SQL_CREATE"]
        self.sql_insert = Config.config["SQL"]["SQL_INSERT"]