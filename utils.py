import glob
import os
import pandas as pd
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1
from pdfminer.psparser import PSLiteral
from pdfminer.utils import decode_text

def parse_questionnaires(drop_cols, input_dir, output_dir, output_fname):
    data_list = read_forms_data(input_dir)

    df=pd.DataFrame(data_list)
    df=df.drop(columns=drop_cols)
    df=df.dropna(how='all')
    df.to_csv(os.path.join(output_dir,output_fname),index=False)

def get_filename_without_extension(path):
    filename_basename = os.path.basename(path)
    filename_without_extension = filename_basename.split('.')[0]
    return filename_without_extension

def read_forms_data(input_dir):
    data_list = {}
    for file in glob.glob(os.path.join(input_dir, "*.pdf")):

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

                if type(values) is bytes:
                    values=decode_text(values)
                elif values is None:
                    values=''
                elif type(values) is PSLiteral:
                    values=values.name
                else:
                    print('')
                if name not in data_list:
                    data_list[name] = []
                data_list[name].append(values)
    return data_list