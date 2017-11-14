import datetime
from collections import namedtuple
import os

import numpy as np

__author__ = 'Xomak'

input_video = "video.mp4"
input_filename = "log.csv"
output_filename = "log_handled.csv"

Point = namedtuple('Point', ('x', 'y'))
TerrainSize = namedtuple('TerrainSize', ('width', 'height'))

top_left = Point(172, 159)
bottom_right = Point(1801, 664)
virtual_size = TerrainSize(bottom_right.x - top_left.x, bottom_right.y - top_left.y)  # In pixels
physical_size = TerrainSize(128, 40)  # In centimeters


def virtual_to_physical(point):
    new_x = (point.x - top_left.x) * (physical_size.width / virtual_size.width)
    new_y = (point.y - top_left.y) * (physical_size.height / virtual_size.height)
    return Point(new_x, new_y)

data = np.loadtxt(input_filename, delimiter=';', skiprows=1)
video_start_time = 1509976324#datetime.datetime.strptime('2017-06-11 13:51:00', '%Y-%m-%d %H:%M:%S')
# video_end_time = os.path.getctime(input_video)
# video_duration = data[-1, 0]

for idx, row in enumerate(data):
    data[idx, 0] = video_start_time + ((float(row[0]) - 2634.731563421829)/1000)#(video_start_time + datetime.timedelta(milliseconds=float(row[0]))).timestamp()
    physical_point = virtual_to_physical(Point(row[1], row[2]))
    data[idx, 1] = physical_point.x
    data[idx, 2] = physical_point.y

np.savetxt(output_filename, data, fmt='%10.5f', delimiter=';')