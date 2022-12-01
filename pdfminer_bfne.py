#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd

from utils import parse_questionnaires

# input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\data\visit_1\bfne'
# output_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\derivatives\visit_1\bfne'

def process_bfne(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'bfne.csv'))

    col_list= ['bfne1','bfne2','bfne3','bfne4','bfne5','bfne6','bfne7','bfne8','bfne9','bfne10','bfne11','bfne12']

    result=[]

    for index, row in df.iterrows():
        s_result = float(row[col_list].sum())
        result.append(s_result)

    df['result']=result
    df.to_csv(os.path.join(data_dir,'bfne_result.csv'),index=False)

if __name__ == '__main__':
    try:
        input_dir = sys.argv[1]
    except:
        print("incorrect arguments")
        sys.exit()
    try:
        output_dir = sys.argv[2]
    except:
        print("incorrect arguments")
        sys.exit()
    os.makedirs(output_dir, exist_ok=True)
    drop_cols=[]
    parse_questionnaires(drop_cols, input_dir, output_dir, 'bfne.csv')
    process_bfne(output_dir)




