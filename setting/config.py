# file config
class Config:
    DEFAULT_INPUT = "./input/input.csv"
    DECIMAL_SEPARATOR: str = "."
    Z_SCORE = 1

    # set up regex
    regex_date = r'[0-9]*/[0-9]*/[0-9]{4}'
    regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    regex_number_float = f'[0-9]*\{DECIMAL_SEPARATOR}[0-9]*'
    regex_number_int = r'[0-9]*'
