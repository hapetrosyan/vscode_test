
import csv

def get_data():
    f = open(r'C:\Q_C_Hakob\PythonProjects\vscode_test\.vscode\my_data.csv')
    csvreader = csv.reader(f)
    my_data = list(csvreader)
    return(my_data)