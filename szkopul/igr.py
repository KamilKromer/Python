n_ = int(input())


class Tree:
    def __init__(self, n):
        self.start_point = Branch(False, False, n)
        self.start_point.PopulateBranch()


class Branch:
    def __init__(self, parent, st, limit):
        self.parent = parent
        self.children = []
        self.limit = limit
        if self.parent:
            self.id = parent.id + 1
        else:
            self.id = 0

        self.robot = {
            False: 0,   # Czarny
            True: 0,    # Czerwony
        }

        if self.parent:  # Copy how many actions did the previous branch have
            self.robot[st] = self.parent.robot[st] + 1
            self.robot[not st] = self.parent.robot[not st]  # Also copy the other robot, but don't add one to it

    def PopulateBranch(self):
        if self.robot[True] < self.limit:
            self.children.append(Branch(self, True, self.limit))
        if self.robot[False] < self.limit:
            self.children.append(Branch(self, False, self.limit))

        for child in self.children:
            child.PopulateBranch()

    def Count(self):
        if len(self.children) == 0:
            return 1
        else:
            total = 1
            for child in self.children:
                total += child.Count()
            return total


def main(il):
    tr = Tree(il)
    print(tr.start_point.Count())

main(n_)