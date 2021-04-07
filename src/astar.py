# Modul lain yang digunakan
import os
from math import *
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
  def __init__(self):
    self.components = []

  def loadFile(self, filename):
    cur_path = os.path.dirname(__file__)
    fpath = os.path.join(cur_path, '../test/'+filename)
    try:
      f = open(fpath, 'r')
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
        coordinates.append((float(dot[0]), float(dot[1])))
      # Ambil adjacent list
      adj = []
      for i in range(count_nodes + 1, len(lines)):
        dot = lines[i].split(" ")
        tmp = []
        for val in dot:
          #tmp.append(int(val))
          tmp.append(float(val))
        adj.append(tmp)
          
      for i in range(count_nodes):
        if (nodes[i] not in self.components):
          weight = []
          for j in range(count_nodes):
            if (adj[i][j] != 0):
              #weight.append(self.euclidean(coordinates[i],coordinates[j]))
              weight.append(self.haversine(coordinates[i],coordinates[j]))
            else:
              weight.append(0)
          value = [nodes[i],coordinates[i],adj[i],weight]
          self.components.append(value)
      
      return True

    except:
      #print("error: file not found")
      raise
      return False

  def getCoordinate(self, key):
    for value in self.components:
      if (value[0] == key):
        return value[1]
  
  def getComponent(self, key):
    for value in self.components:
      if (value[0] == key):
        return value

  def euclidean(self, startPosition, targetPosition):
    return sqrt( (startPosition[0]-targetPosition[0])**2 + (startPosition[1]-targetPosition[1])**2 )

  def straightLineDistance(self, root):
    hn = {}
    for i in range(len(self.components)):
      target = self.components[i][0]
      hn[target] = self.euclidean(self.getCoordinate(root),self.getCoordinate(target))
    return hn
  
  # distance in a spherical object, such as Earth, uses haversine formula
  # https://en.wikipedia.org/wiki/Haversine_formula
  def haversine(self, startPosition, targetPosition):
    r = 6378  # earth radius in equator (kilometer)
    p1 = pi/180 * (targetPosition[0] - startPosition[0])
    p2 = pi/180 * (targetPosition[1] - startPosition[1])
    d = 2 * r * asin(sqrt(sin(p1/2)**2 + cos((pi/180)*targetPosition[0]) * cos((pi/180)*startPosition[0]) * sin(p2/2)**2))
    return d

  def sphericalDistance(self, root):
    hn = {}
    for i in range(len(self.components)):
      target = self.components[i][0]
      hn[target] = self.haversine(self.getCoordinate(root),self.getCoordinate(target))
    return hn

  def astar(self,root,target):
    queue = []
    visited = set()
    #hn = self.straightLineDistance(root)
    hn = self.sphericalDistance(root)

    queue.append([root,0,[root]])
    visited.add(root)
    while (len(queue) != 0):
      #print(queue)
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
      print('%.2f'%queue[0][1], end = "")
      print(" km dengan rute lintasan ", end="")
      print(queue[0][2])

    return queue
  
  # def astarHaversine(self,root,target):
  #   queue = []
  #   visited = set()
  #   hn = self.sphericalDistance(root)

  #   queue.append([root,0,[root]])
  #   visited.add(root)
  #   while (len(queue) != 0):
  #     fn = []
  #     if(queue[0][0] == target):
  #       break
  #     else:
  #       # f(n) = g(n)+h(n)
  #       temp = []
  #       current = self.getComponent(queue[0][0])
  #       for i in range(len(current[3])):
  #         # [Kota, Distance, Path]
  #         path = []
  #         for node in queue[0][2]:
  #           path.append(node)
  #         if (current[3][i] != 0 and self.components[i][0] not in visited):
  #           nodeName = self.components[i][0] 
  #           fn = queue[0][1]+current[3][i]+hn.get(nodeName)

  #           path.append(nodeName)
  #           temp.append([nodeName,fn,path])

  #       if (len(temp) != 0):
  #         # Sort & Choose Lowest f(n)
  #         sorted(temp, key = lambda x: x[1])
  #         queue.append(temp[0])
  #         visited.add(temp[0][0])

  #       queue.pop(0)
  #   # {EOP : Ketemu target atau tidak}
  #   # TEMP
  #   if (len(queue) == 0):print("gak nemu")
  #   else:
  #     print("Jarak terdekat dari "+root+" ke "+target+" adalah ", end = "")
  #     print(queue[0][1], end = "")
  #     print(" dengan rute lintasan ", end="")
  #     print(queue[0][2])
  #   return queue

  def drawGraph(self, result):
    G = nx.Graph()
    nodePosition = {}

    path = []
    for i in range(len(result[0][2]) - 1):
      path.append((result[0][2][i], result[0][2][i+1]))
      path.append((result[0][2][i+1], result[0][2][i]))
    
    for i in range(len(self.components)):
      # Masukkin posisi simpul
      nodePosition[self.components[i][0]] = self.components[i][1]
      for j in range(len(self.components[i][2])):
        # Masukkin sisi
        if (self.components[i][2][j]):
          if(self.components[i][0], self.components[j][0]) in path:
            color = "red"
          else:
            color = "black"

          G.add_edge(self.components[i][0], self.components[j][0], weight=self.components[i][3][j], color=color)

    # Nampilin jarak           
    # G.add_edge(result[0][2][0], result[0][2][-1], weight='%.2f'%result[0][1], color="green")
    #edge = [(u, v) for (u, v, d) in G.edges(data=True)]
    colorNode = []
    for node in G:
      if node in result[0][2]:
        colorNode.append("blue")
      else:
        colorNode.append("white")

    options = {
        "with_labels": True,
        "node_color": colorNode,
        "edge_color": [G[i][j]["color"] for i,j in G.edges()],
        "edgecolors": "black"
    }

    # draw
    nx.draw_networkx(G, nodePosition, **options)

    # edges
    #nx.draw_networkx_edges(G, nodePosition, edgelist=edge, width=6)

    # labels
    nx.draw_networkx_labels(G, nodePosition, font_size=10, font_family="sans-serif")
    
    t = "Jarak terdekat dari "+result[0][2][0]+" ke "+result[0][2][-1]+" adalah "'%.2f'%result[0][1]+" km"
    
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.text(0.5,0.5,t,ha='center',va='center',transform=ax.transAxes)
    plt.show()