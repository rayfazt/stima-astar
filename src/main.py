from astar import *

def main():
  g = Graph()
  filename = str(input("Masukkan nama file: "))
  try:
    g.loadFile(filename)
    root = str(input("Masukkan simpul awal: "))
    target = str(input("Masukkan simpul target: "))
    try:
      result = g.astar(root, target)
      g.drawGraph(result)
    except:
      print("Tidak terdapat graf dengan simpul yang telah dimasukkan")
  except:
    print("File tidak ditemukan")
      

if __name__ == "__main__":
  main()