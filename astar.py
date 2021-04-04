import math

class Graph:
  def __init__(self):
    self.components = {}

  def loadFile(self, filename):
    try:
      f = open(filename, 'r')
      lines = f.readlines()
      for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
      f.close()
          
      # Ambil jumlah simpul
      count_nodes = int(lines[0])
      # Ambil nama simpul
      nodes = []  
      for i in range(1, count_nodes + 1):
        dot = lines[i].split(" ")
        nodes.append(dot[2])
      # Ambil koordinat
      coordinates = []
      for i in range(1, count_nodes + 1):
        dot = lines[i].split(" ")
        coordinates.append((int(dot[0]), int(dot[1])))
      # Ambil adjacent list
      adj = []
      for i in range(count_nodes + 1, len(lines)):
        dot = lines[i].split(" ")
        tmp = []
        for val in dot:
          tmp.append(int(val))
        adj.append(tmp)
          
      for i in range(count_nodes):
        if (nodes[i] not in self.components):
          weight = []
          for j in range(count_nodes):
            if (adj[i][j]):
              weight.append(self.euclideanDistance(coordinates[i],coordinates[j]))
            else:
              weight.append(0)
          value = [coordinates[i],adj[i],weight]
          self.components[nodes[i]] = value
    except:
      print("error: file not found")

  def euclideanDistance(self, startPosition, targetPosition):
    return math.sqrt( (startPosition[0]-targetPosition[0])**2 + (startPosition[1]-targetPosition[1])**2 )

  def heuristic(self,current,target):
    return self.euclideanDistance(self.components.get(current)[0],self.components.get(target)[0])

  def astar(self,root,target):
    visited = set()
    queue = []

    visited.add(root)
    queue.append(root)
    while (queue != 0):
      current = root
      fn = {}
      if(queue[0] == target):
        break
      else:
        # f(n) = g(n)+h(n)
        for i in range(len(self.components.get(current)[1])):
          fn[current] = self.components.get(current)[1][i]+ self.heuristic(current,target)
        
        # Sort

g = Graph()
filename = str(input("Masukkan nama file: "))
g.loadFile(filename)
root = str(input("Masukkan simpul awal: "))
target = str(input("Masukkan simpul target: "))
g.astar(root, target)