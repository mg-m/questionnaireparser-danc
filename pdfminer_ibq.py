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

input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\data\visit_1\ibq'
output_dit=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\derivatives\visit_1\ibq'

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
    df=df.dropna(how='all') #delete if all values are nan
    df.to_csv(os.path.join(output_dir,'ibq.csv'),index=False)

def process_ibq(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'ibq.csv'))

    col_list_act= ['ibqr1','ibqr2','ibqr3','ibqr12','ibqr13','ibqr14','ibqr32','ibqr33','ibqr38','ibqr39','ibqr111','ibqr112','ibqr115','ibqr116','ibqr117']
    for col in col_list_act:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_dist= ['ibqr11','ibqr15','ibqr16','ibqr17','ibqr18','ibqr19','ibqr20','ibqr41','ibqr44','ibqr75','ibqr76','ibqr93','ibqr109','ibqr113','ibqr114','ibqr118']
    for col in col_list_dist:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_fear= ['ibqr90','ibqr94','ibqr99','ibqr150','ibqr151','ibqr152','ibqr153','ibqr154','ibqr155','ibqr156','ibqr157','ibqr158','ibqr161','ibqr162','ibqr163','ibqr164']
    for col in col_list_fear:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_dura= ['ibqr46','ibqr47','ibqr48','ibqr49','ibqr50','ibqr51','ibqr54','ibqr55','ibqr91','ibqr92','ibqr100','ibqr101']
    for col in col_list_dura:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_smil= ['ibqr34','ibqr36','ibqr37','ibqr40','ibqr43','ibqr53','ibqr56','ibqr57','ibqr110','ibqr149']
    for col in col_list_smil:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_hip= ['ibqr58','ibqr65','ibqr66','ibqr67','ibqr77','ibqr78','ibqr79','ibqr80','ibqr81','ibqr82','ibqr165']
    for col in col_list_hip:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_lip= ['ibqr59','ibqr60','ibqr61','ibqr62','ibqr63','ibqr64','ibqr68','ibqr69','ibqr70','ibqr71','ibqr72','ibqr73','ibqr74']
    for col in col_list_lip:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_soot= ['ibqr174','ibqr175','ibqr177','ibqr178','ibqr179','ibqr180','ibqr181','ibqr183','ibqr184','ibqr185','ibqr186','ibqr187','ibqr188','ibqr189','ibqr190','ibqr191']
    for col in col_list_soot:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_fall= ['ibqr21','ibqr22','ibqr23','ibqr24','ibqr25','ibqr26','ibqr27','ibqr28','ibqr29','ibqr119','ibqr120','ibqr121','ibqr122']
    for col in col_list_fall:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_cudd= ['ibqr5','ibqr6','ibqr7','ibqr105','ibqr106','ibqr107','ibqr108','ibqr123','ibqr124','ibqr125','ibqr126','ibqr127','ibqr128','ibqr130','ibqr131','ibqr132']
    for col in col_list_cudd:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_perc= ['ibqr4','ibqr83','ibqr84','ibqr95','ibqr96','ibqr133','ibqr134','ibqr135','ibqr136','ibqr137','ibqr138','ibqr139']
    for col in col_list_perc:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_sad= ['ibqr30','ibqr31','ibqr140','ibqr141','ibqr142','ibqr143','ibqr144','ibqr145','ibqr166','ibqr167','ibqr168','ibqr169','ibqr170','ibqr171']
    for col in col_list_sad:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_app= ['ibqr85','ibqr86','ibqr87','ibqr88','ibqr89','ibqr97','ibqr98','ibqr104','ibqr159','ibqr160','ibqr172','ibqr173']
    for col in col_list_app:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    col_list_voc= ['ibqr8','ibqr9','ibqr10','ibqr35','ibqr42','ibqr45','ibqr52','ibqr102','ibqr103','ibqr146','ibqr147','ibqr148']
    for col in col_list_voc:
        df[col]=df[col].str.replace("b","")
        df[col]=df[col].str.replace("'","")
        df[col] = df[col].astype(float)

    for index, row in df.iterrows():
        act = float(row[col_list_act].mean())
        df['act']=act
        dist = float(row[col_list_dist].mean())
        df['dist']=dist
        fear = float(row[col_list_fear].mean())
        df['fear']=fear
        dura = float(row[col_list_dura].mean())
        df['dura']=dura
        smil = float(row[col_list_smil].mean())
        df['smil']=smil
        hip = float(row[col_list_hip].mean())
        df['hip']=hip
        lip = float(row[col_list_lip].mean())
        df['lip']=lip
        soot = float(row[col_list_soot].mean())
        df['soot']=soot
        fall = float(row[col_list_fall].mean())
        df['fall']=8-fall
        cudd = float(row[col_list_cudd].mean())
        df['cudd']=cudd
        perc = float(row[col_list_perc].mean())
        df['perc']=perc
        sad = float(row[col_list_sad].mean())
        df['sad']=sad
        app = float(row[col_list_app].mean())
        df['app']=app
        voc = float(row[col_list_voc].sum())
        df['voc']=voc
        df.to_csv(os.path.join(data_dir,'ibq_result.csv'),index=False)

    col_list_sur= ['app','voc','hip','smil','act','perc']
    col_list_reg= ['lip','cudd','dura','soot']
    col_list_neg= ['sad','dist','fear','fall']

    for index, row in df.iterrows():
        sur = float(row[col_list_sur].mean())
        reg = float(row[col_list_reg].mean())
        neg = float(row[col_list_neg].mean())

        df['sur']=sur
        df['reg']=reg
        df['neg']=neg

        df.to_csv(os.path.join(data_dir,'ibq_result.csv'),index=False)

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
    process_ibq(output_dir)