import os
import sys

# def main(algorithm, heuristic: str = ''):
#     files = os.listdir('./20120055_20120083_20120105/input/level_1')
#     print(files.__len__())

# if __name__ == "__main__":
#     if len(sys.argv) > 3:
#         print("Too many arguments")
#     elif len(sys.argv) == 3:
#         main(sys.argv[1], sys.argv[2])
#     elif len(sys.argv) == 2:
#         main(sys.argv[1])
#     else:
#         print("1 or 2 arguments are expected (algorithm, heuristic)")

files = os.listdir('.')
# ('./20120055_20120083_20120105/input/level_1')
print(files)