import numpy as np

def read_points_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        x1 = list(map(float, lines[0].split()))
        y1 = list(map(float, lines[1].split()))
        x2 = list(map(float, lines[2].split()))
        y2 = list(map(float, lines[3].split()))

    points1 = np.column_stack((x1, y1))
    points2 = np.column_stack((x2, y2))

    return points1, points2

def write_output_to_file(filename, intersect):
    with open(filename, 'w') as file:
        file.write(str(intersect))

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    return 1 if val > 0 else 2  # clock or counterclockwise

def on_segment(p, q, r):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False

def convex_hulls_intersect(points1, points2):
    hull1 = jarvis_march(points1)
    hull2 = jarvis_march(points2)

    for i in range(len(hull1)):
        for j in range(len(hull2)):
            if do_intersect(hull1[i], hull1[(i+1)%len(hull1)], hull2[j], hull2[(j+1)%len(hull2)]):
                return True

    return False

def jarvis_march(points):
    n = len(points)
    hull = []

    # Function to find the point with the lowest y-coordinate (and leftmost if tie)
    def find_p0_index(points):
        min_idx = 0
        min_y = points[0][1]
        for i in range(1, n):
            y = points[i][1]
            if (y < min_y) or (y == min_y and points[i][0] < points[min_idx][0]):
                min_y = y
                min_idx = i
        return min_idx

    p0 = find_p0_index(points)
    hull.append(p0)

    while True:
        q = (hull[-1] + 1) % n
        for i in range(n):
            if orientation(points[hull[-1]], points[i], points[q]) == 2:
                q = i
        if q == p0:
            break
        hull.append(q)

    return np.array([points[i] for i in hull])

# Read points from the input file
points1, points2 = read_points_from_file("input.txt")

# Check if convex hulls intersect
intersect = convex_hulls_intersect(points1, points2)

# Write output to the output file
write_output_to_file("output_intersect.txt", intersect)
