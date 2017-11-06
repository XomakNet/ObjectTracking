from collections import namedtuple
import os

import numpy as np

__author__ = 'Xomak'

input_video = "video.mp4"
input_filename = "log.csv"
output_filename = "log_handled.csv"

Point = namedtuple('Point', ('x', 'y'))
TerrainSize = namedtuple('TerrainSize', ('width', 'height'))

top_left = Point(5, 5)
bottom_right = Point(1000, 1000)
virtual_size = TerrainSize(bottom_right.x - top_left.x, bottom_right.y - top_left.y)  # In pixels
physical_size = TerrainSize(100, 100)  # In centimetrs

def virtual_to_physical(point):
    new_x = (point.x - top_left.x) * (virtual_size.width / physical_size.width)
    new_y = (point.y - top_left.y) * (virtual_size.width / physical_size.width)
    return Point(new_x, new_y)

data = np.loadtxt(input_filename, delimiter=';', skiprows=1)
video_start_time = None
# video_end_time = os.path.getctime(input_video)
# video_duration = data[-1, 0]

# for idx, row in enumerate(data):
#     row[idx, 0] = row[0] + video_start_time
#     row[idx, 1] =
