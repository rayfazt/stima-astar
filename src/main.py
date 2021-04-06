from astar import *

def main():
  g = Graph()
  filename = str(input("Masukkan nama file: "))
  if (g.loadFile(filename)):
    root = str(input("Masukkan simpul awal: "))
    target = str(input("Masukkan simpul target: "))
    result = g.astar(root, target)
    #print(result)
    g.drawGraph(result)

if __name__ == "__main__":
  main()