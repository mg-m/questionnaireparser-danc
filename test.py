#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os
import PyPDF2 as pypdf
import pandas
import pandas as pd
import glob 


# In[18]:


def get_filename_without_extension(path):
        filename_basename = os.path.basename(path)
        filename_without_extension=filename_basename.split('.')[0]
        return filename_without_extension


# In[23]:


input_dir=r'C:\Users\mgautier\Desktop\questionnaires'
data_list=[]
for file in glob.glob(os.path.join(input_dir,"*.pdf")):
    print(file)
    pdfobject=open(file, 'rb')
    pdf=pypdf.PdfFileReader(pdfobject)
    data=pdf.getFormTextFields()
    print(get_filename_without_extension(file))
    txt=get_filename_without_extension(file)
    cols=txt.split("_")
    data['subj_id']=cols[0]
    data['visit']=cols[1]
    data['questionnaire']=cols[2]
    print(data)
    data_list.append(data)
    df=pd.DataFrame(data_list)
    cols = list(df.columns.values)
    cols = cols[-1:] + cols[:-1]
    cols = cols[-1:] + cols[:-1]
    cols = cols[-1:] + cols[:-1]
    df = df[cols]
    print(cols)
    print(df)
    df.to_csv('test.csv',index=False)


# In[ ]:





# In[ ]:




