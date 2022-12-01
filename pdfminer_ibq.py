#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd

from utils import parse_questionnaires

# input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\data\visit_1\ibq'
# output_dit=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\derivatives\visit_1\ibq'

def process_ibq(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'ibq.csv'))

    col_list_act= ['ibqr1','ibqr2','ibqr3','ibqr12','ibqr13','ibqr14','ibqr32','ibqr33','ibqr38','ibqr39','ibqr111','ibqr112','ibqr115','ibqr116','ibqr117']
    col_list_dist= ['ibqr11','ibqr15','ibqr16','ibqr17','ibqr18','ibqr19','ibqr20','ibqr41','ibqr44','ibqr75','ibqr76','ibqr93','ibqr109','ibqr113','ibqr114','ibqr118']
    col_list_fear= ['ibqr90','ibqr94','ibqr99','ibqr150','ibqr151','ibqr152','ibqr153','ibqr154','ibqr155','ibqr156','ibqr157','ibqr158','ibqr161','ibqr162','ibqr163','ibqr164']
    col_list_dura= ['ibqr46','ibqr47','ibqr48','ibqr49','ibqr50','ibqr51','ibqr54','ibqr55','ibqr91','ibqr92','ibqr100','ibqr101']
    col_list_smil= ['ibqr34','ibqr36','ibqr37','ibqr40','ibqr43','ibqr53','ibqr56','ibqr57','ibqr110','ibqr149']
    col_list_hip= ['ibqr58','ibqr65','ibqr66','ibqr67','ibqr77','ibqr78','ibqr79','ibqr80','ibqr81','ibqr82','ibqr165']
    col_list_lip= ['ibqr59','ibqr60','ibqr61','ibqr62','ibqr63','ibqr64','ibqr68','ibqr69','ibqr70','ibqr71','ibqr72','ibqr73','ibqr74']
    col_list_soot= ['ibqr174','ibqr175','ibqr176','ibqr177','ibqr178','ibqr179','ibqr180','ibqr181','ibqr182','ibqr183','ibqr184','ibqr185','ibqr186','ibqr187','ibqr188','ibqr189','ibqr190','ibqr191']
    col_list_fall= ['ibqr21','ibqr22','ibqr23','ibqr24','ibqr25','ibqr26','ibqr27','ibqr28','ibqr29','ibqr119','ibqr120','ibqr121','ibqr122']
    col_list_cudd= ['ibqr5','ibqr6','ibqr7','ibqr105','ibqr106','ibqr107','ibqr108','ibqr123','ibqr124','ibqr125','ibqr126','ibqr127','ibqr128','ibqr129','ibqr130','ibqr131','ibqr132']
    col_list_perc= ['ibqr4','ibqr83','ibqr84','ibqr95','ibqr96','ibqr133','ibqr134','ibqr135','ibqr136','ibqr137','ibqr138','ibqr139']
    col_list_sad= ['ibqr30','ibqr31','ibqr140','ibqr141','ibqr142','ibqr143','ibqr144','ibqr145','ibqr166','ibqr167','ibqr168','ibqr169','ibqr170','ibqr171']
    col_list_app= ['ibqr85','ibqr86','ibqr87','ibqr88','ibqr89','ibqr97','ibqr98','ibqr104','ibqr159','ibqr160','ibqr172','ibqr173']
    col_list_voc= ['ibqr8','ibqr9','ibqr10','ibqr35','ibqr42','ibqr45','ibqr52','ibqr102','ibqr103','ibqr146','ibqr147','ibqr148']

    act=[]
    dist=[]
    fear=[]
    dura=[]
    smil=[]
    hip=[]
    lip=[]
    soot=[]
    fall=[]
    cudd=[]
    perc=[]
    sad=[]
    app=[]
    voc=[]

    for index, row in df.iterrows():
        s_act = float(row[col_list_act].mean())
        s_dist = float(row[col_list_dist].mean())
        s_fear = float(row[col_list_fear].mean())
        s_dura = float(row[col_list_dura].mean())
        s_smil = float(row[col_list_smil].mean())
        s_hip = float(row[col_list_hip].mean())
        s_lip = float(row[col_list_lip].mean())
        s_soot = float(row[col_list_soot].mean())
        s_fall = float(row[col_list_fall].mean())
        s_cudd = float(row[col_list_cudd].mean())
        s_perc = float(row[col_list_perc].mean())
        s_sad = float(row[col_list_sad].mean())
        s_app = float(row[col_list_app].mean())
        s_voc = float(row[col_list_voc].sum())

        act.append(s_act)
        dist.append(s_dist)
        fear.append(s_fear)
        dura.append(s_dura)
        smil.append(s_smil)
        hip.append(s_hip)
        lip.append(s_lip)
        soot.append(s_soot)
        fall.append(s_fall)
        cudd.append(s_cudd)
        perc.append(s_perc)
        sad.append(s_sad)
        app.append(s_app)
        voc.append(s_voc)

    df['act'] = act
    df['dist']=dist
    df['fear']=fear
    df['dura']=dura
    df['smil']=smil
    df['hip']=hip
    df['lip']=lip
    df['soot']=soot
    df['fall']=8-fall[0]
    df['cudd']=cudd
    df['perc']=perc
    df['sad']=sad
    df['app']=app
    df['voc']=voc

    df.to_csv(os.path.join(data_dir,'ibq_result.csv'),index=False)

    col_list_sur= ['app','voc','hip','smil','act','perc']
    col_list_reg= ['lip','cudd','dura','soot']
    col_list_neg= ['sad','dist','fear','fall']

    sur=[]
    reg=[]
    neg=[]

    for index, row in df.iterrows():
        s_sur = float(row[col_list_sur].mean())
        s_reg = float(row[col_list_reg].mean())
        s_neg = float(row[col_list_neg].mean())

        sur.append(s_sur)
        reg.append(s_reg)
        neg.append(s_neg)

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
    drop_cols=[]
    parse_questionnaires(drop_cols, input_dir, output_dir, 'ibq.csv')
    process_ibq(output_dir)