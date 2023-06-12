class Prospector():
    def __init__(self, board, gm):
        self.prospect_tree = {'prospect': 0.5, 'move': None, 'side': 'opponent', 'branch': []}
        self.tree_path = []
        self.root_info = {'board': board, 'gm': gm}

    def update_branch(self, moves, side):
        branch = self.prospect_tree['branch']
        for move in self.tree_path:
            for tree in branch:
                if tree['move'] == move:
                    branch = tree['branch']
                    break
        branch = [{'prospect':0.5, 'move':move, 'side':side, 'branch':[]} for move in moves]

    def update_prospect(self, prospect):
        branch = self.__move_node()
        branch['prospect'] = prospect


    def __move_node(self):
        branch = self.prospect_tree['branch']
        for move in self.tree_path:
            for tree in branch:
                if tree['move'] == move:
                    branch = tree['branch']
                    break
        return branch



