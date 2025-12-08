import math
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from tools.reader import read


class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"


test_data = read("input_easy.txt", separator=",", formatter="iii")
actual_data = read("input.txt", separator=",", formatter="iii")

def calculate_distances(points):
    all_distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p = points[i]
            o = points[j]
            current_distance = math.sqrt(
                (p.x - o.x) ** 2
                + (p.y - o.y) ** 2
                + (p.z - o.z) ** 2
            )
            all_distances.append((p, o, current_distance))
    all_distances.sort(key=lambda x: x[2])
    return all_distances

def arrange_circuits(circuits, p1, p2):
    p1_circuit = None
    p2_circuit = None
    i = 0
    while i < len(circuits):
        if p1 in circuits[i]:
            p1_circuit = circuits[i]
        if p2 in circuits[i]:
            p2_circuit = circuits[i]
        if p1_circuit is not None and p2_circuit is not None:
            break
        i += 1
    
    if p1_circuit is None:
        if p2_circuit is None:
            circuits.append([p1, p2])
        else:
            p2_circuit.append(p1)
    else:
        if p2_circuit is None:
            p1_circuit.append(p2)
        else:
            if p1_circuit != p2_circuit:
                for point in p2_circuit:
                    p1_circuit.append(point)
                circuits.remove(p2_circuit)

def part1(data, iterations):
    result = 0
    points = [Point(x, y, z) for x, y, z in data]
    all_distances = calculate_distances(points)
    circuits = []
    for i in range(iterations):
        pair = all_distances[i]
        p1 = pair[0]
        p2 = pair[1]
        arrange_circuits(circuits, p1, p2)

    cn = [len(circuit) for circuit in circuits]
    cn.sort(reverse=True)
    result = cn[0] * cn[1] * cn[2]
    return result

print(f"Part 1 Test: {part1(test_data, 10)}")
print(f"Part 1 Actual: {part1(actual_data, 1000)}")


def part2(data):
    result = 0
    points = [Point(x, y, z) for x, y, z in data]
    all_distances = calculate_distances(points)
    circuits = []
    i = 0
    while i < len(all_distances):
        pair = all_distances[i]
        p1 = pair[0]
        p2 = pair[1]
        arrange_circuits(circuits, p1, p2)
        i += 1
        if len(circuits) == 1 and len(circuits[0]) == len(points):
            result = p1.x * p2.x
            break
    return result



print(f"Part 2 Test: {part2(test_data)}")
print(f"Part 2 Actual: {part2(actual_data)}")
