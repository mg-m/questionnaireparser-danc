#!/usr/bin/env python
# coding: utf-8

# In[67]:


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


# In[68]:


def get_filename_without_extension(path):
        filename_basename = os.path.basename(path)
        filename_without_extension=filename_basename.split('.')[0]
        return filename_without_extension


# In[75]:


input_dir=r'C:\Users\mgautier\Desktop\questionnaires'
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
df.to_csv('test.csv',index=False)


# In[ ]:




