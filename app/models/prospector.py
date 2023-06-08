class Prospector():
    def __init__(self, board, gm):
        self.prospect_tree = {'prospect': 0.5, 'move': None, 'type': 'opponent', 'branch': []}
        self.tree_path = []
        self.root_info = {'board': board, 'gm': gm}

    def update_branch(self, moves, type):
        return

