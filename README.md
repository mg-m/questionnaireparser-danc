# questionnaireparser
extract data from fillable forms 

import os
import PyPDF2 as pypdf
import pandas
import pandas as pd
import glob 

input_dir=r'directory'
data_list=[]

#extract data from file 
for file in glob.glob(os.path.join(input_dir,"*.pdf")):
    print(file)
    pdfobject=open(file, 'rb')
    pdf=pypdf.PdfFileReader(pdfobject)
    data=pdf.getFormTextFields()
    
    #extract id from filename 
    path=r'your path'
    def get_filename_without_extension(path):
        filename_basename = os.path.basename(r'your path')
        filename_without_extension=filename_basename.split('.')[0]
        return filename_without_extension
    print(get_filename_without_extension(path))
    txt=get_filename_without_extension(path)
    subj_id=txt.split("_")
    
    ##append to your dataset 
    data['subj_id']=subj_id
    data_list.append(data)
    
    #dataset in csvfile 
df=pd.DataFrame(data_list)
df.to_csv('test.csv',index=False)
