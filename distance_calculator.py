import subprocess
from math import sqrt
import csv
import matplotlib.pyplot as plt

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while True:
        line = process.stdout.readline().decode('utf-8')
        if line == '' and process.poll() is not None:
            break
        yield line
        
def print_translation_values():
    line_points = [[3.6, 0.0, 0.5], [3.6, 1.0, 0.5], [3.6, -1, 0.5]]
    line_directions = [[0.000001, 0.000001, 1], [0.000001, 0.000001, 1], [0.000001, 0.000001, 1]]
    rebar_detections = []
    for line in run_command('ros2 run tf2_ros tf2_echo odom head'):
        if "Invalid frame ID" not in line:
            data = line.split()
            if "At time" in line:
                t = data[2]
            elif "Translation:" in line:
                x = float(data[2].strip("[,"))
                y = float(data[3].strip(","))
                z = float(data[4].strip("],"))
                point = [x, y, z]
                for i in range(3):
                    line_point = line_points[i]
                    line_direction = line_directions[i]
                    distance = sqrt(sum([(point[i] - line_point[i])**2 for i in range(3)]) - (sum([(point[i] - line_point[i]) * line_direction[i] for i in range(3)])**2 / sum([i**2 for i in line_direction])))
                    if distance < 0.4:
                        rebar_detections.append([t, x, y, z, distance])
                        print("Time: {}, Translation: x = {}, y = {}, z = {}, Distance to line = {}".format(t, x, y, z, distance))
                        print("Rebar is detected")
                    try:
                        with open("rebar_detections.csv", "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(rebar_detections)
                    except Exception as e:
                        print("Error writing to file: ", e)

    # plt.scatter([detection[2] for detection in rebar_detections], [detection[3] for detection in rebar_detections])
    # plt.xlabel("y")
    # plt.ylabel("z")
    # plt.title("Rebar Detections")
    # plt.show()

print_translation_values()






