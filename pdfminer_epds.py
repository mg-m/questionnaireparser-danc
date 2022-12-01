#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd

from utils import parse_questionnaires

# input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\data\visit_1\epds'
# output_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\derivatives\visit_1\epds'

def process_epds(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'epds.csv'))

    col_list= ['epds1','epds2','epds3','epds4','epds5','epds6','epds7','epds8','epds9','epds10']

    result = []

    for index, row in df.iterrows():

        s_result = float(row[col_list].sum())
        result.append(s_result)

        #if result>10:
        #    print ("possible depression")

    df['result']=result
    df.to_csv(os.path.join(data_dir,'epds_result.csv'),index=False)

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

    drop_cols=['date','name','nb weeks of pregnancy','nb weeks after childbirth']

    parse_questionnaires(drop_cols, input_dir, output_dir,'epds.csv')
    process_epds(output_dir)



