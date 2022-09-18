from treelib import Node, Tree

class Tree_maze:
    root = None
    tree = Tree()

    def add_root(root):
        Tree_maze.tree.create_node('%i'%root,'%i'%root) 

    def add_node(child, parent):
        try: 
            Tree_maze.tree.create_node('%i'%child, '%i'%child, parent='%i'%parent)
        except: 
            return
    
    def print_tree():
        Tree_maze.tree.save2file('tree/tree.txt')

    def clear_tree():
        Tree_maze.tree = Tree()
