#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pdfminer
import pandas
import pandas as pd
import glob 
import numpy as np
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
from pdfminer.psparser import PSLiteral, PSKeyword
from pdfminer.utils import decode_text

def get_filename_without_extension(path):
        filename_basename = os.path.basename(path)
        filename_without_extension=filename_basename.split('.')[0]
        return filename_without_extension

input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\data\visit_1\epds'
output_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\derivatives\visit_1\epds'

def parse_questionnaires(input_dir, output_dir):
    data_list={}
    for file in glob.glob(os.path.join(input_dir,"*.pdf")):

        with open(file,'rb')as fp:
            parser=PDFParser(fp)
            doc=PDFDocument(parser)
            res=resolve1(doc.catalog)

            if 'AcroForm' not in res:
                raise ValueError("No AcroForm found")

            fields=resolve1(doc.catalog['AcroForm'])['Fields']

            for f in fields :
                field = resolve1(f)
                name,values=field.get('T'),field.get('V')

                name=decode_text(name)
                values=resolve1(values)

                if name not in data_list:
                    data_list[name]=[]
                data_list[name].append(values)

    df=pd.DataFrame(data_list)
    df=df.drop(columns=['date','name','nb weeks of pregnancy','nb weeks after childbirth'])
    df=df.dropna(how='all') #delete if all values are nan
    df.to_csv(os.path.join(output_dir,'epds.csv'),index=False)

def process_epds(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'epds.csv'))

    col_list= ['epds1','epds2','epds3','epds4','epds5','epds6','epds7','epds8','epds9','epds10']
    for col in col_list:
        df[col]=df[col].str.replace("/","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    for index, row in df.iterrows():
        result = float(row[col_list].sum())

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
    parse_questionnaires(input_dir, output_dir)
    process_epds(output_dir)



