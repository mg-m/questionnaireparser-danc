import os
import pdfminer
import pandas
import pandas as pd
import glob
import sys
import numpy as np
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
from pdfminer.psparser import PSLiteral, PSKeyword
from pdfminer.utils import decode_text


def get_filename_without_extension(path):
    filename_basename = os.path.basename(path)
    filename_without_extension = filename_basename.split('.')[0]
    return filename_without_extension


def parse_questionnaires(input_dir, output_dir):
    data_list = {}
    for file in glob.glob(os.path.join(input_dir, "*.pdf")):
        # print(file)

        with open(file, 'rb') as fp:
            parser = PDFParser(fp)
            doc = PDFDocument(parser)
            res = resolve1(doc.catalog)

            if 'AcroForm' not in res:
                raise ValueError("No AcroForm found")

            fields = resolve1(doc.catalog['AcroForm'])['Fields']

            for f in fields:
                field = resolve1(f)
                name, values = field.get('T'), field.get('V')

                name = decode_text(name)
                values = resolve1(values)
                # print(name,values)

                if name not in data_list:
                    data_list[name] = []
                data_list[name].append(values)

    df = pd.DataFrame(data_list)
    print(df)
    df.to_csv(os.path.join(output_dir, 'questionnaire_data.csv'), index=False)

def process_bai(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'questionnaire_data.csv'))

    df=df.dropna(how='all')

    col_list= ['bai1','bai2','bai3','bai4','bai5','bai6','bai7','bai8','bai9','bai10','bai11','bai12','bai13','bai14','bai15','bai16','bai17','bai18','bai19','bai20','bai21']
    for col in col_list:
        df[col]=df[col].str.replace("/","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    score_data = {
        'subject_id': [],
        'result': []
    }

    for index, row in df.iterrows():

        subject_id = row['subject number']

        result=float(row[col_list].sum())

        #if result <= 21:
        #    print("low anxiety")
        #elif (22 >= result and result <= 35):
        #    print("moderate anxiety")
        #elif result >= 36:
        #    print("concerning levels of anxiety")

        score_data['subject_id'].append(subject_id)
        score_data['result'].append(result)

        score_df = pd.DataFrame(score_data)
        score_df.to_csv(os.path.join(data_dir, 'score_data.csv'), index=False)

if __name__=='__main__':
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
    process_bai(output_dir)