from validate_email import validate_email
from dateutil import parser


class PreProcessData():
    def __init__(self, df):
        self.data_frame = df

    def validate_email(self, column_name):
        """
        check email function using validate_email lib
        """
        false_index = []
        new_df = self.data_frame[~self.data_frame[column_name].isnull()]
        validated_df = new_df[new_df[column_name].apply(
            validate_email)]
        for index, row in new_df.iterrows():
            if index not in validated_df.index:
                false_index.append([index, row[column_name]])
        if new_df.shape[0] > 0 and validated_df.shape[0]/new_df.shape[0] >= 0.9:
            print("Column {} la truong email".format(column_name))
            print("index va gia tri loi: ", *false_index)

    def datetime_validate(self, column_name):
        new_df = self.data_frame[~self.data_frame[column_name].isnull()]
        cnt = 0
        false_index = []
        for index, row in new_df.iterrows():
            try:
                parser.parse(row[column_name])
                cnt += 1
            except:
                false_index.append([index, row[column_name]])
        if cnt > 0 and cnt/new_df[column_name].shape[0] >= 0.9:
            print("Column {} la truong ngay thang".format(column_name))
            print("index va gia tri loi: ", *false_index)

    def numeric_validate(self, column_name):
        new_df = self.data_frame[~self.data_frame[column_name].isnull()]
        check_list = new_df[column_name].str.isnumeric()
        count = 0
        false_index = []
        for index, row in new_df.iterrows():
            if check_list[index] == True:
                count += 1
            else:
                false_index.append([index, row[column_name]])
        if count > 0 and count/len(check_list) >= 0.9:
            print("Column {} la truong so".format(column_name))
            print("index loi: ", *false_index)

    # def numeric_validate1(self, column_name):
    #     check_list = self.data_frame[column_name].str.isnumeric()
    #     count = 0
    #     false_index = []
    #     null = 0
    #     for index, row in self.data_frame.iterrows():
    #         if check_list[index] == True:
    #             count += 1
    #         elif str(check_list[index]) is 'nan':
    #             null += 1
    #         else:
    #             false_index.append([index, row[column_name]])
    #     if count > 0 and (count+null)/len(check_list) >= 0.9:
    #         print("Column {} la truong so".format(column_name))
    #         print("index loi: ", *false_index)