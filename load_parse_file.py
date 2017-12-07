# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:37:06 2017

@author: yinsheng.zhou
"""
import numpy as np
import pandas as pd
import csv

class FileLoader:
    def __init__(self, filename):
        self.filename = filename
        
    def load(self):
        rows = []
        with open(self.filename, encoding="utf-8") as csvfile:
            csvreader = csv.reader(x.replace('\0', '') for x in csvfile)
            for row in csvreader:
                rows.append(row)        
        data = pd.DataFrame(np.array(rows))
        self.df = data
        
mm = FileLoader("PROD_SG_OADCTF_EAS_20171205.txt.csv")   
mm.load();
mm.df.to_csv(mm.filename, index=False);