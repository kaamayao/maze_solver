import os
import glob
import time
import posixpath as path
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import matplotlib as matplotlib
from src.core.gui_maze_solver import window 
from src.core.graph import get_node_coordinates, get_node_number
from src.core.animation import Animation
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=os.cpu_count() - 1)
matplotlib.use('tkagg')
colormap = plt.cm.Set2
normalize = matplotlib.colors.Normalize(vmin=0, vmax=6)
plt.axis('off') 

def save_img(maze, index=0):
    plt.imshow(maze, cmap=colormap, norm=normalize)
    plt.savefig('./images/maze%i.png'%index)

def print_maze(maze, index=0):
    if index <= 1:
        plt.imshow(maze, cmap=colormap, norm=normalize)
        plt.savefig('./images/maze%i.png'%index)
        return
    executor.submit(save_img, maze, index)
    time.sleep(0.2)

def get_maze_step(maze, reached, frontier, path=None):
    n_maze = deepcopy(maze)
    sentinel = object()
    for node in reached:
        i,j = get_node_coordinates(maze, node)
        n_maze[i][j] = 4

    for node in frontier:
        i,j = get_node_coordinates(maze, node)
        n_maze[i][j] = 3

    if path is not None: 
        for node in path:
            i,j = get_node_coordinates(maze, node)
            n_maze[i][j] = 5
        
    return n_maze

def clear_maze_print(maze):
    Animation.clear_frame_count()
    dirname = path.dirname(__file__)
    image_path = path.join(dirname.split('/src', 1)[0], 'images/*')
    files = glob.glob(image_path)
    for f in files:
        os.remove(f)
    print_maze(maze)
    
