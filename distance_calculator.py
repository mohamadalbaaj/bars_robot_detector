import subprocess
import time
from math import sqrt

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while True:
        line = process.stdout.readline().decode('utf-8')
        if line == '' and process.poll() is not None:
            break
        yield line

def print_translation_values():
    line_point = [2, 0.0, 0.5]
    line_direction = [0.000001, 0.000001, 1]
    for line in run_command('ros2 run tf2_ros tf2_echo robot_base head'):
        if "Invalid frame ID" not in line:
            data = line.split()
            if "At time" in line:
                t = data[2]
            elif "Translation:" in line:
                x = float(data[2].strip("[,"))
                y = float(data[3].strip(","))
                z = float(data[4].strip("],"))
                point = [x, y, z]
                distance = sqrt(sum([(point[i] - line_point[i])**2 for i in range(3)]) - (sum([(point[i] - line_point[i]) * line_direction[i] for i in range(3)])**2 / sum([i**2 for i in line_direction])))
                print("Time: {}, Translation: x = {}, y = {}, z = {}, Distance to line = {}".format(t, x, y, z, distance))
                if distance < 0.4:
                    print("Rebar is detected")
   
print_translation_values()





