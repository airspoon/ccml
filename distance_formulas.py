def euclidean_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
        distance += (pt1[i] - pt2[i]) ** 2
    distance **= 0.5
    return distance

def manhattan_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
        distance += abs(pt1[i] - pt2[i])
    return distance

def hamming_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
        if pt1[i] != pt2[i]:
            distance += 1
    return distance

d2 = [[1, 2], [4, 0]]
d3 = [[5, 4, 3], [1, 7, 9]]

print(euclidean_distance(d2[0], d2[1]))
print(euclidean_distance(d3[0], d3[1]))

print(manhattan_distance(d2[0], d2[1]))
print(manhattan_distance(d3[0], d3[1]))

print(hamming_distance(d2[0], d2[1]))
print(hamming_distance(d3[0], d3[1]))

print(hamming_distance([1, 2], [1, 100]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))