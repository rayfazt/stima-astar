import os

def read_file():
    filename = "test.txt"
    try:
      f = open(filename, 'r')
      lines = f.readlines()
      for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
      return lines
    except:
      print("error: file not found")

def get_coordinates(lines):
  count_nodes = int(lines[0])
  coordinates = []
  for i in range(1, count_nodes + 1):
    dot = lines[i].split(" ")
    coordinates.append((int(dot[0]), int(dot[1])))
  return coordinates

def get_nodes(lines):
  count_nodes = int(lines[0])
  nodes = []  
  for i in range(1, count_nodes + 1):
    dot = lines[i].split(" ")
    nodes.append(dot[2])
  return nodes

def get_adjmat(lines):
  count_nodes = int(lines[0])
  adj = []
  for i in range(count_nodes + 1, len(lines)):
    dot = lines[i].split(" ")
    tmp = []
    for val in dot:
      tmp.append(int(val))
    adj.append(tmp)
  return adj

lines = read_file()
coords = get_coordinates(lines)
nodes = get_nodes(lines)
adj = get_adjmat(lines)

print(coords)
print(nodes)
print(adj)