import os
import glob
import time
from src.core.gui_maze_solver import update_image

class Animation:
    current_frame = 0

    def show_next_frame(maze): 
        dirname = os.path.dirname(__file__)
        image_path = os.path.join(dirname.split('/src', 1)[0], 'images/*')
        files = glob.glob(image_path)
        Animation.current_frame = (Animation.current_frame + 1) % len(files)
        update_image(Animation.current_frame)

    def show_prev_frame(maze): 
        dirname = os.path.dirname(__file__)
        image_path = os.path.join(dirname.split('/src', 1)[0], 'images/*')
        files = glob.glob(image_path)
        Animation.current_frame = (Animation.current_frame - 1) % len(files)
        update_image(Animation.current_frame)

    def clear_frame_count():
        Animation.current_frame = 0
        update_image(Animation.current_frame)
