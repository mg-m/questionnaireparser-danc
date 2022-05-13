#!/usr/bin/env python
# coding: utf-8

# In[31]:


import os
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


# In[32]:


def get_filename_without_extension(path):
        filename_basename = os.path.basename(path)
        filename_without_extension=filename_basename.split('.')[0]
        return filename_without_extension


# In[33]:


input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\visit_1\ibq'
data_list={}
for file in glob.glob(os.path.join(input_dir,"*.pdf")):
    #print(file)

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
            #print(name,values)

            if name not in data_list:
                data_list[name]=[]
            data_list[name].append(values)
            
df=pd.DataFrame(data_list)
print(df)
df.to_csv('ibq_1.csv',index=False)


# In[34]:


input_dir=r'C:\Users\mgautier\Projects\QuestionnaireParser'
df = pd.read_csv('ibq_1.csv')
df.head()
#print(df.head)
df.shape
#print (df.shape)
print(df)
df.value_counts()
df.notna()
df.dropna(how='all')

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


# In[38]:


for index, row in df.iterrows():
    
    row['act'] = row[col_list_act].mean()
    print(row)
    
    act=float(row["act"])
    print(act)
    
    df['act']=act
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['dist'] = row[col_list_dist].mean()
    print(row)
    
    dist=float(row["dist"])
    print(dist)
    
    df['dist']=dist
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['fear'] = row[col_list_fear].mean()
    print(row)
    
    fear=float(row["fear"])
    print(fear)
    
    df['fear']=fear
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['dura'] = row[col_list_dura].mean()
    print(row)
    
    dura=float(row["dura"])
    print(dura)
    
    df['dura']=dura
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['smil'] = row[col_list_smil].mean()
    print(row)
    
    smil=float(row["smil"])
    print(smil)
    
    df['smil']=smil
    df.to_csv('ibq_1_result.csv',index=False)
    
    
for index, row in df.iterrows():
    
    row['hip'] = row[col_list_hip].mean()
    print(row)
    
    hip=float(row["hip"])
    print(hip)
    
    df['hip']=hip
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['lip'] = row[col_list_lip].mean()
    print(row)
    
    lip=float(row["lip"])
    print(lip)
    
    df['lip']=lip
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['soot'] = row[col_list_soot].mean()
    print(row)
    
    soot=float(row["soot"])
    print(soot)
    
    df['soot']=soot
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['fall'] = row[col_list_fall].mean()
    print(row)
    
    fall=float(row["fall"])
    print(fall)
    
    df['fall']=8-fall
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['cudd'] = row[col_list_cudd].mean()
    print(row)
    
    cudd=float(row["cudd"])
    print(cudd)
    
    df['cudd']=cudd
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['perc'] = row[col_list_perc].mean()
    print(row)
    
    perc=float(row["perc"])
    print(perc)
    
    df['perc']=perc
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['sad'] = row[col_list_sad].mean()
    print(row)
    
    sad=float(row["sad"])
    print(sad)
    
    df['sad']=sad
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['app'] = row[col_list_app].mean()
    print(row)
    
    app=float(row["app"])
    print(app)
    
    df['app']=app
    df.to_csv('ibq_1_result.csv',index=False)
    
for index, row in df.iterrows():
    
    row['voc'] = row[col_list_voc].mean()
    print(row)
    
    voc=float(row["voc"])
    print(voc)
    
    df['voc']=voc
    df.to_csv('ibq_1_result.csv',index=False)


# In[40]:


col_list_sur= ['app','voc','hip','smil','act','perc']
for index, row in df.iterrows():
    
    row['sur'] = row[col_list_sur].mean()
    print(row)
    
    sur=float(row["sur"])
    print(sur)
    
    df['sur']=sur
    df.to_csv('ibq_1_result.csv',index=False)


col_list_reg= ['lip','cudd','dura','soot']
for index, row in df.iterrows():
    
    row['reg'] = row[col_list_reg].mean()
    print(row)
    
    reg=float(row["reg"])
    print(reg)
    
    df['reg']=reg
    df.to_csv('ibq_1_result.csv',index=False)
    
col_list_neg= ['sad','dist','fear','fall']
for index, row in df.iterrows():
    
    row['neg'] = row[col_list_neg].mean()
    print(row)
    
    neg=float(row["neg"])
    print(neg)
    
    df['neg']=neg
    df.to_csv('ibq_1_result.csv',index=False)

