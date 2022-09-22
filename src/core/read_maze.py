import os
import csv
import tkinter
from tkinter import filedialog

def create_maze_matrix(path):
    res_maze_matrix = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            replace_values_row(row) 
            if(len(row)!=0):
                res_maze_matrix.append(row)
    return res_maze_matrix

def replace_values_row(row): 
    for i in range(len(row)):
        if(row[i]=="c"):
            row[i]=0
        if(row[i]=="w"):
            row[i]=1

def read_maze():
    tkinter.Tk().withdraw()
    folder_path = filedialog.askopenfilename()
    return create_maze_matrix(folder_path)

def read_maze_default():
    dirname = os.path.dirname(__file__)
    platform = platform.system()
    default_path_img = ''
    if(platform == 'Windows') {
        default_path_img = os.path.join(dirname.split('\\src', 1)[0], 'data\\maze_5x5.csv')
    }
    else {
        default_path_img = os.path.join(dirname.split('/src', 1)[0], 'data/maze_5x5.csv')
    }
    return create_maze_matrix(default_path_img)

def __init__(self,name,roll):
    super().__init__()
    pass
