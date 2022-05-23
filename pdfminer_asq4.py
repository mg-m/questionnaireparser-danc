import os
import sys

import pdfminer
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

def process_asq1(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'questionnaire_data.csv'))

    df=df.dropna(how='all')  # delete if all values are nan

    col_list_communication = ['communication1', 'communication2', 'communication3', 'communication4', 'communication5',
                              'communication6']
    for col in col_list_communication:
        df[col] = df[col].str.replace("/", "")
        df[col] = df[col].str.replace("'", "")
        df[col] = df[col].astype(float)

    col_list_gmotor = ['gmotor1', 'gmotor2', 'gmotor3', 'gmotor4', 'gmotor5', 'gmotor6']
    for col in col_list_gmotor:
        df[col] = df[col].str.replace("/", "")
        df[col] = df[col].str.replace("'", "")
        df[col] = df[col].astype(float)

    col_list_fmotor = ['fmotor1', 'fmotor2', 'fmotor3', 'fmotor4', 'fmotor5', 'fmotor6']
    for col in col_list_fmotor:
        df[col] = df[col].str.replace("/", "")
        df[col] = df[col].str.replace("'", "")
        df[col] = df[col].astype(float)

    col_list_pbsolving = ['pbsolving1', 'pbsolving2', 'pbsolving3', 'pbsolving4', 'pbsolving5', 'pbsolving6']
    for col in col_list_pbsolving:
        df[col] = df[col].str.replace("/", "")
        df[col] = df[col].str.replace("'", "")
        df[col] = df[col].astype(float)

    col_list_social = ['social1', 'social2', 'social3', 'social4', 'social5', 'social6']
    for col in col_list_social:
        df[col] = df[col].str.replace("/", "")
        df[col] = df[col].str.replace("'", "")
        df[col] = df[col].astype(float)

    score_data={
        'subject_id':[],
        'communication_score':[],
        'gross_motor_score':[],
        'fine_motor_score':[],
        'pbsolving_score':[],
        'social_score':[]
    }
    for index, row in df.iterrows():

        subject_id=row['subject number']

        comm_score = float(row[col_list_communication].sum())

        #for asq4
        # if comm_score <= 34.6:
        #     print("communication deficit")
        # elif (comm_score > 34.6 and comm_score < 43.44):
        #     print("monitor communication")
        # elif comm_score >= 43.44:
        #     print("communication ok")

        #for asq6
        #if comm_score <= 29.65:
        #    print("communication deficit")
        #elif (comm_score > 29.65 and comm_score < 39.27):
        #    print("monitor communication")
        #elif comm_score >= 39.27:
        #    print("communication ok")

        #for asq12
        #if comm_score <= 15.64:
        #    print("communication deficit")
        #elif (comm_score > 15.64 and comm_score < 29.43):
        #    print("monitor communication")
        #elif comm_score >= 29.43:
        #    print("communication ok")

        score_data['subject_id'].append(subject_id)
        score_data['communication_score'].append(comm_score)

        gmotor_score=float(row[col_list_gmotor].sum())
        #for asq4
        #if gmotor_score <= 38.41:
        #    print("gmotor deficit")
        #elif (38.41 > gmotor_score and gmotor_score < 46.52):
        #    print("monitor gmotor")
        #elif gmotor_score >= 46.52:
        #    print("gmotor ok")

        #for asq6
        #if gmotor_score <= 22.25:
        #    print("gmotor deficit")
        #elif (22.25 > gmotor_score and gmotor_score < 33.95):
        #    print("monitor gmotor")
        #elif gmotor_score >= 33.95:
        #    print("gmotor ok")

        #for asq12
        #if gmotor_score <= 21.49:
        #    print("gmotor deficit")
        #elif (21.49 > gmotor_score and gmotor_score < 35.71):
        #    print("monitor gmotor")
        #elif gmotor_score >= 35.71:
        #    print("gmotor ok")

        score_data['gross_motor_score'].append(gmotor_score)

        fmotor_score = float(row[col_list_fmotor].sum())

        #for asq4
        #if fmotor_score<=29.62:
            #print("fmotor deficit")
        #elif (29.62>fmotor_score and fmotor_score<40.6):
            #print("monitor fmotor")
        #elif fmotor_score>=40.6:
            #print ("fmotor ok")

        #for asq6
        #if fmotor_score <= 25.14:
        #    print("fmotor deficit")
        #elif (25.14 > fmotor_score and fmotor_score < 37.04):
        #    print("monitor fmotor")
        #elif fmotor_score >= 37.04:
        #    print("fmotor ok")

        #for asq12
        #if fmotor_score <= 34.50:
        #    print("fmotor deficit")
        #elif (34.50 > fmotor_score and fmotor_score < 43.36):
        #    print("monitor fmotor")
        #elif fmotor_score >= 43.36:
        #    print("fmotor ok")

        score_data['fine_motor_score'].append(fmotor_score)

        pbsolving_score = float(row[col_list_pbsolving].sum())

        #for asq4
        #if pbsolving_score <= 34.98:
            #print("pbsolving deficit")
        #elif (34.98 > pbsolving_score and pbsolving_score < 44.38):
            #print("monitor pbsolving")
        #elif pbsolving_score >= 44.38:
            #print("pbsolving ok")

        #for asq6
        #if pbsolving_score <= 27.72:
        #    print("pbsolving deficit")
        #elif (27.72 > pbsolving_score and pbsolving_score < 39.06):
        #    print("monitor pbsolving")
        #elif pbsolving_score >= 39.06:
        #    print("pbsolving ok")

        #for asq12
        #if pbsolving_score <= 27.32:
        #    print("pbsolving deficit")
        #elif (27.32 > pbsolving_score and pbsolving_score < 38.16):
        #    print("monitor pbsolving")
        #elif pbsolving_score >= 38.16:
        #    print("pbsolving ok")

        score_data['pbsolving_score'].append(pbsolving_score)

        social_score = float(row[col_list_social].sum())

        #for asq4
        #if social_score <= 33.16:
            #print("social deficit")
        #elif (33.16 > social_score and social_score < 42.54):
            #print("monitor social")
        #elif social_score >= 42.54:
            #print("social ok")

        #for asq6
        #if social_score <= 25.34:
        #    print("social deficit")
        #elif (25.34 > social_score and social_score < 36.83):
        #    print("monitor social")
        #elif social_score >= 36.83:
        #    print("social ok")

        #for asq12
        #if social_score <= 21.73:
        #    print("social deficit")
        #elif (21.73 > social_score and social_score < 33.73):
        #    print("monitor social")
        #elif social_score >= 33.73:
        #    print("social ok")

        score_data['social_score'].append(social_score)

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
    process_asq1(output_dir)

