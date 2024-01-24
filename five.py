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

def write_output_to_file(filename, x_coords, y_coords):
    with open(filename, 'w') as file:
        file.write(" ".join(map(lambda x: f"{x:.1f}", x_coords)))
        file.write("\n")
        file.write(" ".join(map(lambda y: f"{y:.1f}", y_coords)))

def merge_convex_hulls(convex_hulls):
    merged_points = np.concatenate(convex_hulls)
    merged_hull = jarvis_march(merged_points)
    return merged_hull

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

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    return 1 if val > 0 else 2  # clock or counterclockwise

# Read points from the input file
points1, points2 = read_points_from_file("input.txt")

# Compute convex hulls for each set of points
hull1 = jarvis_march(points1)
hull2 = jarvis_march(points2)

# Merge convex hulls
convex_hulls = [points1, points2]
merged_hull = merge_convex_hulls(convex_hulls)

# Write output to the output file
write_output_to_file("output_union.txt", merged_hull[:, 0], merged_hull[:, 1])
