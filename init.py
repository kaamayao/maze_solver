import PySimpleGUI as sg
from src.core.read_maze import read_maze, read_maze_default
from src.core.gui_maze_solver import window, update_image
from src.core.print_maze import print_maze, clear_maze_print
from src.core.animation import Animation
from src.algorithms.a_star import a_star_search
from src.algorithms.breadth import breadth_search
from src.algorithms.depth import depth_search
from src.algorithms.depth_iterative import depth_iterative_search 
from src.algorithms.greedy import greedy_search
from src.algorithms.uniform import uniform_search

def main():
    maze = read_maze_default()
    print_maze(maze)
    exitSolver = False

    while not exitSolver:
        event, values = window.read()
        if event == 'select_maze':
            maze = read_maze()
        if event == 'print_maze':
            print_maze(maze)   
        if event == 'a_star':
            clear_maze_print(maze)
            a_star_search(maze)
        if event == 'depth':
            clear_maze_print(maze)
            depth_search(maze)
        if event == 'breadth':
            clear_maze_print(maze)
            breadth_search(maze)
        if event == 'depth_iterative':
            clear_maze_print(maze)
            depth_iterative_search(maze)
        if event == 'uniform':
            clear_maze_print(maze)
            uniform_search(maze)
        if event == 'greedy':
            clear_maze_print(maze)
            greedy_search(maze)
        if event == 'exit':
            exitSolver = True
        if event == 'update_image':
           update_image() 
        if event == 'prev_image':
           Animation.show_prev_frame(maze)
        if event == 'next_image':
           Animation.show_next_frame(maze)
        if event == 'export_gif':
           Animation.export_gif(maze)
        if event == sg.WIN_CLOSED:
            exitSolver = True

    window.close()

main()
