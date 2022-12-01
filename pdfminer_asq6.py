#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd

from utils import parse_questionnaires

# input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\data\visit_2\asq'
# output_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\derivatives\visit_2\asq'

def process_asq6(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'asq_6.csv'))

    col_list_communication= ['communication1','communication2','communication3','communication4','communication5','communication6']
    col_list_gmotor= ['gmotor1','gmotor2','gmotor3','gmotor4','gmotor5','gmotor6']
    col_list_fmotor= ['fmotor1','fmotor2','fmotor3','fmotor4','fmotor5','fmotor6']
    col_list_pbsolving= ['pbsolving1','pbsolving2','pbsolving3','pbsolving4','pbsolving5','pbsolving6']
    col_list_social= ['social1','social2','social3','social4','social5','social6']

    communication=[]
    gmotor=[]
    fmotor=[]
    pbsolving=[]
    social=[]

    for index, row in df.iterrows():
        s_communication = float(row[col_list_communication].sum())
        communication.append(s_communication)

        # if communication<=29.65:
        #   print("communication deficit")
        # elif (communication>29.65 and communication<39.27):
        #   print("monitor communication")
        # elif communication>=39.27:
        #   print ("communication ok")

        s_gmotor=float(row[col_list_gmotor].sum())
        gmotor.append(s_gmotor)

        # if gmotor<=22.25:
        #     print("gmotor deficit")
        # elif (22.25>gmotor and gmotor <33.95):
        #     print("monitor gmotor")
        # elif gmotor>=33.95:
        #     print ("gmotor ok")

        s_fmotor=float(row[col_list_fmotor].sum())
        fmotor.append(s_fmotor)

        # if fmotor<=25.14:
        #     print("fmotor deficit")
        # elif (25.14>fmotor and fmotor<37.04):
        #     print("monitor fmotor")
        # elif fmotor>=37.04:
        #     print ("fmotor ok")

        s_pbsolving = float(row[col_list_pbsolving].sum())
        pbsolving.append(s_pbsolving)

        # if pbsolving<=27.72:
        #     print("pbsolving deficit")
        # elif (27.72>pbsolving and pbsolving<39.06):
        #     print("monitor pbsolving")
        # elif pbsolving>=39.06:
        #     print ("pbsolving ok")

        s_social = float(row[col_list_social].sum())
        social.append(s_social)

        # if social<=25.34:
        #     print("social deficit")
        # elif (25.34>social and social<36.83):
        #     print("monitor social")
        # elif social>=36.83:
        #     print ("social ok")

        df['communication'] = communication
        df['gmotor'] = gmotor
        df['fmotor'] = fmotor
        df['pbsolving'] = pbsolving
        df['social'] = social
        df.to_csv(os.path.join(data_dir, 'asq_6_result.csv'), index=False)

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

    drop_cols=['date','child first name','child last name','child age','initials','date of birth','nb of weeks if premature','sex','parent first name','parent last name','parent initials','link','adress','city','region','postal code','country','house phone number','other phone number','mail','people helping filling the questionnaire','subject child number','program number','program name','child age if premature','notes',
                        'communication1_score','communication2_score','communication3_score','communication4_score','communication5_score','communication6_score','communication_total_score',
                       'gmotor1_score','gmotor2_score','gmotor3_score','gmotor4_score','gmotor5_score','gmotor6_score','gmotor_total_score',
                       'fmotor1_score','fmotor2_score','fmotor3_score','fmotor4_score','fmotor5_score','fmotor6_score','fmotor_total_score',
                       'pbsolving1_score','pbsolving2_score','pbsolving3_score','pbsolving4_score','pbsolving5_score','pbsolving6_score','pbsolving_total_score',
                       'social1_score','social2_score','social3_score','social4_score','social5_score','social6_score','social_total_score',
                       'global1','global2','global3','global4','global5','global6','global7','global8','global1_no','global2_no','global3_yes','global4_yes','global5_yes','global6_yes','global7_yes','global8_yes',]

    parse_questionnaires(drop_cols, input_dir, output_dir, 'asq_6.csv')
    process_asq6(output_dir)