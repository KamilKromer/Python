n_ = int(input())


class Tree:
    def __init__(self, n):
        self.start_point = Branch(False, False)
        self.branchlist = []
        self.branchlist.append(self.start_point)

        for ind in range(n):
            self.branchlist.append(Branch(self.branchlist[ind], False))  # Create the first branches of the tree,
                                                                          # the False, False, ..., False path





class Branch:
    def __init__(self, parent, st):
        self.parent = parent

        self.robot = {
            False: 0,  # Czarny
            True: 0,  # Czerwony
        }

        if self.parent:  # Copy how many actions did the previous branch have
            self.robot[st] = self.parent.robot[st] + 1
            self.robot[not st] = self.parent.robot[not st]  # Also copy the other robot, but don't add one to it

