import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from tools.reader import read

data = read('input_easy.txt')

print(data)

