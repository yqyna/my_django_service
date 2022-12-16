# -*- coding:utf-8 -*-
# @FileName  :use_pandas_example.py
# @Time      :2022/12/16 11:03
# @Author    : yuhaiping
import pandas as pd


def read_excel_data(file_path):
    """
    读取Excel数据

    :param file_path:
    :return:
    """

    df = pd.read_excel(file_path)
    print(df.shape[0])
    print(df)
    return df


if __name__ == '__main__':

    _file_path = r"C:\Users\Administrator\Desktop\data.xlsx"
    data = read_excel_data(_file_path)
    print(data["id"].to_list())

