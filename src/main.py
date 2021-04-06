from astar import *

def main():
  g = Graph()
  filename = str(input("Masukkan nama file: "))
  if (g.loadFile(filename)):
    root = str(input("Masukkan simpul awal: "))
    target = str(input("Masukkan simpul target: "))
    #g.astar(root, target)
    g.astarHaversine(root, target)
    g.drawGraph()

if __name__ == "__main__":
  main()