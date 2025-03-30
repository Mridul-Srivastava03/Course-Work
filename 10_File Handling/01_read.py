# f = open("funny.txt", "r")
# for line in f:
#     print(line)
#
# f.close()

with open ("funny.txt", 'r') as f:
    lines = f.read()
    print(lines)