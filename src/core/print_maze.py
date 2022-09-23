import os
import glob
import posixpath as path
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from src.core.gui_maze_solver import window 
from src.core.graph import get_node_coordinates, get_node_number
from src.core.animation import Animation
from copy import deepcopy
import matplotlib as matplotlib

matplotlib.use('tkagg')

def print_maze(maze, index=0):
    colormap = plt.cm.Set2
    normalize = matplotlib.colors.Normalize(vmin=0, vmax=5)
    plt.imshow(maze, cmap=colormap, norm=normalize)
    plt.axis('off') 
    plt.savefig('./images/maze%i.png'%index)
    window.write_event_value("update_image", None)

def get_maze_step(maze, reached, frontier):
    n_maze = deepcopy(maze)
    sentinel = object()
    for node in reached:
        i,j = get_node_coordinates(maze, node)
        n_maze[i][j] = 4

    for node in frontier:
        i,j = get_node_coordinates(maze, node)
        n_maze[i][j] = 3
        
    return n_maze

def clear_maze_print(maze):
    Animation.clear_frame_count()
    dirname = path.dirname(__file__)
    image_path = path.join(dirname.split('/src', 1)[0], 'images/*')
    files = glob.glob(image_path)
    for f in files:
        os.remove(f)
    print_maze(maze)
    
