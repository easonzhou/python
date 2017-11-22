# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:47:11 2017

@purpose: loading csv files and check whether the number of columns of each row are equal. 
For those are abnormal, record the line number and number of columns into a csv file

@author: yinsheng.zhou
"""
import numpy as np
import pandas as pd

filename = "PROD_SG_OADCTF_EAS_20171119.txt.csv"
DELIMITER = ","
target_num = 77

cnts = []
columns = []

with open(filename, encoding="utf8") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        num_columns = len(line.split(DELIMITER))
        if num_columns != target_num:
            print("Line {}: {}".format(cnt, num_columns))
            cnts.append(cnt)
            columns.append(num_columns)
        line = fp.readline()
        cnt += 1
        
my_2darray = np.array([cnts, columns])
file = pd.DataFrame(my_2darray)
file.transpose()
file = file.transpose()
file.to_csv(filename + '_corrupted_rows.csv', index=False, header=["line_number", "number_columns"])