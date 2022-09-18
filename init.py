import PySimpleGUI as sg
from src.core.read_maze import read_maze, read_maze_default
from src.core.gui_maze_solver import window, update_image
from src.core.print_maze import print_maze, clear_maze_print
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
        match event:
            case('select_maze'):
                maze = read_maze()
            case('print_maze'):
                print_maze(maze)   
            case('a_star'):
                a_star_search(maze)
            case('depth'): 
                depth_search(maze)
            case('breadth'): 
                breadth_search(maze)
            case('depth_iterative'): 
                depth_iterative_search(maze)
            case('uniform'): 
                uniform_search(maze)
            case('greedy'): 
                greedy_search(maze)
            case("exit"):
                exitSolver = True
            case('update_image'):
               update_image() 
            case('prev_image'):
               clear_maze_print(maze)
            case('next_image'):
               clear_maze_print(maze)
            case('play'):
               clear_maze_print(maze)
            case(sg.WIN_CLOSED): 
                exitSolver = True

    window.close()

main()
