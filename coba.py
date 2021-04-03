def read_file():
    filename = input("Masukkan nama file: ")
    f = open(filename, 'r')
    lines = f.readlines()
    print(lines)

read_file()
