import numpy as np

# def corner_points(points: list) -> list:
#     corners = []
#
#     for i, point_i in enumerate(points):
#         is_corner = True
#         for j, point_j in enumerate(points[i:]):
#             if point_j[0] > point_i[0] and point_j[1] > point_i[1]:
#                 is_corner = False
#         if is_corner:
#             corners.append(point_i)
#
#     return corners

def corner_points(points: list) -> list:
    corners = []
    points_sorted = sorted(points)
    corners.append(points_sorted[-1])

    for point in reversed(points_sorted[:-1]):
        if point[1] > corners[-1][1]:
            corners.append(point)

    return corners





points = [(1, 1), (2, 6), (3, 3), (4, 9), (5, 4), (6, 6), (7, 8), (8, 6), (9, 2), (10, 4), (11, 2), (13, 3)]
np.random.shuffle(points)
print(points)
print(corner_points(points))