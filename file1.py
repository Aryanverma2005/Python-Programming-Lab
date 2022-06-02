# find the largest word in a file
f = open('sample.txt')
data = f.read().split()
re = max(data,key=len)
print(re)
f.close()