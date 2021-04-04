import math

class Graph:
  def __init__(self):
    self.components = []

  def loadFile(self, filename):
    try:
      f = open(filename, 'r')
      lines = f.readlines()
      for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
          
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
          value = [nodes[i],coordinates[i],adj[i],weight]
          self.components.append(value)

    except:
      print("error: file not found")

  def getCoordinate(self, key):
    for value in self.components:
      if (value[0] == key):
        return value[1]
  
  def getComponent(self, key):
    for value in self.components:
      if (value[0] == key):
        return value

  def euclideanDistance(self, startPosition, targetPosition):
    return math.sqrt( (startPosition[0]-targetPosition[0])**2 + (startPosition[1]-targetPosition[1])**2 )

  def straigthLineDistance(self, root):
    hn = {}
    for i in range(len(self.components)):
      target = self.components[i][0]
      hn[target] = self.euclideanDistance(self.getCoordinate(root),self.getCoordinate(target))
    return hn

  def astar(self,root,target):
    queue = []
    visited = set()
    hn = self.straigthLineDistance(root)

    queue.append([root,0,[root]])
    visited.add(root)
    while (len(queue) != 0):
      print(queue)
      x = input()
      fn = []
      if(queue[0][0] == target):
        break
      else:
        # f(n) = g(n)+h(n)
        temp = []
        current = self.getComponent(queue[0][0])
        for i in range(len(current[3])):
          # [Kota, Distance, Path]
          path = []
          for node in queue[0][2]:
            path.append(node)
          if (current[3][i] != 0 and self.components[i][0] not in visited):
            nodeName = self.components[i][0] 
            fn = queue[0][1]+current[3][i]+hn.get(nodeName)

            path.append(nodeName)
            temp.append([nodeName,fn,path])

        if (len(temp) != 0):
          # Sort & Choose Lowest f(n)
          sorted(temp, key = lambda x: x[1])
          queue.append(temp[0])
          visited.add(temp[0][0])

        queue.pop(0)
    # {EOP : Ketemu target atau tidak}
    # TEMP
    if (len(queue) == 0):print("gak nemu")
    else:
      print("Jarak terdekat dari "+root+" ke "+target+" adalah ", end = "")
      print(queue[0][1], end = "")
      print(" dengan rute lintasan ", end="")
      print(queue[0][2])

g = Graph()
filename = str(input("Masukkan nama file: "))
g.loadFile(filename)
root = str(input("Masukkan simpul awal: "))
target = str(input("Masukkan simpul target: "))
g.astar(root, target)