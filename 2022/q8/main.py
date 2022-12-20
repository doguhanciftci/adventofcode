import copy
import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator='', formatter='iiiii')
data = read('input.txt', separator='', formatter='i' * 99)


class Tree:
    width = 0
    members = []
    max_vision = 0

    def __init__(self, height, left=None, right=None, up=None, bottom=None):
        self.height = height
        self.left = left
        self.right = right
        self.up = up
        self.bottom = bottom
        self.visible = None
        self.vision = 0
        Tree.members.append(self)

    def get_neighbor(self, direction):
        if direction == 'left':
            return self.left
        elif direction == 'right':
            return self.right
        elif direction == 'up':
            return self.up
        elif direction == 'bottom':
            return self.bottom
        else:
            return None

    def is_edge(self):
        return self.left is None or self.right is None or self.up is None or self.bottom is None

    def __repr__(self):
        return f"Node({self.height})"


def get_tree(lines):
    Tree.width = len(lines)
    Tree.members = []

    right_most = []
    for line in lines:
        current = None
        for l in line:
            if current is None:
                current = Tree(l)
            else:
                current.right = Tree(l, left=current)
                current = current.right
        right_most.append(current)

    while True:
        top_most = right_most[0]
        top_most.bottom = right_most[1]
        for i in range(1, len(right_most) - 1):
            right_most[i].up = right_most[i - 1]
            right_most[i].bottom = right_most[i + 1]
        right_most[-1].up = right_most[-2]

        if top_most.left is None:
            break

        right_most = [r.left for r in right_most]

    return right_most[0]


def part1(lines):
    get_tree(lines)
    for tree in Tree.members:
        if tree.is_edge():
            tree.visible = True
            continue

        for direction in ['left', 'right', 'up', 'bottom']:
            tree.visible = None
            neighbor = tree.get_neighbor(direction)
            while neighbor is not None:
                if neighbor.height >= tree.height:
                    tree.visible = False
                    break
                neighbor = neighbor.get_neighbor(direction)
            if tree.visible is None:
                tree.visible = True
                break

    return sum([1 if t.visible else 0 for t in Tree.members])


def part2(lines):
    get_tree(lines)
    for tree in Tree.members:
        if tree.is_edge():
            tree.vision = 0
            continue
        visions = [1] * 4
        directions = ['left', 'right', 'up', 'bottom']
        for i in range(4):
            direction = directions[i]
            neighbor = tree.get_neighbor(direction)
            while neighbor is not None:
                if neighbor.height >= tree.height or neighbor.is_edge():
                    break
                neighbor = neighbor.get_neighbor(direction)
                visions[i] += 1
        tree.vision = visions[0] * visions[1] * visions[2] * visions[3]
        if Tree.max_vision < tree.vision:
            Tree.max_vision = tree.vision
    return Tree.max_vision


print('Part 1:')
print(part1(data_easy))
print(part1(data))

print('\nPart 2:')
print(part2(data_easy))
print(part2(data))
