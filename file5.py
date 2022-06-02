# count the num of lines in a file.
f = open('sample.txt')
data = f.readlines()
print(len(data))
f.close()