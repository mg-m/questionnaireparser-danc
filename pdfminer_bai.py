#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd

from utils import parse_questionnaires

# input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\data\visit_1\bai'
# output_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\derivatives\visit_1\bai'

def process_bai(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'bai.csv'))

    col_list= ['bai1','bai2','bai3','bai4','bai5','bai6','bai7','bai8','bai9','bai10','bai11','bai12','bai13','bai14','bai15','bai16','bai17','bai18','bai19','bai20','bai21']

    result=[]

    for index, row in df.iterrows():

        s_result = float(row[col_list].sum())
        result.append(s_result)

        #if result <=21:
        #    print("low anxiety")
        #elif (22>=result and result<=35):
        #    print("moderate anxiety")
        #elif result>=36:
        #    print ("concerning levels of anxiety")

    df['result']=result
    df.to_csv(os.path.join(data_dir,'bai_result.csv'),index=False)

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

    drop_cols=['date','name','results']

    parse_questionnaires(drop_cols,input_dir, output_dir, 'bai.csv')
    process_bai(output_dir)




