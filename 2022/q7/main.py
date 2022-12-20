import copy
import sys
from tools.reader import read

# from enum import Enum

sys.path.insert(0, '../../tools')

data_easy = read('input_easy.txt', separator=' ')
data = read('input.txt', separator=' ')


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.folders = []
        self.parent = parent

    def add_file(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(folder)

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for folder in self.folders:
            size += folder.get_size()
        return size


def get_main_folder(lines):
    main = Folder('main')
    current_folder = main
    ls_mode = False
    for line in lines:
        if line[0] == '$':
            if line[1] == 'cd':
                ls_mode = False
                if line[2] == '..':
                    current_folder = current_folder.parent
                elif line[2] == '/':
                    current_folder = main
                else:
                    for folder in current_folder.folders:
                        if folder.name == line[2]:
                            current_folder = folder
                            break
            elif line[1] == 'ls':
                ls_mode = True
        elif ls_mode:
            if line[0] == 'dir':
                current_folder.add_folder(Folder(line[1], current_folder))
            else:
                current_folder.add_file(File(line[1], int(line[0])))

    return main


def part1(lines):
    main = get_main_folder(lines)
    global _size
    _size = 0

    def recurse_folder(folder):
        global _size
        size = folder.get_size()
        if size <= 100000:
            _size += size
        for folder in folder.folders:
            recurse_folder(folder)

    recurse_folder(main)
    return _size


def part2(lines):
    main = get_main_folder(lines)

    total_space = 70000000
    unused_space = 30000000
    global limit
    limit = main.get_size() - (total_space - unused_space)
    to_be_deleted = []

    def recurse_folder(folder):
        global limit
        size = folder.get_size()
        if size >= limit:
            to_be_deleted.append(size)
        for folder in folder.folders:
            recurse_folder(folder)

    recurse_folder(main)
    to_be_deleted.sort()
    return to_be_deleted[0]


print('Part 1:')
print(part1(data_easy))
print(part1(data))

print('\nPart 2:')
print(part2(data_easy))
print(part2(data))
