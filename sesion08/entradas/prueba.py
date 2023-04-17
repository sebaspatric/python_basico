file = open("test.txt", "w")
file.write("test1\n")
file.close()

file = open("test.txt", "r+")
file.readline()
file.write("test2")

file.seek(0)
print(file.read())
file.close()