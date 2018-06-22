
import csv


def read_csv_file(file_name):
    table = []
    with open(file_name, 'r') as file:
        csvfile = csv.reader(file,delimiter=",")
        for line in csvfile:
            table.append(line)
    return table

def write_csv_file(csv_table,file_name):
    with open(file_name, 'wr') as file:
        file_writer = csv.writer(file, delimiter = ' ')
        for i in range(0,len(csv_table)):
            file_writer.writerow(csv_table[i])
    return 0

def select_columns(my_table,col_indices):
    table_col = []
    for i in range(0,len(my_table)):
        table_col.append([])
        for j in col_indices:
            table_col[i].append(my_table[i][j])
#            table_col[i].append(my_table[i][j])
#    return table_col
    return table_col

def sort_by_column(my_table,col_idx):

    return 0



col_indices = [1,2,3]
my_table = read_csv_file("cancer.csv")
my_table_sub = select_columns(my_table,col_indices)
print(my_table_sub)
