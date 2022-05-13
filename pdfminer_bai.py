#!/usr/bin/env python
# coding: utf-8

# In[13]:


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


# In[14]:


def get_filename_without_extension(path):
        filename_basename = os.path.basename(path)
        filename_without_extension=filename_basename.split('.')[0]
        return filename_without_extension


# In[15]:


input_dir=r'C:\Users\mgautier\Desktop\DEVMOBETA\questionnaires\visit_1\bai'
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
df.to_csv('bai_1.csv',index=False)


# In[16]:


input_dir=r'C:\Users\mgautier\Projects\QuestionnaireParser'
df = pd.read_csv('bai_1.csv')
df.head()
#print(df.head)
df.shape
#print (df.shape)
df=df.drop(columns=['date','name','results'])
print(df)
df.notna()
df.dropna(how='all')

col_list= ['bai1','bai2','bai3','bai4','bai5','bai6','bai7','bai8','bai9','bai10','bai11','bai12','bai13','bai14','bai15','bai16','bai17','bai18','bai19','bai20','bai21']
for col in col_list:
    df[col]=df[col].str.replace("/","")
    df[col]=df[col].str.replace("'","")
    df[col] = df[col].astype(float)


# In[24]:


for index, row in df.iterrows():
    
    row['result'] = row[col_list].sum()
    print(row)
    
    result=float(row["result"])
    print(result) 
    
    if result <=21: 
        print("low anxiety")
    elif (22>=result and result<=35):
        print("moderate anxiety")
    elif result>=36:
        print ("concerning levels of anxiety")

df['result']=result
df.to_csv('bai_1_result.csv',index=False)


# In[ ]:




