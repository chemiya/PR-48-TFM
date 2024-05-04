import csv
import pandas as pd
import csv_tools

def calculate_header(header):
    return header.split('-')[-1]

#Guarda una lista de objetos en formato csv
def writeListOfObjectsToCSV(lista,fileName):
    with open(fileName,'w',newline='', encoding='utf-8') as resultFile:
        members = [attr for attr in dir(lista[0]) if not callable(getattr(lista[0], attr)) and not attr.startswith("__")]
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows([members])

        for obj in lista:
            values = [getattr(obj, member) for member in members]
            wr.writerows([values])





#escribe el header
def writeHeader(output_object,fileName):
    with open(fileName,'w',newline='', encoding='utf-8') as resultFile:
        members = [attr for attr in dir(output_object) if not callable(getattr(output_object, attr)) and not attr.startswith("__")]
        
        res = map(calculate_header,members)

        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows([res])





#añade al final de un excel
def appendLineToExistingFile(output_object,fileName):
    with open(fileName,'a',newline='', encoding='utf-8') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        members = [attr for attr in dir(output_object) if not callable(getattr(output_object, attr)) and not attr.startswith("__")]
        values = [getattr(output_object, member) for member in members]
        wr.writerows([values])



       
        
def combineCsvList(file_list,file_name):
    combined_csv = pd.concat([pd.read_csv(f) for f in file_list])
    combined_csv.to_csv( file_name, index=False, encoding='utf-8-sig')
    